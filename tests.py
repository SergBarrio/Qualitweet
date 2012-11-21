import unittest
import test_hubs
import numpy as np


MENTION_CORPUS = [
    {
        "text":"@bob Howdy!",
        "id":101,
        "entities":{"user_mentions":[{"id":2,"screen_name":"bob"}]},
        "user":{"id":4,"screen_name":"Diane"}
    },
    {
        "text":"Welcome @bob and @alice!",
        "id":102,
        "entities":{"user_mentions":[
            {"id":1,"screen_name":"alice"},
            {"id":2,"screen_name":"bob"}
        ]},
        "user":{"id":3,"screen_name":"charlie"}
    },
    {
        "text":"Hi @charlie and @alice!",
        "id":103,
        "entities":{"user_mentions":[
            {"id":1,"screen_name":"alice"},
            {"id":3,"screen_name":"charlie"}
        ]},
        "user":{"id":2,"screen_name":"BOB"}
    },
    {
        "text":"Howdy!",
        "id":104,
        "entities":{"user_mentions":[]},
        "user":{"id":1,"screen_name":"Alice"}
    }
]

class TestQualitweet(unittest.TestCase):
    def setUp(self):
        self.qualitweet = test_hubs.Qualitweet()
        
    def test_index_tweets(self):
    
        test_dict = {
                'charlie': {
                    'mentioned': ['alice', 'bob'], 
                    'mentioned_by': ['BOB']
                }, 
                 'Diane': {
                    'mentioned': ['bob'], 
                    'mentioned_by': []
                },
                 'alice': {
                    'mentioned': [], 
                    'mentioned_by': ['charlie', 'BOB']
                }, 
                'Alice': {
                    'mentioned': [], 
                    'mentioned_by': []
                }, 
                'bob' : {
                    'mentioned': [], 
                    'mentioned_by': ['Diane', 'charlie']
                }, 
                'BOB': {
                    'mentioned': ['alice', 'charlie'], 
                    'mentioned_by': []
                }
            }
    
        self.qualitweet.index_tweets(MENTION_CORPUS)
        self.assertEqual(test_dict,self.qualitweet.user_dict)
        
    def test_compute_score(self):
    
        hub = [[ 2, 1, 0, 0, 0, 1],
                 [ 1, 1, 0, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0],
                 [ 1, 0, 0, 0, 0, 2]]
                     
        authority =  [[ 1, 0, 1, 0, 0, 0],
                     [ 0, 0, 0, 0, 0, 0],
                     [ 1, 0, 2, 0, 1, 0],
                     [ 0, 0, 0, 0, 0, 0],
                     [ 0, 0, 1, 0, 2, 0],
                     [ 0, 0, 0, 0, 0, 0]]
    
        self.qualitweet.index_tweets(MENTION_CORPUS)
        self.qualitweet.compute_score()
        
        calculated_hub = self.qualitweet.scores[0]
        calculated_auth = self.qualitweet.scores[1]
        
        i = 0
        for row in hub:
            j = 0
            for score in row:
                self.assertEqual(score,calculated_hub[i][j])
                j = j + 1
            i = i + 1
        
        i = 0
        for row in authority:
            j = 0
            for score in row:
                self.assertEqual(score,calculated_auth[i][j])
                j = j + 1
            i = i + 1
        
if __name__ == '__main__':
    unittest.main()