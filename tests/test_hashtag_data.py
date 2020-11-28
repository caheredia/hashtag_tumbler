from unittest import TestCase

from src.hashtag_data import chicano, film, fuji, leica, sanfrancisco, street


class TestData(TestCase):
    def setUp(self):
        self.maxDiff = None
        self.groups = [chicano, film, fuji, leica, sanfrancisco, street]

    def test_for_sorted(self):
        for group in self.groups:
            self.assertListEqual(group, sorted(group))

    def test_for_duplicates(self):
        for group in [chicano, film, fuji, leica, sanfrancisco, street]:
            # self.assert((group), tuple(set(group)))
            pass
