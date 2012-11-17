#!/usr/bin/env python
import sys
import ujson as json

# This is a tool I used to shrink the data returned by the streaming api. There
# are a lot of fields it returns that are mostly useless, and removing them
# makes the data about a third the size. It also removes things that are not
# tweets and duplicate tweets. It reads json from stdin and writes json to
# stdout.

tweet_ignore = [
    'contributors', 'in_reply_to_screen_name', 'source',
    'truncated', 'id_str', 'retweeted', 'retweeted_status',
    'in_reply_to_status_id_str', 'in_reply_to_user_id_str',
    'retweeted_count', 'favorited', 'geo', 'user_id_str',
    'possibly_sensitive_editable', 'possibly_sensitive',
    ]

user_ignore = [
    'contributors_enabled', 'follow_request_sent', 'following',
    'profile_background_color', 'profile_background_image_url',
    'profile_background_image_url_https', 'default_profile_image',
    'profile_background_tile', 'profile_link_color',
    'profile_sidebar_border_color', 'profile_sidebar_fill_color',
    'profile_text_color', 'profile_use_background_image',
    'show_all_inline_media', 'status', 'notifications',
    'id_str', 'is_translator', 'profile_image_url', 'protected',
    'time_zone', 'default_profile', 'listed_count', 'geo_enabled',
    ]

def strip_dict(d,trash):
    for field in trash:
        if field in d:
            del d[field]
    nulls = [k for k,v in d.iteritems() if v==None]
    for key in nulls:
        del d[key]

seen = set()

for line in sys.stdin:
    tweet = json.loads(line)
    if 'user' not in tweet or tweet['id'] in seen:
        continue
    strip_dict(tweet,tweet_ignore)
    strip_dict(tweet['user'],user_ignore)
    print json.dumps(tweet)
    seen.add(tweet['id'])
