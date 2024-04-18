import tweepy
import os

# 从环境变量中获取 Twitter 认证信息
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

def authenticate_twitter():
    """
    认证 Twitter API 并创建 API 对象。
    返回 tweepy API 对象。
    """
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

def tweet_message(message):
    """
    发送一个推文。
    参数:
        message (str): 要发布的推文内容。
    返回:
        tweepy.Status: 发送推文的状态对象。
    """
    api = authenticate_twitter()
    status = api.update_status(message)
    return status