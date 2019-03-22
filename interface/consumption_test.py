import unittest
import requests
from requests.auth import HTTPBasicAuth


class ConsumptionTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://hzzskj.tpddns.cn:8603/api/ShopInfo/consumption'

    def tearDown(self):
        print(self.result)

    def test_consumption(self):
        """ type = 1，查询今日数据 """
        r = requests.get(self.base_url, params={"type": 1},
                         headers={"Authorization":
                                      "Basic R09ISTo4Ris1c2lwRDlxRUJtaW9kNmtWWVBBL21tTDlyQVdaMTgxVXRDMjNkQ2h3PQ=="})
        self.result = r.json()
        self.assertEqual(self.result["ReturnCode"], '200')
        self.assertEqual(self.result["ErrorMessage"], None)
        self.assertEqual(self.result["Data"]["countParam"][1]['count'], 2)
        self.assertEqual(self.result["Data"]["countParam"][0]['count'], 0)


if __name__ == '__main__':
    unittest.main()
