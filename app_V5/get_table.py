from get_db_manage import get_db
from op_db import conn_db
import re

def get_table(user,id):
    db_manage = get_db('root','123456',user)  # 获取数据库管理
    s = 'SELECT * FROM table_user_can_see'+' where id='+id+';'
    all=conn_db(db_manage,s) #执行操作
    s='SHOW COLUMNS from '+all[0][1]
    db_manage = get_db('root', '123456', all[0][2])
    now = conn_db(db_manage, s)
    title = []
    for i in now:
        linshi={'title':i[0]}
        title.append(linshi)
    s = 'select * from ' + all[0][1]
    print(s)
    db_manage = get_db('root', '123456', all[0][2])
    now = conn_db(db_manage, s)
    content=[]
    for i in now:
        linshi1=[]
        for t in i:
            linshi2={'content':t}
            linshi1.append(linshi2)
        content.append(linshi1)
    return title,content