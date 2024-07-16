#회원가입 하기
import pymysql
from tkinter import messagebox as m

#사용자에게 인풋을 받아서 받은 인풋을 db 고객 테이블에 맞게 추가
# 1. 인풋 받기
# 2. 받은 인풋을 변수로 INSERT 함수로 고객 테이블에 추가
# 회원가입 시 필요한 변수 = id,password,성별,주소,우편번호,전화번호,휴대폰
def SignIn(id, pw, sex, address, addNum, call, phone):
    conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='상품판매db', charset='utf8')
    cur = conn.cursor()

    sqlSelectCostumerTable = 'select id from 고객'

    cur.execute(sqlSelectCostumerTable)
    result = cur.fetchall()
    if (id,) not in result:
        if call == "":
            call = None
        data = (id, pw, sex, address, addNum, call, phone)

        sqlIntoTable = "INSERT INTO 고객(id, password, 성별, 주소, 우편번호, 전화번호, 휴대폰) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(sqlIntoTable, data)
    else:
        m.showwarning("시스템 알림", "동일한 ID는 사용할 수 없습니다.")

    conn.commit()
    conn.close()


