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

class Qualitweet(object):
    def __init__(self):    
        client_key = u'23C1viXJOPhm35xYXnodg'
        client_secret = u'leXE8HDyCxJMKzNSjv0xkxSwj3a8qaonuyIP0Gito'
        resource_owner_key = u'43041495-m2utOeJQseujCsNdvtfrzml9ftz0b0xUbPRIkQ'
        resource_owner_secret = u'cCzOjwfBa1YTqK8LFAJsaBBwvBxMp1vXkRuByMo'
        
        self.scores = []

        self.queryoauth = OAuth1(client_key, client_secret, resource_owner_key, resource_owner_secret, signature_type='query')
        
    def index_tweets(self,tweets):
        # adj_matrix = np.random.randint(1, size=(N, N))
        # print adj
        self.user_dict = {}

        # Go outside the corpus by one layer
        # Obviously we look within the tweets we find (probably expand the users we find)
        # But we also take the first 40-100 tweets of the users mentioned by the first users
        # If they mention or mention others we'll get a reasonable h/a matrix
        for tweet in tweets:
            # print tweet['screen_name']
            # url = u'https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=' + tweet['screen_name'] + '&count=20'
            # r = requests.get(url, auth=queryoauth)
            # print r.text
            curr_user = tweet['user']['screen_name']
            
            # find user, see who they mentioned
            if (tweet['user']['screen_name'] not in self.user_dict):
                self.user_dict[curr_user] = {}
                self.user_dict[curr_user]['mentioned'] = []
                self.user_dict[curr_user]['mentioned_by'] = []
            # list the users mentioned by a user and who mentioned that user
            for mentioned_user in tweet['entities']['user_mentions']:
                # don't add a mentioned user twice
                if ( mentioned_user['screen_name'] not in self.user_dict[curr_user]['mentioned'] ):
                    self.user_dict[curr_user]['mentioned'].append(mentioned_user['screen_name'])
                    
                # also add the mentioned user to the dictionary for the next part
                if ( mentioned_user['screen_name'] not in self.user_dict ):
                    self.user_dict[mentioned_user['screen_name']] = {}
                    self.user_dict[mentioned_user['screen_name']]['mentioned'] = []
                    self.user_dict[mentioned_user['screen_name']]['mentioned_by'] = []
                    
                # now add current user to the mentioned users 'mentioned_by'
                if ( curr_user not in self.user_dict[mentioned_user['screen_name']]['mentioned_by'] ):
                    self.user_dict[mentioned_user['screen_name']]['mentioned_by'].append(curr_user)
                
                
    def compute_score(self):
        self.scores = []
    
        # We now have a dictionary
        # start with a 'row' of all zeroes
        adjacency = []
        adjacency = adjacency + [0]*(len(self.user_dict) - len(adjacency))
        # Adjacency Matrix
        A = np.zeros( shape=(len(self.user_dict), len(self.user_dict)) )
        # keep track of A's rows
        outer_count = 0
        for mentioning_user in self.user_dict:
            inner_count = 0
            for mentioned_user in self.user_dict:
                if( mentioned_user in self.user_dict[mentioning_user]['mentioned'] ):
                    adjacency[inner_count] = 1
                else:
                    adjacency[inner_count] = 0
                inner_count += 1
            # print adjacency
            A[outer_count] = adjacency
            outer_count += 1
            
        self.scores = [np.dot(A, np.transpose(A)), np.dot(np.transpose(A), A)]
        
if __name__ == '__main__':
    tweets = read_tweets()
    
    algorithm = Qualitweet()
    algorithm.index_tweets(tweets)
    algorithm.compute_score()
