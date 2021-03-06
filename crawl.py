#!/usr/bin/env python
import requests
import sys
from requests.auth import OAuth1
import os

# This reads tweets from Twitter's streaming API and writes them to a file.
# See Twitter's documentation here:
# https://dev.twitter.com/docs/api/1/post/statuses/filter
# You will need to change the SCREEN_NAME and PASSWORD below.

client_key = u''
client_secret = u''
resource_owner_key = u''
resource_owner_secret = u''

queryoauth = OAuth1(client_key, client_secret, resource_owner_key, resource_owner_secret, signature_type='query')

# build corpus of 40 tweets each from the found users
page = 1
f = open('test.json', 'w')
while (page < 5):
	# This will get 20 (the max) users on one page
	url = u'https://api.twitter.com/1/users/search.json?q=' + '%20'.join(sys.argv[1:]) + '&page=' + repr(page) + '&per_page=20'

	r = requests.get(url, auth=queryoauth)
	
	for user in r.json:
		# print user['screen_name']
		url = u'https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=' + user['screen_name'] + '&count=40'
		corpus_r = requests.get(url, auth=queryoauth)
		for tweet in corpus_r.json:
			f.write( str(tweet)+'\n' )
	page+=1