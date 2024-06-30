from get_db_manage import get_db
from op_db import conn_db
import re

def get_question(page):
    page=int(page)
    db_manage = get_db('root','123456')  # 获取数据库管理
    if page is None or page < 0:
        page = 0
    l = str(page * 10 + 0)
    r = str(page * 10 + 9)
    s = 'SELECT * FROM question where id>=' + l + ' and id<=' + r + ' ORDER BY id;'
    now=conn_db(db_manage,s) #执行操作
    return now