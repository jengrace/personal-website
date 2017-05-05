#This file contains all controls that manipulate the model.
import models as m

from twitter import TweepyInterface

twitter = TweepyInterface()  # instantiate twitter object here


class Control():
    def saveUserComments(self, comment_text):
        c = m.UserComment()
        c.text = comment_text
        c.save()
        return c

    def retrieveUserComments(self):
        cmnts = m.UserComment.objects.values()
        #self.retrieveThreeLatestComments()
        return cmnts

    def retrieveThreeLatestComments(self):
        cmnts = m.UserComment.objects.all().order_by('-timestamp')[:3].values()
        return cmnts

    def saveTweet(self, tweet_text, keyword_tweet):
        t = m.LinkCommentTweet()
        t.text = tweet_text
        t.keyword = keyword_tweet
        t.save()
        return t

    def reset_db(self):
        m.UserComment.objects.all().delete()
        m.LinkCommentTweet.objects.all().delete()

    def readBannedWordList(self):
    # read casts the file being opened into a string
        wordfile = open('jengrace/static/bannedwordlist.txt')
        text = wordfile.read()
        wordlist = text.split()
        return wordlist

    def detectBannedWord(self, text):
        bannedwords = self.readBannedWordList()
        commentwordlist = []
        commentwordlist = text.split()
        for i in commentwordlist:
            for e in bannedwords:
                if i == e:
                    return True
        return False  # if the execution gets here, its because theres no banned word

    def saveTweetsFromComments(self):
        for comment in self.retrieveThreeLatestComments():  # list of last 3 comments
            comment = comment['text']
            comment = comment.split()
            for word in comment:  # each word is the "keyword"
                if len(word) >= 5:
                    tweet_list = twitter.retrieveSearchedTweets(word)
                    if len(tweet_list) > 0:  # if the keyword is tweetable
                        self.saveTweet(tweet_list[0], word)

    #returns a list of tweet objects from the database
    def retrieveTweetsFromDb(self):
        tweets = m.LinkCommentTweet.objects.all().order_by('-timestamp')[:6].values()
        return tweets
