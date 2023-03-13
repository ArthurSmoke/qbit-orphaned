# qbit-orphaned
Find files in download folder that not used by any torrent in qbittorrent

modified from [qbt-orphaned-downloads](https://github.com/JakeWharton/qbt-orphaned-downloads)

## Difference from [qbt-orphaned-downloads](https://github.com/JakeWharton/qbt-orphaned-downloads)
1. remove tag management function
2. only find files not used by torrents, remove find hardlink logic
4. bypass the files contain given keywords
3. add telegram notifacation

## Usage
```bash
sudo docker run -d \
	--name qbit-orphaned \
	-e QBT_HOST=http://your.domain:port \
	-e QBT_USER=user \
	-e QBT_PASS=pass \
	-e IGNORE_KEYWORD="keyword1,keyword2" \
	-e TG_BOT_TOKEN="bot_token" \
	-e TG_USER_ID=tg_userid \
	-e CRON="*/25 * * * *" \
	-v /path/to/your/downloads:/downloads \
	arthur623/qbit-orphaned
```
