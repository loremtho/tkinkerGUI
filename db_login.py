#로그인 하기
import pymysql
import pandas as pd
from tkinter import *
from tkinter import messagebox

# 로그인하기
# 사용자에게 인풋을 받아서 현재 db에 존재하는지 확인
# if 존재한다면 로그인 성공
#   if 해당 id 의 고객의 "구분" 문자열이 = 관리자라면
#       관리자 메뉴 출력
#   else = 사용자라면
#       사용자 메뉴 출력

def login(id,pw):
    conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='상품판매db', charset='utf8')
    cur = conn.cursor()
    # Input_ID = input("아이디를 입력하세요 : ")
    # Input_PW = input("비밀번호를 입력하세요 : ")
    user_ID = id #entry_ID.get()
    user_PW = pw #entry_PW.get()
    checkID = "SELECT id, password, 고객번호, 구분 FROM 고객 WHERE id = %s"  # 테이블에서 id 가져오기
    cur.execute(checkID, (user_ID,))
    res = cur.fetchone()

    conn.close()

    return res

    # if res:
    #     db_id, db_pw, db_userNum, db_acc = res
    #     if db_pw == user_PW:
    #         print("@로그인 성공")
    #         if db_acc == "관리자":
    #             # 관리자 메뉴 출력
    #             print("@관리자 메뉴 출력")
    #             AdminMenu()
    #             print("사용자 번호 : {0} || 사용자 이름 : {1}".format(db_userNum, db_id))
    #         else:
    #             # 사용자 메뉴 출력
    #             print("@사용자 메뉴 출력")
    #             UserMenu()
    #             print("사용자 번호 : {0} || 사용자 이름 : {1}".format(db_userNum, db_id))
    # else:
    #     print("로그인 실패")

def AdminMenu():
    print("=" * 35)
    print("{0:^31}".format("관리자메뉴"))
    print("-" * 35)
    print("{0:<31}".format("1. 상품 삽입\n2. 상품 변경\n3. 상품 삭제\n4. 내역리스트 출력"))
    print("=" * 35)

def UserMenu():
    print("=" * 35)
    print("{0:^31}".format("사용자메뉴"))
    print("-" * 35)
    print("{0:<31}".format("1. 구매\n2. 구매 내역 출력"))
    print("=" * 35)

def login_Component(type):

    if type == 0:
        # 사용자 이름 라벨 및 입력 필드
        label_username.pack()
        entry_ID.pack()

        # 비밀번호 라벨 및 입력 필드
        label_password.pack()
        entry_PW.pack()

        # 로그인 버튼
        login_button.pack()

        # # 사용자 이름 라벨 및 입력 필드
        #
        # label_username.grid(row=0, column=0, padx=10, pady=10)
        # entry_ID = Entry(w)
        # entry_ID.grid(row=0, column=1, padx=10, pady=10)
        #
        # # 비밀번호 라벨 및 입력 필드
        # label_password = Label(w, text="Password")
        # label_password.grid(row=1, column=0, padx=10, pady=10)
        # entry_PW = Entry(w, show="*")
        # entry_PW.grid(row=1, column=1, padx=10, pady=10)
        #
        # # 로그인 버튼
        # login_button = Button(w, text="Login", command=login)
        # login_button.grid(row=2, column=0, columnspan=2, pady=10)
    elif type == 1:
        label_username.pack_forget()
        entry_ID.pack_forget()
        label_password.pack_forget()
        entry_PW.pack_forget()
        login_button.pack_forget()

def login_window(w):
    w.title("Login")

    global label_username
    label_username = Label(w, text="ID")

    global entry_ID
    entry_ID = Entry(w)

    global label_password
    label_password = Label(w, text="Password")

    global entry_PW
    entry_PW = Entry(w, show="*")

    global login_button
    login_button = Button(w, text="Login", command=login)

    login_Component(0)

    w.mainloop()




