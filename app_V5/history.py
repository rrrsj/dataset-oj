from get_db_manage import get_db
from op_db import conn_db
import re



def history(user,id):
    now_user = re.findall(r"user=([\S|\s]*)", user, re.S | re.I)[0]
    db_manage = get_db('root', '123456', now_user)
    s = 'SELECT history FROM ' + 'history_submit where id="' + str(id) + '"'
    now = conn_db(db_manage, s)
    ans={'text':now[0][0]}
    print(ans)
    return ans


#history('user=user1','0')