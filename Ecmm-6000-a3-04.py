#Twitter Profiler app. This is a simple script to configure the Twitter API

import tweepy
import time #https://github.com/tweepy/tweepy
import csv


# Twitter API credentials. Get yours from apps.twitter.com. Twitter acct rquired
# If you need help, visit https://dev.twitter.com/oauth/overview
consumer_key = "sdstQlBpZHrLJg61JFLwQN5Zx"
consumer_secret = "jSxZTMEfx7sY953iaVS6yXuiYdtAt2T4gYuvyw3XEBRTQ4Qacp"
access_key = "927216109828431878-r19HryK4cIT3CBSSto2DuonNONjFUBD"
access_secret = "LoWaVXPOQkV3VsjKuhqhkH3btKdQYlDltzAT6lbCRUHEO"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# this function collects a twitter profile request and returns a Twitter object
def get_profile(screen_name):
    try:
        #https://dev.twitter.com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken"

    return user_profile

#this function collects twitter profile tweets and returns Tweet objects
def get_tweets(screen_name):
    try:
        #https://developer.twitter.com/en/docs/tweets/timelines/overview describes user_timeline
        tweets = api.user_timeline(screen_name, count=20)
    except:
        user_profile = "broken"

    return tweets

s = get_profile("CitronResearch")
print "Name:" +s.name 
print "id:" +s.id_str

def get_tweets(screen_name):

    alltweets = []
    try:
        tweets = api.user_timeline(screen_name, count=200)
        print "tweets"
        alltweets.extend(tweets)
        oldest = alltweets[-1].id - 1
        print oldest
        print len(tweets)
        while len(tweets) > 0:
            tweets = api.user_timeline(screen_name, count=200, max_id=oldest)
            alltweets.extend(tweets)
            oldest = alltweets[-1].id - 1
            print "...%s tweets downloaded so far" % (len(alltweets))
    except:
        user_profile = "broken"
    return alltweets

list1 = []
t = get_tweets("CitronResearch")  
for tweet in t:
    list1.append(tweet.retweet_count)

for tweet in t:
    if tweet.retweet_count == max(list1):
        text1 = tweet.text

with open ('tweets.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id","user","created_at","text"])
    for tweet in t:
        if "FTC" in tweet.text:
            writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])


