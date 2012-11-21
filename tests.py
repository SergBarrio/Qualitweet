import unittest
import test_hubs


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