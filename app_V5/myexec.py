from get_db_manage import get_db
from op_db import conn_db
import re

def exec(user,s):
    try:
        user = re.findall(r"user=([\S|\s]*)", user, re.S | re.I)[0]
        db_manage = get_db('root', '123456', user)  # 获取数据库管理
        select_s = 'select max(id) from history_submit'
        now = conn_db(db_manage, select_s)
        now_id = now[0][0]
        if now_id is None:
            now_id=0
        insert_s = 'insert into history_submit values ' + '(' + str(now_id + 1) + ', "' + str(s) + '" );'
        db_manage = get_db('root', '123456', user)
        conn_db(db_manage, insert_s)
        db_manage = get_db(user, '123456', user+'ans')
        print('121212')
        now = conn_db(db_manage, s)
        print('121212')
        if 'create' in s:
            try:
                table_name = re.findall(r"table([\S|\s]*)as", s, re.S | re.I)[0].strip()
            except:
                try:
                    table_name=re.findall(r"table([\S|\s]*)\(",s, re.S | re.I)[0].strip()
                except:
                    table_name = re.findall(r"view([\S|\s]*)as", s, re.S | re.I)[0].strip()
            db_manage = get_db('root', '123456', user)  # 获取数据库管理
            print('121212')
            select_s = 'select max(id) from table_user_can_see'
            now = conn_db(db_manage, select_s)
            now_id = now[0][0]
            if now_id is None:
                now_id=0
            insert_s = 'insert into table_user_can_see values ' + '(' + str(now_id + 1) + ', "' + str(table_name) + '"'+',"'+user+'ans" );'
            print(insert_s)
            db_manage = get_db('root', '123456', user)  # 获取数据库管理
            conn_db(db_manage, insert_s)
        elif "drop" in s:
            try:
                table_name = re.findall(r"table([\S|\s]*)\(", s, re.S | re.I)[0].strip()
            except:
                table_name = re.findall(r"view([\S|\s]*)\(", s, re.S | re.I)[0].strip()
            delete_s = 'delete from table_user_can_see where name="'+table_name+'";'
            print(delete_s)
            db_manage = get_db('root', '123456', user)  # 获取数据库管理
            conn_db(db_manage, delete_s)
        return 1
    except:
        return 0



