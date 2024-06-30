from get_db_manage import get_db
from op_db import conn_db
import re


def check(user,id):
    try:
        user = re.findall(r"user=([\S|\s]*)", user, re.S | re.I)[0]
        db_manage = get_db('root', '123456', 'myshujuku')  # 获取数据库管理
        select_s = 'select ans_table from question where id='+str(id)+';'
        table_name = conn_db(db_manage, select_s)
        db_manage = get_db('root', '123456', 'myshujuku')  # 获取数据库管理
        select_s1 = 'select * from '+str(table_name[0][0])+';'
        table_content1 = conn_db(db_manage, select_s1)

        db_manage = get_db('root', '123456', user+'ans')  # 获取数据库管理
        select_s2 = 'select * from ' + str(table_name[0][0]) + ';'
        table_content2 = conn_db(db_manage, select_s2)
    except:
        table_content1='1'
        table_content2='2'

    if table_content1==table_content2:
        db_manage = get_db('root', '123456', user)  # 获取数据库管理
        select_s = 'select state from state where id=' +str(id)+ ';'
        state = conn_db(db_manage, select_s)
        if len(state)!=0:
            db_manage = get_db('root', '123456', user)  # 获取数据库管理
            update_s = 'update state set state=1 where id=' +str(id)+ ';'
            state = conn_db(db_manage, update_s)
        elif len(state)==0:
            db_manage = get_db('root', '123456', user)  # 获取数据库管理
            insert_s = 'insert into state values('+str(id)+', 1);'
            print(insert_s)
            state = conn_db(db_manage, insert_s)
        return 1
    else:
        db_manage = get_db('root', '123456', user)  # 获取数据库管理
        select_s = 'select state from state where id=' +str(id)+ ';'
        state = conn_db(db_manage, select_s)
        if len(state) != 0 and state[0][0]!=1:
            db_manage = get_db('root', '123456', user)  # 获取数据库管理
            updata_s = 'update state set state=2 where id=' +str(id)+ ';'
            state = conn_db(db_manage, updata_s)
        elif len(state) == 0:
            db_manage = get_db('root', '123456', user)  # 获取数据库管理
            insert_s = 'insert into state values(' + str(id) + ', 2);'
            state = conn_db(db_manage, insert_s)
        return 0

