
#Twitter Profiler app. This is a simple script to configure the Twitter API

import tweepy
import time #https://github.com/tweepy/tweepy

# Twitter API credentials. Get yours from apps.twitter.com. Twitter acct rquired
# If you need help, visit https://dev.twitter.com/oauth/overview
consumer_key = "sdstQlBpZHrLJg61JFLwQN5Zx"
consumer_secret = "jSxZTMEfx7sY953iaVS6yXuiYdtAt2T4gYuvyw3XEBRTQ4Qacp"
access_key = "927216109828431878-r19HryK4cIT3CBSSto2DuonNONjFUBD"
access_secret = "LoWaVXPOQkV3VsjKuhqhkH3btKdQYlDltzAT6lbCRUHEO"

# this function collects a twitter profile request and returns a Twitter object
def get_profile(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        #https://dev.twitter.com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken"

    return user_profile

# uses the function to query a Twitter user. Try s = get_profile("cd_conrad")
s = get_profile("Shopify")
print "Name: " + s.name
print "ID: " + s.id_str   #This gives me the unique ID  - Do this for Shopify and Citron
