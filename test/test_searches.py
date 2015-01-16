# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from config import *
from youku import YoukuSearchs


class SearchsTest(unittest.TestCase):
    def setUp(self):
        self.youku = YoukuSearchs(CLIENT_ID)

    def test_search_videos_by_tag(self):
        result = self.youku.search_videos_by_tag('Google')
        self.assertGreater(result['total'], 0)

    def test_search_videos_by_keyword(self):
        result = self.youku.search_videos_by_keyword('Google')
        self.assertGreater(result['total'], 0)

    def test_search_shows_by_keyword(self):
        result = self.youku.search_shows_by_keyword(u'柯南')
        self.assertGreater(result['total'], 0)

    def test_search_keyword_complete(self):
        result = self.youku.search_keyword_complete(u'柯南')
        self.assertGreater(result['total'], 0)

    def test_search_keyword_top(self):
        result = self.youku.search_keyword_top()
        self.assertGreater(result['total'], 0)

    def test_search_show_address_unite(self):
        result = self.youku.search_show_address_unite('54624')
        self.assertIsNotNone(result)

    def test_search_show_top_unite(self):
        result = self.youku.search_show_top_unite(u'电视剧')
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
