# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from config import *
from youku import YoukuPersons

PERSON_ID = '11366'


class PersonsTest(unittest.TestCase):

    def setUp(self):
        self.youku = YoukuPersons(CLIENT_ID)

    def test_find_person_by_id(self):
        pserson = self.youku.find_person_by_id(PERSON_ID)
        self.assertIsNotNone(pserson['name'])

    def test_find_persons_by_ids(self):
        result = self.youku.find_persons_by_ids(PERSON_ID)
        self.assertGreater(result['total'], 0)

    def test_find_persons_by_type(self):
        result = self.youku.find_persons_by_type('performer')
        self.assertGreater(result['total'], 0)


if __name__ == '__main__':
    unittest.main()
