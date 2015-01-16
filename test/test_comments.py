# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import random
import string
from config import *
from youku import YoukuComments

VIDEO_ID = 'XODY3Njc0OTA4'
# random content
CONTENT = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))


class CommentsTest(unittest.TestCase):
    def setUp(self):
        self.youku = YoukuComments(CLIENT_ID)

    def test(self):
        comm = self.youku.find_comments_by_video(VIDEO_ID)
        self.assertIsNotNone(comm['total'])

        comm1 = self.youku.find_comment_by_id(comm['comments'][0]['id'])
        self.assertIsNotNone(comm1)

        comm2 = self.youku.find_comments_by_ids(comm1['id'])
        self.assertEqual(comm2['total'], 1)

        hot_comm = self.youku.find_hot_comments_by_video(VIDEO_ID)
        self.assertIsNotNone(hot_comm)

        comm_by_me = self.youku.find_comments_by_me(ACCESS_TOKEN)
        self.assertIsNotNone(comm_by_me)

        # comm_by_me = self.youku.find_comments_by_mention_me(ACCESS_TOKEN)
        # self.assertIsNotNone(comm_by_me)

        # comm_by_me = self.youku.find_comments_by_reply_me(ACCESS_TOKEN)
        # self.assertIsNotNone(comm_by_me)

        # comm_by_me = self.youku.find_comments_by_to_me(ACCESS_TOKEN)
        # self.assertIsNotNone(comm_by_me)


if __name__ == '__main__':
    unittest.main()
