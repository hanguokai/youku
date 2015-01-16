# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from config import *
from youku import YoukuSchemas


class SchemasTest(unittest.TestCase):

    def setUp(self):
        self.youku = YoukuSchemas(CLIENT_ID)

    def test_video_category(self):
        result = self.youku.video_category()
        self.assertIsNotNone(result['categories'])

    def test_upload_spec(self):
        result = self.youku.upload_spec()
        self.assertIsNotNone(result['allowed_max_file_size'])

    def test_comment_expression(self):
        result = self.youku.comment_expression()
        self.assertIsNotNone(result['expressions'])

    def test_show_category(self):
        result = self.youku.show_category()
        self.assertIsNotNone(result['categories'])

    def test_playlist_category(self):
        result = self.youku.playlist_category()
        # This return category not categories, maybe a bug
        self.assertIsNotNone(result['category'])

    def test_searche_top_category(self):
        result = self.youku.searche_top_category()
        self.assertIsNotNone(result['categories'])


if __name__ == '__main__':
    unittest.main()
