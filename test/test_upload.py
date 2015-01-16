# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from config import *
from youku import YoukuUpload


class UploadTest(unittest.TestCase):
    def setUp(self):
        self.file_info = {
            'title': u'测试优酷Python客户端上传',
            'tags': 'other',
            'description': 'Polymer video #7'
            # 'category': 'Tech'
        }

    def test_upload(self):
        UPLOAD_FILE = 'f3659211207n.mp4'
        youku = YoukuUpload(CLIENT_ID, ACCESS_TOKEN, UPLOAD_FILE)

        # youku.create(youku.prepare_video_params(**params))
        # youku.create_file()
        # youku.upload_slice()
        # youku.check()
        # youku.commit()
        # youku.cancel()
        # youku.spec()
        youku.upload(self.file_info)


if __name__ == '__main__':
    unittest.main()
