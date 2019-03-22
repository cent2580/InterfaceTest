import sys
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

# 创建测试数据
datas = {

    # 标签数据
    'blogs_tag': [
        {'id': 1,
         'name': '小米',
         },
    ],

    # 分类数据
    'blogs_category': [

        {'id': 1,
         'name': '发布会',
         'category_order': 0},
    ],

    # 文章数据
    'blogs_article': [
        {'id': 1, 'title': '小米', 'content': '小米发布会',
         'image': 'article_image/2019/0314/pexels-photo-872795_rXvSARo.jpeg',
         'views': 10,
         'add_time': '2016-08-20 00:25:42',
         'update_time': '2016-08-20 00:25:42',
         'category_id': 1,
         'user_id': 1},
    ],

}


# 将测试数据插入表
def init_data():
    DB().init_data(datas)


if __name__ == '__main__':
    init_data()
