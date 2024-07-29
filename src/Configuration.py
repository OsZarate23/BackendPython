import pymysql
from pymysql.cursors import DictCursor


class DevelopmentConfig:
    mysql = {
        'host': 'localhost',
        'user': 'root',
        'password': 'tacosychesco1',
        'db': 'dbsystem'
    }


def get_db_connection():
    db_config = DevelopmentConfig.mysql
    connection = pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        db=db_config['db'],
        charset='utf8mb4',
        cursorclass=DictCursor
    )
    return connection
