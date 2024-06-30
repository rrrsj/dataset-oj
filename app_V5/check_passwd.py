from get_db_manage import get_db
from op_db import conn_db


def check_passwd(user,passwd):
    try:
        db_manage = get_db('root','123456')  # 获取数据库管理
        s='SELECT passwd FROM user where user_name="'+str(user)+'"'
        now=conn_db(db_manage,s) #执行操作
        if passwd==now[0][0]:
            return 1
        else:
            return 0
    except:
        return 0