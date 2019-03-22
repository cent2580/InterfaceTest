import unittest
import requests
import os
import sys
from db_fixture import test_data

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class GetArticleTest(unittest.TestCase):
    """ 获得文章列表 """

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api_query_article'
        self.auth = ("admin", "Myself1997")

    def tearDown(self):
        print(self.result)

    def test_query_article1_eid_faild(self):
        """ eid = 2 查询结果为空 """
        r = requests.get(self.base_url, params={"eid": 2}, auth=self.auth)
        self.result = r.json()
        self.assertEqual(self.result["status"], 1002)
        self.assertEqual(self.result["message"], "查询结果不存在")

    def test_query_article1_eid_success(self):
        """ 根据eid查询结果成功 """
        r = requests.get(self.base_url, params={"eid": 1}, auth=self.auth)
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result["status"], 200)
        self.assertEqual(self.result["message"], "查询结果成功")

    def test_query_article1_title_faild(self):
        """ 关键字‘你好’ 查询结果为空 """
        r = requests.get(self.base_url, params={"title": "你好"}, auth=self.auth)
        self.result = r.json()
        self.assertEqual(self.result["status"], 1002)
        self.assertEqual(self.result["message"], "查询结果不存在")

    def test_query_article1_title_success(self):
        """ 关键字‘小’模糊查询成功 """
        r = requests.get(self.base_url, params={"title": "小"}, auth=self.auth)
        self.result = r.json()
        self.assertEqual(self.result["status"], 200)
        self.assertEqual(self.result["message"], "查询结果成功")


if __name__ == '__main__':
    test_data.init_data()  # 初始化接口测试数据
    unittest.main()
