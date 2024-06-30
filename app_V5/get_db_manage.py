import pymysql
import config


def get_db(user,passwd,db=config.db):
    conn = pymysql.connect(
        host=config.host,
        user=user,
        passwd=passwd,
        port=config.port,
        db=db,
        charset=config.charset
    )
    return conn
