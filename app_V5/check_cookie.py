from get_db_manage import get_db
from op_db import conn_db
import re

def check_cookie(user):
    db_manage = get_db('root','123456')  # 获取数据库管理
    now_user=re.findall(r"user=([\S|\s]*)",user, re.S|re.I)[0]
    print("当前cookie"+now_user)
    s='SELECT count(*) FROM user where user_name="'+str(now_user)+'"'
    now=conn_db(db_manage,s) #执行操作
    return now[0][0]