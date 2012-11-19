import ujson
import fileinput
import requests
import sys
import ast
import numpy as np
from requests.auth import OAuth1

def read_tweets():
    for line in fileinput.input():
		dict_line = ast.literal_eval(line)
		yield dict_line

tweets = read_tweets()

client_key = u'23C1viXJOPhm35xYXnodg'
client_secret = u'leXE8HDyCxJMKzNSjv0xkxSwj3a8qaonuyIP0Gito'
resource_owner_key = u'43041495-m2utOeJQseujCsNdvtfrzml9ftz0b0xUbPRIkQ'
resource_owner_secret = u'cCzOjwfBa1YTqK8LFAJsaBBwvBxMp1vXkRuByMo'

queryoauth = OAuth1(client_key, client_secret, resource_owner_key, resource_owner_secret, signature_type='query')

retweet_sum = 0
mention_sum = 0

# adj_matrix = np.random.randint(1, size=(N, N))
# print adj
user_dict = {}

for tweet in tweets:
	# print tweet['screen_name']
	# url = u'https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=' + tweet['screen_name'] + '&count=20'
	# r = requests.get(url, auth=queryoauth)
	# print r.text
	
	
	#check if we need to initialize
	if (tweet['user']['screen_name'] not in user_dict):
		user_dict[tweet['user']['screen_name']] = {}
		user_dict[tweet['user']['screen_name']]['retweets'] = 0
		user_dict[tweet['user']['screen_name']]['mentions'] = 0
	user_dict[tweet['user']['screen_name']]['retweets'] += tweet['retweet_count']
	user_dict[tweet['user']['screen_name']]['mentions'] += len(tweet['entities']['user_mentions'])
print user_dict
