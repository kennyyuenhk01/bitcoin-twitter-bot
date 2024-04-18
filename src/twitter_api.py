import tweepy
import os

# 从环境变量中获取 Twitter 认证信息
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

def authenticate_twitter():
    """
    认证 Twitter API 并创建 API 对象。
    返回 tweepy API 对象。
    """

    # Gainaing access and connecting to Twitter API using Credentials
    client = tweepy.Client(
        consumer_key=TWITTER_API_KEY,
        consumer_secret=TWITTER_API_SECRET_KEY,
        access_token=TWITTER_ACCESS_TOKEN,
        access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
    )

    return client

def tweet_message(message):
    """
    发送一个推文。
    参数:
        message (str): 要发布的推文内容。
    返回:
        tweepy.Status: 发送推文的状态对象。
    """
    client = authenticate_twitter()
    status = client.create_tweet(message)
    return status