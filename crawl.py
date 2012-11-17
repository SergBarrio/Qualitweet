#!/usr/bin/env python
import requests
import sys
from requests.auth import OAuth1
import os

# This reads tweets from Twitter's streaming API and writes them to a file.
# See Twitter's documentation here:
# https://dev.twitter.com/docs/api/1/post/statuses/filter
# You will need to change the SCREEN_NAME and PASSWORD below.

url = u'https://api.twitter.com/1/users/search.json?q=' + '%20'.join(sys.argv[1:])
client_key = u'23C1viXJOPhm35xYXnodg'
client_secret = u'leXE8HDyCxJMKzNSjv0xkxSwj3a8qaonuyIP0Gito'
resource_owner_key = u'43041495-m2utOeJQseujCsNdvtfrzml9ftz0b0xUbPRIkQ'
resource_owner_secret = u'cCzOjwfBa1YTqK8LFAJsaBBwvBxMp1vXkRuByMo'

queryoauth = OAuth1(client_key, client_secret, resource_owner_key, resource_owner_secret, signature_type='query')


# Used the get already, using id:19426551,user:nfl and id:41147159, user:nikefootball
# r = requests.get(url, auth=queryoauth)

# output = open('tweets.%d.json'%os.getpid(),'w')

# Football
# url = u'https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=nfl&count=20'
# url = u'https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=nikefootball&count=20'

# Movies
# url = u'https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=YahooMovies&count=20'
# url = u'https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=TwitterMovies&count=20'
# url = u'https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=skymovies&count=20'

r = requests.get(url, auth=queryoauth)

# build corpus of 40 tweets each from the found users
for user in r.json:
	url = u'https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=' + user['screen_name'] + '&count=1'
	corpus_r = requests.get(url, auth=queryoauth)
	for tweet in corpus_r.json:
		print tweet
