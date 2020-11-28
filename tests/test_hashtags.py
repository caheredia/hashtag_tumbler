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
