from pymysql import connect, cursors
from pymysql.err import OperationalError
import os
import configparser as cparser

# 读取db_config配置文件
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + '/db_config.ini'

cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get('mysqlconf', 'host')
port = cf.get('mysqlconf', 'port')
db = cf.get('mysqlconf', 'db_name')
user = cf.get('mysqlconf', 'user')
password = cf.get('mysqlconf', 'password')


# 封装MySQL基本操作
class DB:
    def __init__(self):
        try:
            # 连接MySQL数据库
            self.connection = connect(
                host=host,
                port=int(port),
                user=user,
                password=password,
                db=db,
                charset='utf8mb4',
                cursorclass=cursors.DictCursor
            )
        except OperationalError as e:
            print('MySQL Error %d：%s' % (e.args[0], e.args[1]))

    def clear(self, table_name):
        # 清除表数据
        real_sql = "delete from " + table_name + "where ShopId = 26;"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    def insert(self, table_name, table_data):
        # 插入表数据
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    def close(self):
        # 关闭数据库连接
        self.connection.close()

    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()


if __name__ == '__main__':
    db = DB()
    table_name = ''
    data = {}
    db.clear(table_name)
    db.insert(table_name, data)
    db.close()

