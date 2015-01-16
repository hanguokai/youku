# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from config import *
from youku import YoukuPlaylists

PL_ID = '23331739'
VIDEO_ID = 'XODY3NDU2MzY4'


class PlaylistsTest(unittest.TestCase):

    def setUp(self):
        self.youku = YoukuPlaylists(CLIENT_ID)

    def test_find_playlist_by_id(self):
        pl = self.youku.find_playlist_by_id(PL_ID)
        self.assertIsNotNone(pl['name'])

    def test_find_playlists_by_ids(self):
        pl = self.youku.find_playlists_by_ids(PL_ID)
        self.assertGreater(pl['total'], 0)

    def test_find_playlists_by_category(self):
        pl = self.youku.find_playlists_by_category(
            u'资讯', period='month')
        self.assertGreater(pl['total'], 0)

    def test_find_playlists_by_me(self):
        pl = self.youku.find_playlists_by_me(ACCESS_TOKEN)
        self.assertIsNotNone(pl['total'])

    def test_find_playlists_by_userid(self):
        pl = self.youku.find_playlists_by_userid(USER_ID)
        self.assertIsNotNone(pl['total'])

    def test_find_playlists_by_username(self):
        pl = self.youku.find_playlists_by_username(USER_NAME)
        self.assertIsNotNone(pl['total'])

    def test_find_videos_by_playlist(self):
        pl = self.youku.find_videos_by_playlist(PL_ID)
        self.assertIsNotNone(pl['total'])

    def test_playlist_crud(self):
        pid = self.youku.create_playlist(ACCESS_TOKEN,
                                         'title',
                                         'test,other',
                                         description='description')
        pid = self.youku.update_playlist(ACCESS_TOKEN, pid, 'update title')
        pid = self.youku.add_videos_to_playlist(ACCESS_TOKEN, pid, VIDEO_ID)
        pid = self.youku.add_videos_to_playlist(ACCESS_TOKEN, pid,
                                                'XODY4MzMyMzA4')
        pid = self.youku.set_cover_video_for_playlist(ACCESS_TOKEN,
                                                      pid, VIDEO_ID)
        self.youku.find_next_video_in_playlist(pid, VIDEO_ID)
        pid = self.youku.del_videos_from_playlist(ACCESS_TOKEN, pid, VIDEO_ID)
        pid = self.youku.destroy_playlist(ACCESS_TOKEN, pid)

if __name__ == '__main__':
    unittest.main()
