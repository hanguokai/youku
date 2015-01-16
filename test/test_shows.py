# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from config import *
from youku import YoukuShows

SHOW_ID = 'zeebadce421c911e4a705'


class ShowsTest(unittest.TestCase):

    def setUp(self):
        self.youku = YoukuShows(CLIENT_ID)

    def test_find_show_by_id(self):
        show = self.youku.find_show_by_id(SHOW_ID)
        self.assertIsNotNone(show['name'])

    def test_find_shows_by_ids(self):
        show = self.youku.find_shows_by_ids(SHOW_ID)
        self.assertGreater(show['total'], 0)

    def test_find_show_premium_by_ids(self):
        show = self.youku.find_show_premium_by_ids(SHOW_ID)
        self.assertGreater(show['total'], 0)

    def test_find_shows_by_category(self):
        show = self.youku.find_shows_by_category(u'电视剧', u'古装')
        self.assertGreater(show['total'], 0)

    def test_find_shows_by_related(self):
        show = self.youku.find_shows_by_related(SHOW_ID)
        self.assertIsNotNone(show['total'])

    def test_find_videos_by_show(self):
        show = self.youku.find_videos_by_show(SHOW_ID)
        self.assertGreater(show['total'], 0)

if __name__ == '__main__':
    unittest.main()
