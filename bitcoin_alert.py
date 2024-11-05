#!/usr/bin/python3

from requests import Session
import json
import time
import requests

def get_btc_Info(): # Function to get the info

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest' # Coinmarketcap API url

    api = 'your_api_key' # Replace this with your API key

    parameters = { 'slug': 'bitcoin', 'convert': 'USD' } # API parameters to pass in for retrieving specific cryptocurrency data

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api
    } # Headers for the API request

    session = Session() # Create new session object to manage API requests
    session.headers.update(headers) #Update the session headers with the specified headers

    response = session.get(url, params=parameters) # Receiving the response from the API

    info = json.loads(response.text)
    name = name = info['data']['1']['name']
    data = info['data']['1']['quote']['USD']
    date = data['last_updated']
    price = data['price']
    percent_change_24h = data['percent_change_24h']
    percent_change_7d = data['percent_change_7d']
    percent_change_30d = data['percent_change_30d']
    percent_change_90d = data['percent_change_90d']
    
    btc_info = {'name':name, 'last_updated':date,
                'price':price, 
                'percent_change_24h':percent_change_24h,
                'percent_change_7d':percent_change_7d,
                'percent_change_30d':percent_change_30d,
                'percent_change_90d':percent_change_90d
               }
    
    return btc_info 

# send telegram message through telegram bot to your telegram account
def send_message(TOKEN, chatID, message):
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chatID}&text={message}"
    
    requests.get(url).json()
    
def main():
    #bitcoin_history = []
    price = get_btc_Info()['price']
    while True:

        if price < BITCOIN_LOWER_THRESHOLD:
            message = f'Alert! Daily btc updates: {price}' #replace this with any message that you prefer
            send_message(bot_token, chatID, message)
            return 

        if price > BITCOIN_UPPER_THRESHOLD:
            message = f'Alert! Daily btc updates: {price}' #replace this with any message that you prefer
            send_message(bot_token, chatID, message)
            return 

        messagge = f'Daily btc updates: {price}' #replace this with any message that you prefer
        send_message(bot_token, chatID, message)
        return 
        
bot_token = 'telegram_bot_token' # replace this with your telegram bot token
chatID = 'telegram)_chatID' # replace this with your telegram chat_id

BITCOIN_LOWER_THRESHOLD = 55000 #replace this with any number that you prefer
BITCOIN_UPPER_THRESHOLD = 60000 #replace this with any number that you prefer

if __name__ == '__main__':
    main()
