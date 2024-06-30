from flask import Flask, render_template, request, jsonify
import json
import re
import get_quesiton_state
from get_db_manage import get_db
from op_db import conn_db
import check_passwd
import check_cookie
import get_question
import get_quesiton_detail
import get_history
import get_table_detail
import get_table
import check
import myexec
import history
app = Flask(__name__)





@app.route("/log_in", methods=['GET'])   #登录页面
def log_in_html():
    return render_template("log.html")



@app.route("/check_user_passwd", methods=['POST']) #判断用户名和密码是否正确
def check_user_passwd():
    data = json.loads(request.get_data())
    state=check_passwd.check_passwd(data['account'],data['password'])
    return jsonify({"state":str(state)})


@app.route("/check_user_cookie",methods=['POST'])
def check_user_cookie():
    data = json.loads(request.get_data())
    try:
        state=check_cookie.check_cookie(data['cookie'])
    except:
        state=0
    return jsonify({"state": str(state)})





@app.route("/main", methods=['GET']) #问题列表
def main_html():
    page_number = request.args.get("p") #p是第几页 （p-1）*10---(p-1)*10+9
    print("page_number",page_number)
    if page_number is None:
        page_number = 0
    question=get_question.get_question(page_number)
    question_list=[]
    for i in question:
        linshi={'question_id':i[0],'state':0,'text':i[1]}
        question_list.append(linshi)#问题列表 问题的id，当前问题是否尝试了，问题题目
    hot_question_list = [{'question_id': 0, 'state': 0, 'text': '问题1'}]
    new_question_list = [{'question_id': 0, 'state': 0, 'text': '问题1'}]

    return render_template("main.html", question_list=question_list, hot_question_list=hot_question_list,
                           new_question_list=new_question_list)


@app.route("/get_state", methods=['POST']) #问题状态
def get_state():
    data = json.loads(request.get_data())  # 要执行的sql语句
    state=get_quesiton_state.get_question_state(data['question'],data['user'])
    return jsonify({"state": state})





@app.route("/answer", methods=['GET'])
def answer_html():
    question_id = request.args.get("question_id")
    now=get_quesiton_detail.get_question_detail(question_id)
    question = {'title': now[0][1], 'level':now[0][3], 'content': now[0][2]} #问题题目，难度，内容
    table_list=[{'table_id': 0, 'text': 'student'}]
    history_submit = [{'table_id': 0, 'text': 'student'}]
    return render_template("answer.html", question=question,table_list=table_list,history_submit=history_submit)


@app.route("/get_table_history", methods=['POST'])
def get_table_history():
    data = json.loads(request.get_data())
    #print(data)
    ans=get_history.get_question(data['user'])
    history=[]
    #print(ans)
    for i in ans:
        linshi={'id':i[0],'content':i[1]}
        history.append(linshi)
    ans = get_table_detail.get_table_detail(data['user'])
    #print(ans)
    table = []
    for i in ans:
        linshi = {'id': i[0], 'content': i[1],'database':i[2]}
        table.append(linshi)
    end_ans={'history':history,'table':table}
    return jsonify(end_ans)


@app.route("/form", methods=['GET'])
def form_html():
    form_id = request.args.get("form_id")
    user = request.args.get("user")
    print(form_id)
    print(user)
    title_list,line_list=get_table.get_table(user,form_id)
    return render_template("form.html",title_list=title_list,line_list=line_list)




@app.route("/check_question", methods=['POST'])
def check_question():
    data = json.loads(request.get_data())#要执行的sql语句
    print('提交语句',data)
    ans=myexec.exec(data['cookie'],data['submit'])
    return jsonify({"now": ans})


@app.route("/check_ans", methods=['POST'])
def check_ans():
    data = json.loads(request.get_data())#问题编号
    try:
        now=check.check(data['cookie'],data['id'])
    except:
        now=0
    return jsonify({"now": now})


@app.route("/get_history", methods=['POST'])
def get_submit_history():
    data = json.loads(request.get_data())
    ans=history.history(data['cookie'],data['id'])
    return jsonify(ans)



if __name__ == '__main__':
    app.run()
