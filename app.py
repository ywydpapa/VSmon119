import json
from flask import Flask, request, render_template, make_response
from time import time, localtime
import pymysql

db = None
cur = None
app = Flask(__name__)

def select(query):
  # 접속정보
  db = pymysql.connect(host='192.168.108.25', user='swcore', password='core2020', db='vs119f', charset='utf8')
  # 커서생성
  cur = db.cursor()
  # 실행할 sql문
  cur.execute(query)
  result = cur.fetchall()
  db.close() # 종료
  return result

@app.route('/')
def home():  # put application's code here
    sql="select * from vsUser"
    result = select(sql)
    return render_template("home.html", result=result)

@app.route('/map')
def map():
    sql="select * from vsUser"
    result = select(sql)
    return render_template("mainMap.html", result=result)

@app.route('/login')
def login():
    sql="select * from vsUser"
    result = select(sql)
    return render_template("login.html", result=result)


if __name__ == '__main__':
    app.run(debug=True, port=80,host='0.0.0.0')
