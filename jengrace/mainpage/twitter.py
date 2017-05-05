import os

# tweepy accesses the twitter database
import tweepy as tw

ckey = os.environ["CKEY"]
csecret = os.environ["CSECRET"]
atoken = os.environ["ATOKEN"]
asecret = os.environ["ASECRET"]


class TweepyInterface():  # listener
    def retrieveSearchedTweets(self, filtered_tweet):
        auth = tw.OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        api = tw.API(auth)
        query = filtered_tweet
        max_tweets = 1  # 1 tweet/function call

        '''
        searched_tweets = []
        for tweet in tw.Cursor(api.search, q=query).items(max_tweets):
            searched_tweets.append(tweet.text)
        '''

        searched_tweets = [tweet.text for tweet in tw.Cursor(api.search, q=query).items(max_tweets)]
        return searched_tweets
