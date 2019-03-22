import time
import unittest
import sys
from HTMLTestRunner import HTMLTestRunner
from db_fixture import test_data

sys.path.append('./interface')
sys.path.append('./db_fixture')


# 指定测试用例为当前文件夹下的interface目录
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')


if __name__ == '__main__':
    test_data.init_data()  # 初始化接口测试数据
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')

    runner = HTMLTestRunner(stream=fp,
                            title='接口测试',
                            description='接口测试说明')
    runner.run(discover)
    fp.close()

