
import os

from dotenv import load_dotenv
import tweepy

load_dotenv() #load env vars for Keys/Tokens security

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")            # get env vars from .env file
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET) # initialize OAuthHandler obj; REPLACE in .OAuthHandler(consumer_key, consumer_secret) consumer_key WITH TWITTER_API_KEY, consumer_secret WITH TWITTER_API_SECRET..
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)  # replace in set_access_token(access_token, access_token_secret), access_token with TWITTER_ACCESS_TOKEN, etc 
print("AUTH", type(auth))  #print auth ob

api = tweepy.API(auth) # use auth obj to init new api client instance; use api client line a Basilica conn; issue reqs using it
print("API CLIENT", type(api))

'''
public_tweets = api.home_timeline() # gets tweets for authentic8d user, but we want ANY USER, see BELOW:
for tweet in public_tweets:
    print(tweet.text)
'''

#def twitter_api_client():
#    return tweepy.API(auth)
if __name__ == "__main__":
    user = api.get_user("s2t2")
    print(type(user)) #> <class 'tweepy.models.User'>
    pprint(user._json)
    print(user.id)
    print(user.screen_name)
    print(user.name)
    print(user.followers_count)
    #tweets = api.user_timeline("s2t2", tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    tweets = api.user_timeline("s2t2", tweet_mode="extended", count=150)
    print(type(tweets)) #> <class 'tweepy.models.ResultSet'>
    for tweet in tweets:
        print("-----")
        print(tweet.id, tweet.full_text)

user = api.get_user('s2t2')   #originally passed in 'twitter'
print(type(user)) # print type of resp we get bk 

breakpoint()