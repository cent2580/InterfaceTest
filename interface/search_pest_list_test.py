import unittest
import requests


class SearchPestListTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://90.63.1.7:8605/api/Category/SsearchPestList'

    def tearDown(self):
        print(self.result)

    def test_search_pest_list_null(self):
        """ 关键字为’null‘，查询结果为空 """
        r = requests.get(self.base_url, params={'key': '叶',
                                                'PageNo': 1,
                                                'PageSize': 3})
        self.result = r.json()
        self.assertEqual(self.result["ReturnCode"], '200')
        self.assertEqual(self.result["ErrorMessage"], None)


if __name__ == '__main__':
    unittest.main()
