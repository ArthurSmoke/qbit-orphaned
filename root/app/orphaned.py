import os
import qbittorrentapi
from telegram import send_telegram_message

DOWNLOADS_PATH = "/downloads"
IGNORE_LIST = filter(None, os.environ['IGNORE_KEYWORD'].split(','))
HOST = os.environ['QBT_HOST']
USER = os.environ['QBT_USER']
PASS = os.environ['QBT_PASS']


# find all files in download folder
files_in_download_folder=[]
for dir_path, _, file_names in os.walk(DOWNLOADS_PATH):
	for file_name in file_names:
		full_path = os.path.join(dir_path, file_name)
		relative_path = os.path.relpath(full_path, DOWNLOADS_PATH)
        # ignore the file that contain ignore keyword
		if not any(ignore_text in relative_path for ignore_text in IGNORE_LIST):
		    files_in_download_folder.append(relative_path)


client = qbittorrentapi.Client(
    host=HOST, username=USER, password=PASS
)


try:
    client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)

torrents = client.torrents.info()
if len(torrents) > 0:
    for torrent in torrents:
        for file in torrent.files:
            if file.name in files_in_download_folder:
                files_in_download_folder.remove(file.name)
    files_not_used = '\n'.join(files_in_download_folder)
    print("Please Check Below Orphaned Files:")
    print(files_not_used)
    send_telegram_message(files_not_used)