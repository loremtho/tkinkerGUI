#관리자, 사용자 메뉴
import pymysql
import pandas as pd
import tkinter as tk
from tkinter import messagebox as m
from datetime import datetime as d

now = d.now()
nowTime = now.strftime('%Y-%m-%d %H:%M:%S')
#메뉴 기능 만들기

#@관리자 메뉴
#상품 삽입, 변경, 삭제
#내역 리스트 출력 (날짜, 사용자, 상품명, 단가, 개수, 금액)

#상품 삽입
def AdminFuction_Insert(Item_Name, Item_SellPrice, Item_BuyPrice):
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='상품판매db', charset='utf8')
        cur = conn.cursor()
        # 1. 상품 삽입
        # Item_Name = input("상품의 이름을 입력하세요 : ")
        # Item_SellPrice = input("상품의 판매가를 입력하세요 : ")
        # Item_BuyPrice = input("상품의 구매가를 입력하세요 : ")
        if Item_Name and Item_SellPrice and Item_BuyPrice:
            ItemData = (Item_Name, Item_SellPrice, Item_BuyPrice)

            CheckItemInTable = "SELECT 상품명 FROM 상품 WHERE 상품명 = %s"
            cur.execute(CheckItemInTable, (Item_Name,))
            res = cur.fetchone()
            if res:
                m.showwarning("시스템 알림", "테이블에 동일한 상품이 있습니다.")
            else:
                IntoItemTable = "INSERT INTO 상품(상품명, 판매가, 구매가) VALUES(%s, %s, %s)"
                cur.execute(IntoItemTable, ItemData)

                CurrentItemTable = "SELECT 상품번호,상품명,판매가,구매가 FROM 상품"
                cur.execute(CurrentItemTable)
                res2 = cur.fetchall()
                pdres = pd.DataFrame(res2, columns=['상품번호', '상품명', '판매가', '구매가'])
                print(pdres)
        else:
            m.showwarning("시스템 알림", "삽입할 정보를 입력해주세요.")

        conn.commit()
    except pymysql.Error as e:
        m.showerror("Database Error", f"Database Error: {str(e)}")
    finally:
        if 'conn' in locals():
            conn.close()

    return res2

#상품 삭제
def AdminFuction_Delete(Item_Name):
    conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='상품판매db', charset='utf8')
    cur = conn.cursor()
    # 2. 상품 제거
    while True:
        if Item_Name:
            IsExistItem = "SELECT 상품번호,상품명,판매가,구매가 FROM 상품 WHERE 상품명 = %s"
            cur.execute(IsExistItem, (Item_Name,))
            res = cur.fetchall()
            if res:
                response = m.askquestion("시스템 알림", "삭제하시겠습니까?")
                if response == "yes":
                    DeleteItem = "DELETE FROM 상품 WHERE 상품명 = %s"
                    cur.execute(DeleteItem, (Item_Name,))
                    m.showinfo("시스템 알림", f"{Item_Name}(가)이 삭제되었습니다.")
                    print(f"{Item_Name} 이 삭제되었습니다.")
                elif response == "no":
                    m.showinfo("시스템 알림", f"{Item_Name} 삭제를 취소했습니다.")
                    print(f"{Item_Name} 삭제를 취소했습니다.")
                break
            else:
                m.showwarning("시스템 알림", "해당하는 상품 정보가 없습니다. 다시 검색하세요.")
                print("해당하는 상품 정보가 없습니다. 다시 검색하세요.")

    conn.commit()
    conn.close()
#상품 변경
def AdminFuction_Update(UpdateP_Name, UpdateP_Sell, UpdateP_Buy):
    conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='상품판매db', charset='utf8')
    cur = conn.cursor()
    while True:
        # 이후 변경할 품목의 이름을 받아 상품의 속성 변경
        ## 판매가 입력 x , 구매가만 입력할 경우
        if UpdateP_Sell == "" and UpdateP_Buy:
            UpdateItemColumn = "UPDATE 상품 SET 구매가 = %s WHERE 상품명 = %s "
            cur.execute(UpdateItemColumn, (UpdateP_Buy, UpdateP_Name))
            m.showinfo("시스템 알림", f"{UpdateP_Name}의 구매가가 변경되었습니다.")
            print(f"@{UpdateP_Name}의 구매가가 변경되었습니다. ")
            break
        ## 판매가와 구매가 모두 입력할 경우
        elif UpdateP_Sell and UpdateP_Buy:
            UpdateItemColumn = "UPDATE 상품 SET 판매가 = %s, 구매가 = %s WHERE 상품명 = %s "
            cur.execute(UpdateItemColumn, (UpdateP_Sell, UpdateP_Buy, UpdateP_Name))
            m.showinfo("시스템 알림", f"{UpdateP_Name}의 판매가와 구매가가 변경되었습니다.")
            print(f"@{UpdateP_Name}의 판매가와 구매가가 변경되었습니다. ")
            break
        ## 판매가만 입력, 구매가 입력 x 일 경우
        elif UpdateP_Sell and UpdateP_Buy == "":
            UpdateItemColumn = "UPDATE 상품 SET 판매가 = %s WHERE 상품명 = %s "
            cur.execute(UpdateItemColumn, (UpdateP_Sell, UpdateP_Name))
            m.showinfo("시스템 알림", f"{UpdateP_Name}의 판매가가 변경되었습니다.")
            print(f"@{UpdateP_Name}의 판매가가 변경되었습니다. ")
            break
        else:
            m.showinfo("시스템 알림", "변경할 정보를 입력하지 않았습니다.")
            print("변경할 정보를 입력하지 않았습니다.")
            break

    conn.commit()
    conn.close()
#유저들 구매내역 리스트 출력
def AdminFuction_TableSelect():
    conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='상품판매db', charset='utf8')
    cur = conn.cursor()

    #날짜, 사용자, 상품명, 단가, 개수, 금액
    TablePrint = \
        ("SELECT 판매날짜, id, 상품명, 판매가, 수량 , 수량*판매가 "
         "FROM 고객, 상품, 판매, 판매상세 "
         "WHERE 고객.고객번호 = 판매.고객번호 "
         "AND 판매.판매번호 = 판매상세.판매번호 "
         "AND 판매상세.상품번호 = 상품.상품번호")

    cur.execute(TablePrint)
    res = cur.fetchall()

    # pdres = pd.DataFrame(res, columns=['날짜', '구매자명', '상품명', '판매가', '갯수', '총액'])
    # print("{0:=^45}".format("사용자들의 구매내역 리스트"))
    # print(pdres)
    # print("=" * 50)

    conn.commit()
    conn.close()

    return res

#상품 리스트 출력
def AdminFuction_TablePrint():
    conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='상품판매db', charset='utf8')
    cur = conn.cursor()

    # 1.상품 리스트 출력
    table = 'SELECT  상품번호, 상품명, 판매가, 구매가 FROM 상품'
    cur.execute(table)
    res = cur.fetchall()

    return res

#@사용자 메뉴
#자기 구매 내역 리스트 출력
#구매하기 => 상품명, 개수 입력, 현재 시스템 날짜를 구매 테이블과 구매상세 테이블에 추가
#구매는 날짜와 사용자 번호 삽입
#구매상세는 판매번호, 상품번호, 개수 삽입

#구매내역 리스트 출력
def UserFuction_PurchaseList(user_name):
    conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='상품판매db', charset='utf8')
    cur = conn.cursor()

    TablePrint = (
        "SELECT 판매.판매날짜 AS 구매날짜, 고객.id, 상품.상품명, 상품.판매가, 판매상세.수량, 판매상세.수량 * 상품.판매가 AS 총액 "
        "FROM 고객 "
        "JOIN 판매 ON 고객.고객번호 = 판매.고객번호 "
        "JOIN 판매상세 ON 판매.판매번호 = 판매상세.판매번호 "
        "JOIN 상품 ON 판매상세.상품번호 = 상품.상품번호 "
        "WHERE 고객.id = %s"
    )

    cur.execute(TablePrint, (user_name,))
    res = cur.fetchall()

    conn.commit()
    conn.close()

    return res
#현재 상품 목록 띄워주기
def UserFuction_ItemList():
    conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='상품판매db', charset='utf8')
    cur = conn.cursor()

    #1.상품 리스트 출력
    table = 'SELECT  상품번호, 상품명, 판매가 FROM 상품'
    cur.execute(table)
    res = cur.fetchall()

    return res
    # pdres = pd.DataFrame(res, columns=['상품번호', '상품명', '가격'])
    # print("{0:=^45}".format("상품 리스트"))
    # print(pdres)
    # print("=" * 50)
# 구매하기
def UserFuction_Purchase(requiredItem_Name, requiredItems_Entity, user_num):
    conn = pymysql.connect(host='localhost', user='root', passwd='1234', db='상품판매db', charset='utf8')
    cur = conn.cursor()
    #----2.원하는 상품 이름과 개수 인풋으로 받기----
    selectItemNum = 'SELECT 상품번호 FROM 상품 WHERE 상품명 = %s'
    cur.execute(selectItemNum, (requiredItem_Name,))
    res = cur.fetchone()
    #conn.commit()
    requiredItems_Num = res[0]

    #----3.받은 정보를 판매와 판매상세 테이블에 추가----
    ## 판매 테이블에는 현재 시스템 날짜를 판매날짜로 추가하고 현재 고객번호 삽입
    costomerInfoData = (nowTime, user_num)
    sellTable = 'INSERT INTO 판매(판매날짜, 고객번호) VALUES (%s, %s)'
    cur.execute(sellTable, costomerInfoData)
    #conn.commit()
    ## 판매 테이블에 존재하는 판매번호를 받아오기
    sellDetailTable = 'SELECT 판매번호 FROM 판매 WHERE 판매날짜 = %s AND 고객번호 = %s'
    cur.execute(sellDetailTable, (nowTime, user_num))
    res = cur.fetchone()
    #conn.commit()
    ## 판매상세의 새로운 행에 받아온 모든 정보 넣어주기 ( 판매번호, 상품번호, 수량 )
    requiredtuple = (res[0], requiredItems_Num, requiredItems_Entity)
    sellTable = 'INSERT INTO 판매상세(판매번호, 상품번호, 수량) VALUES (%s, %s, %s)'
    cur.execute(sellTable, requiredtuple)

    conn.commit()
    conn.close()
