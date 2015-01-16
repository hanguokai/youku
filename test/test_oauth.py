# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from config import *
from youku import YoukuOauth


class OauthTest(unittest.TestCase): pass
    # TODO

if __name__ == '__main__':
    unittest.main()
