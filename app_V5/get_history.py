from get_db_manage import get_db
from op_db import conn_db
import re


def get_question(user):
    now_user = re.findall(r"user=([\S|\s]*)", user, re.S | re.I)[0]
    db_manage = get_db('root', '123456', now_user)  # 获取数据库管理
    s = 'SELECT * FROM history_submit;'
    now = conn_db(db_manage, s)  # 执行操作
    print(now)
    return now
