import tweepy
import os

# 从环境变量中获取 Twitter 认证信息
TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

def authenticate_twitter():
    """
    认证 Twitter API 并创建 API 客户端。
    返回 tweepy.Client 对象。
    """
    client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
    return client

def tweet_message(message):
    """
    使用 Twitter API v2 发送一个推文。
    参数:
        message (str): 要发布的推文内容。
    返回:
        tweepy.Response: 发送推文的响应对象。
    """
    client = authenticate_twitter()
    response = client.create_tweet(text=message)
    return response

# 示例：发送推文
if __name__ == "__main__":
    result = tweet_message("Hello Twitter v2!")
    print(result.data)  # 打印推文响应的详细信息