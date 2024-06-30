from get_db_manage import get_db
from op_db import conn_db
import re

def get_question_state(question_id,user):
    now_user = re.findall(r"user=([\S|\s]*)", user, re.S | re.I)[0]
    state=[]
    print('question_id',question_id)
    for i in question_id:
        db_manage = get_db('root','123456',now_user)
        s = 'SELECT state FROM '+'state where id=' + str(i) + ';'
        now = conn_db(db_manage, s)
        try:
            state.append(now[0][0])
        except:
            state.append('0')
    return state