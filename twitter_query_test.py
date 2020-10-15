'''
    twitter_query_test.py
    
    This file tests twitter_query.py.
'''

import unittest
from twitter_query import get_relevant_tweets, get_random_tweet
from twitter_query import KEY_CONTENTS, KEY_DATE, KEY_AUTHOR, KEY_URL
from twitter_query import DATABASE_URL, TWITTER_ACCESS_TOKEN, \
            TWITTER_ACCESS_TOKEN_SECRET, TWITTER_KEY, TWITTER_KEY_SECRET

from dotenv import load_dotenv
import tweepy
import random
import os
from os.path import join, dirname


KEY_INPUT = "input"
KEY_EXPECTED = "expected"

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)
dotenv_path = join(dirname(__file__), 'tweepy.env')
load_dotenv(dotenv_path)

class TwitterQueryTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "Biggie Smalls",
                KEY_EXPECTED: {}
            },
            {
                KEY_INPUT: "Tupac Shakur",
                KEY_EXPECTED: {}
            },
            {
                KEY_INPUT: "Beyonce Knowles",
                KEY_EXPECTED: {}
            },
        ]

    def test_auth_success(self):
        for test_case in self.success_test_params:
            relevant_tweets = get_relevant_tweets(
                query = "Biggie",
                access_token = TWITTER_ACCESS_TOKEN,
                access_token_secret = TWITTER_ACCESS_TOKEN_SECRET,
                key = TWITTER_KEY,
                key_secret = TWITTER_KEY_SECRET,
                count = 10)
            first_tweet = relevant_tweets[0]
            self.assertEqual(first_tweet[KEY_AUTHOR], "@CMecenary")

        
if __name__ == '__main__':
    unittest.main()