# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from config import *
from youku import YoukuUsers


class UserTest(unittest.TestCase):
    def setUp(self):
        self.youku = YoukuUsers(CLIENT_ID)

    def test_my_info(self):
        me = self.youku.my_info(ACCESS_TOKEN)
        self.assertIn('id', me)

    def test_by_id(self):
        user = self.youku.find_user_by_id('419384312')
        self.assertEqual(user['name'], u'韩国恺')

    def test_by_ids(self):
        users = self.youku.find_users_by_ids('419384312,155482632')
        self.assertEqual(users['total'], 2)

    def test_by_name(self):
        user = self.youku.find_user_by_name(u'GDGBeijing')
        self.assertEqual(user['id'], '155482632')

    def test_by_names(self):
        users = self.youku.find_users_by_names(u'GDGBeijing,韩国恺')
        self.assertEqual(users['total'], 2)

    def test_friendship_followings(self):
        users = self.youku.friendship_followings(user_id='419384312')
        self.assertIn('total', users)

    def test_friendship_followers(self):
        users = self.youku.friendship_followers(user_name='GDGBeijing')
        self.assertIn('total', users)

    def test_friendship_create_destroy(self):
        self.youku.create_friendship(ACCESS_TOKEN, user_name='GDGBeijing')
        self.youku.destroy_friendship(ACCESS_TOKEN, user_name='GDGBeijing')

    def test_subscribe_create_cancel(self):
        self.assertTrue(self.youku.create_subscribe(ACCESS_TOKEN,
                        '2a7260de1faa11e097c0'))
        self.assertTrue(self.youku.cancel_subscribe(ACCESS_TOKEN,
                        '2a7260de1faa11e097c0'))

    def test_subscribe_get(self):
        self.assertIn('total', self.youku.subscribe_get(ACCESS_TOKEN))

    def test_subscribe_notice(self):
        self.assertIn('total', self.youku.subscribe_notice(ACCESS_TOKEN))

if __name__ == '__main__':
    unittest.main()
