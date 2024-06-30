from get_db_manage import get_db
from op_db import conn_db
import re

def get_question_detail(id):
    db_manage = get_db('root','123456')  # 获取数据库管理
    s = 'SELECT * FROM question where id='+id+ ';'
    now=conn_db(db_manage,s) #执行操作
    return now