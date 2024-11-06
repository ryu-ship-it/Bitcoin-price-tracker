A simple Bitcoin tracker that checks Bitcoin prices and sends notifications via Telegram. 
I've used the website [CoinMarketCap](https://coinmarketcap.com/api/documentation/v1/) to track the Bitcoin price. 
You can register here [Register for CoinMarketCap's API](https://coinmarketcap.com/academy/article/register-for-coinmarketcap-api) to get your API key.

### 1. Setup
```

python3 -m venv venv
source ./venv/bin/activate
pip3 install requests
```
### 2. Get the telegram bot token and chatId
[create telegram chat bot and get chatid](https://www.youtube.com/watch?v=l5YDtSLGhqk&ab_channel=NextGenVision)


### 2. Run code using 
```
python3 bitcoin_alert.py
```
If you want to schedule this code to run, you can use corn 
on terminal 
```
crontab -e
```
and in the crontab file
```
0 0 * * * /usr/bin/python3 /path_to_file/bitcoin_alert.py
```
this should help you run the job daily at 0 clock
 
