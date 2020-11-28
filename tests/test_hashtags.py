from random import randint
from unittest import TestCase

from src.hashtag_data import (
    chicano,
    film,
    fuji,
    leica,
    mediumformat,
    sanfrancisco,
    street,
)
from src.hashtags import k_random_hashtags, parse_hashtag_string, return_hashtags


class TestHashtags(TestCase):
    def setUp(self):
        self.groups = [chicano, film, fuji, leica, mediumformat, sanfrancisco, street]

    def test_k_random_hashtags(self):
        for group in self.groups:
            group_len = len(group)
            random_int = randint(0, group_len)

            random_hashtags = k_random_hashtags(hashtag_list=group, k=random_int)
            string_of_hashtags = return_hashtags(random_hashtags)
            list_of_parsed_hashtags = parse_hashtag_string(string_of_hashtags)

            self.assertEqual(len(list_of_parsed_hashtags), random_int)
