import os
import requests
from twitter_api import tweet_message

# 环境变量
CRYPTOCOMPARE_API_KEY = os.getenv('CRYPTOCOMPARE_API_KEY')

def get_bitcoin_price():
    url = 'https://min-api.cryptocompare.com/data/price'
    parameters = {
        'fsym': 'BTC',
        'tsyms': 'USD',
        'api_key': CRYPTOCOMPARE_API_KEY
    }
    response = requests.get(url, params=parameters)
    data = response.json()
    return data['USD']

def main():
    try:
        price = get_bitcoin_price()
        print(f"Current Bitcoin Price: ${price} USD")
        message = f"Current Bitcoin price: ${price} USD"
        tweet = tweet_message(message)
        print("Tweet sent successfully:", tweet.text)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()