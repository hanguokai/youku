# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from config import *
from youku import YoukuVideos

VIDEO_ID = 'XODY3NDU2MzY4'
VIDEO_URL = 'http://v.youku.com/v_show/id_XODY3NDU2MzY4.html'


class VideosTest(unittest.TestCase):

    def setUp(self):
        self.youku = YoukuVideos(CLIENT_ID)

    def test_find_by_id(self):
        video = self.youku.find_video_by_id(VIDEO_ID)
        self.assertIsNotNone(video)

    def test_find_by_url(self):
        video = self.youku.find_video_by_url(VIDEO_URL)
        self.assertIsNotNone(video)

    def test_find_by_ids(self):
        video = self.youku.find_videos_by_ids(VIDEO_ID)
        self.assertIsNotNone(video['total'])

    def test_find_video_detail_by_id(self):
        video = self.youku.find_video_detail_by_id(VIDEO_ID)
        self.assertIsNotNone(video)

    def test_find_video_details_by_ids(self):
        video = self.youku.find_video_details_by_ids(VIDEO_ID)
        self.assertIsNotNone(video['total'])

    def test_find_videos_by_me(self):
        video = self.youku.find_videos_by_me(ACCESS_TOKEN)
        self.assertIsNotNone(video['total'])

    def test_find_videos_by_userid(self):
        video = self.youku.find_videos_by_userid(USER_ID)
        self.assertIsNotNone(video['total'])

    def test_find_videos_by_username(self):
        video = self.youku.find_videos_by_username(USER_NAME)
        self.assertIsNotNone(video['total'])

    def test_update_video(self):
        vid = self.youku.update_video(ACCESS_TOKEN, VIDEO_ID, 'update title')
        self.assertIsNotNone(vid)

    # def test_destroy_video(self):
    #     vid = self.youku.destroy_video(ACCESS_TOKEN, 'XODY3MzI5NDM2')
    #     self.assertIsNotNone(vid)

    def test_find_videos_by_related(self):
        video = self.youku.find_videos_by_related(VIDEO_ID)
        self.assertIsNotNone(video['total'])

    def test_find_favorite_videos_by_me(self):
        video = self.youku.find_favorite_videos_by_me(ACCESS_TOKEN)
        self.assertIsNotNone(video['total'])

    def test_find_favorite_videos_by_userid(self):
        video = self.youku.find_favorite_videos_by_userid(USER_ID)
        self.assertIsNotNone(video['total'])

    def test_find_favorite_videos_by_username(self):
        video = self.youku.find_favorite_videos_by_username(USER_NAME)
        self.assertIsNotNone(video['total'])

    def test_create_favorite_video(self):
        vid = self.youku.create_favorite_video(ACCESS_TOKEN, VIDEO_ID)
        self.assertIsNotNone(vid)

    def test_destroy_favorite_video(self):
        vid = self.youku.destroy_favorite_video(ACCESS_TOKEN, VIDEO_ID)
        self.assertIsNotNone(vid)

    def test_find_videos_by_category(self):
        video = self.youku.find_favorite_videos_by_username(u'资讯', u'社会资讯')
        self.assertIsNotNone(video['total'])


if __name__ == '__main__':
    unittest.main()
