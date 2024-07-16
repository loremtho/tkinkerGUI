import tkinter as tk
from tkinter import ttk, simpledialog
from tkinter import messagebox as m
import db_login as login
import db_Signin as sign
import db_MenuFuction as menu

w = tk.Tk()
w.geometry("1000x800")


#로그인 화면에 필요한 tkinter 싹 다
def login_func():
    global user_id
    user_id = entry_id.get()
    user_pw = entry_pw.get()

    res = login.login(user_id, user_pw)
    if res:
        global db_userNum
        db_id, db_pw, db_userNum, db_acc = res
        if db_pw == user_pw:
            print("@로그인 성공")
            m.showinfo("시스템 알림", "@로그인 성공")
            if db_acc == "관리자":
                m.showinfo("관리자 권한", f"사용자 ID :{db_id},"
                                     f"사용자 {db_userNum},{db_acc}")
                #관리자 메뉴 출력
                Clear_window()
                admin_print()
            else:
                m.showinfo("사용자", f"사용자 ID :{db_id},"
                                  f"{db_userNum},{db_acc}")
                Clear_window()
                user_print()
                #사용자 메뉴 출력
    else:
        m.showwarning("시스템 알림", "@로그인 실패")

def login_print():
    w.title("로그인")
    Clear_window()
    login_frame = tk.Frame(w)
    login_frame.pack(fill="both", expand=True)
    label_userid = tk.Label(login_frame, text="ID")
    label_userid.place(x=500, y=200)
    global entry_id
    entry_id = tk.Entry(login_frame)
    # 관리자
    entry_id.insert(0, "둘리")
    # 도우너
    #entry_id.insert(0,"도우너")
    entry_id.place(x=600, y=220)
    label_userpw = tk.Label(login_frame, text="PW")
    label_userpw.place(x=500, y=300)
    global entry_pw
    entry_pw = tk.Entry(login_frame, show="*")
    entry_pw.insert(0, "1234")
    entry_pw.place(x=600, y=320)

    signin_btn = tk.Button(login_frame, text="회원가입", command=signin_print)
    signin_btn.place(x=550, y=400)

    login_button = tk.Button(login_frame, text="로그인", command=login_func)
    login_button.place(x=650, y=400)

    login_frame.mainloop()

def signin_print():
    w.title("회원가입")
    Clear_window()
    signin_frame = tk.Frame(w)
    signin_frame.pack(fill="both", expand=True)
    # 아이디
    label_userid = tk.Label(signin_frame, text="ID")
    label_userid.pack(padx=50, pady=10, side="top")
    global sign_entry_id
    sign_entry_id = tk.Entry(signin_frame)
    sign_entry_id.pack(padx=50, pady=10, side="top")
    # 비번
    label_userpw = tk.Label(signin_frame, text="PW")
    label_userpw.pack(padx=50, pady=10, side="top")
    global sign_entry_pw
    sign_entry_pw = tk.Entry(signin_frame)
    sign_entry_pw.pack(padx=50, pady=10, side="top")
    # 성별
    label_usersex = tk.Label(signin_frame, text="성별")
    label_usersex.pack(padx=50, pady=10, side="top")
    global sign_entry_usersex
    sign_entry_usersex = tk.Entry(signin_frame)
    sign_entry_usersex.pack(padx=50, pady=10, side="top")
    # 주소
    label_userAdress = tk.Label(signin_frame, text="주소")
    label_userAdress.pack(padx=50, pady=10, side="top")
    global sign_entry_address
    sign_entry_address = tk.Entry(signin_frame)
    sign_entry_address.pack(padx=50, pady=10, side="top")
    # 우편번호
    label_userAdressNum = tk.Label(signin_frame, text="우편번호")
    label_userAdressNum.pack(padx=50, pady=10, side="top")
    global sign_entry_addressNum
    sign_entry_addressNum = tk.Entry(signin_frame)
    sign_entry_addressNum.pack(padx=50, pady=10, side="top")
    # 전화번호
    label_userCallNum = tk.Label(signin_frame, text="전화번호")
    label_userCallNum.pack(padx=50, pady=10, side="top")
    global sign_entry_CallNum
    sign_entry_CallNum = tk.Entry(signin_frame)
    sign_entry_CallNum.pack(padx=50, pady=10, side="top")
    # 휴대폰
    label_userPhoneNum = tk.Label(signin_frame, text="휴대폰")
    label_userPhoneNum.pack(padx=50, pady=10, side="top")
    global sign_entry_PhoneNum
    sign_entry_PhoneNum = tk.Entry(signin_frame)
    sign_entry_PhoneNum.pack(padx=50, pady=10, side="top")

    sigiin_btn = tk.Button(signin_frame, text="회원가입하기", command=lambda :
                            signin_func(sign_entry_id, sign_entry_pw, sign_entry_usersex,
                                        sign_entry_address, sign_entry_addressNum, sign_entry_CallNum,
                                        sign_entry_PhoneNum))
    sigiin_btn.pack(padx=60, pady=20, side="top")


    signin_frame.mainloop()

def signin_func(id, pw, sex, adress, addNum, call, phone):
    sign.SignIn(id.get(), pw.get(), sex.get(), adress.get(), addNum.get(), call.get(), phone.get())
    m.showinfo("시스템 알림", "회원가입이 완료되었습니다.")
    login_print()



# 위젯 숨기기 함수
def Clear_window():
    for widget in w.winfo_children():
        widget.pack_forget()


# => 관리자 섹션
#===================================================
# 삽입 함수
def admin_Insert_func(entry_ItemName, entry_ItemSellPrice, entry_ItemBuyPrice):
    menu.AdminFuction_Insert(entry_ItemName.get(), entry_ItemSellPrice.get()
                             , entry_ItemBuyPrice.get())
    m.showinfo("시스템알림", f"{entry_ItemName.get()}이(가) 등록되었습니다.")
    Clear_window()
    admin_Insert_print()
# 관리자 삽입
def admin_Insert_print():
    w.title("상품 삽입 창")
    Clear_window()
    admin_Insert_frame = tk.Frame(width=1000, height=400)
    admin_Insert_frame.pack(fill="both", expand=True, side="bottom")

    label_ItemName = tk.Label(admin_Insert_frame, text="삽입할 상품 이름")
    label_ItemName.place(x=350, y=100)
    entry_ItemName = tk.Entry(admin_Insert_frame)
    entry_ItemName.place(x=500, y=100)
    label_ItemSellPrice = tk.Label(admin_Insert_frame, text="삽입할 상품 판매가")
    label_ItemSellPrice.place(x=350, y=150)
    entry_ItemSellPrice = tk.Entry(admin_Insert_frame)
    entry_ItemSellPrice.place(x=500, y=150)
    label_ItemBuyPrice = tk.Label(admin_Insert_frame, text="삽입할 상품 구매가")
    label_ItemBuyPrice.place(x=350, y=200)
    entry_ItemBuyPrice = tk.Entry(admin_Insert_frame)
    entry_ItemBuyPrice.place(x=500, y=200)

    insert_btn = tk.Button(admin_Insert_frame, text="상품 삽입하기", command=lambda :admin_Insert_func(entry_ItemName, entry_ItemSellPrice, entry_ItemBuyPrice))
    insert_btn.place(x=400, y=250, width=200, height=50)

    back_btn = tk.Button(admin_Insert_frame, text="뒤로 가기", command=admin_print)
    back_btn.place(x=50, y=400, width=200, height=50)

    admin_Insert_frame.pack(fill="both", expand=True)

    admin_InsertList_frame = tk.Frame(width=1000, height=400)
    admin_InsertList_frame.pack(fill="both", expand=True, side="top")

    res = menu.AdminFuction_TablePrint()

    columns = ('상품번호', '상품명', '판매가', '구매가')
    tree = ttk.Treeview(admin_InsertList_frame, columns=columns, show='headings', height=len(res))

    col_widths = {'상품번호': 100, '상품명': 100, '판매가': 100, '구매가': 100}
    for col in columns:
        tree.column(col, width=col_widths[col])
        tree.heading(col, text=col)

    tree.pack(fill="x", expand=True, anchor="n")
    admin_InsertList_frame.rowconfigure(0, weight=1)  # row 0을 윈도우 크기에 맞춤

    create_treeview(tree, res)

    admin_Insert_frame.mainloop()

# 관리자 삭제
def admin_Delete_print():
    w.title("상품 제거 창")
    Clear_window()

    admin_DeleteList_frame = tk.Frame(width=1000, height=600)
    admin_DeleteList_frame.pack(fill="both", expand=True, side="top")

    res = menu.AdminFuction_TablePrint()

    columns = ('상품번호', '상품명', '판매가', '구매가')
    global deletetree
    deletetree = ttk.Treeview(admin_DeleteList_frame, columns=columns, show='headings', height=len(res))

    col_widths = {'상품번호': 100, '상품명': 100, '판매가': 100, '구매가': 100}
    for col in columns:
        deletetree.column(col, width=col_widths[col])
        deletetree.heading(col, text=col)

    deletetree.pack(fill="x", expand=True, anchor="n")
    admin_DeleteList_frame.rowconfigure(0, weight=1)  # row 0을 윈도우 크기에 맞춤

    create_treeview(deletetree, res)

    deletetree.bind("<<TreeviewSelect>>", admin_Delete_func)

    admin_Delete_frame = tk.Frame(width=1000, height=200)
    admin_Delete_frame.pack(fill="both", expand=True, side="bottom")

    back_btn = tk.Button(admin_Delete_frame, text="뒤로 가기", command=admin_print)
    back_btn.place(x=370, y=150, width=200, height=50)
    admin_Delete_frame.mainloop()

def admin_Delete_func(event):
    selected_item = deletetree.selection()
    item_values = deletetree.item(selected_item[0], "values")
    menu.AdminFuction_Delete(item_values[1])
    Clear_window()
    admin_Delete_print()

# 관리자 변경
def admin_Update_print():
    w.title("상품 변경 창")
    Clear_window()
    admin_Update_frame = tk.Frame(width=1000, height=400)
    admin_Update_frame.pack(fill="both", expand=True, side="bottom")
    label_ItemName = tk.Label(admin_Update_frame, text="변경할 상품명")
    label_ItemName.place(x=350, y=50)
    entry_ItemName = tk.Entry(admin_Update_frame)
    entry_ItemName.place(x=450, y=50)
    label_ItemSellPrice = tk.Label(admin_Update_frame, text="적용할 판매가")
    label_ItemSellPrice.place(x=350, y=100)
    entry_ItemSellPrice = tk.Entry(admin_Update_frame)
    entry_ItemSellPrice.place(x=450, y=100)
    label_ItemBuyPrice = tk.Label(admin_Update_frame, text="적용할 구매가")
    label_ItemBuyPrice.place(x=350, y=150)
    entry_ItemBuyPrice = tk.Entry(admin_Update_frame)
    entry_ItemBuyPrice.place(x=450, y=150)

    update_btn = tk.Button(admin_Update_frame, text="상품 정보 변경하기", command=lambda: admin_Update_func(entry_ItemName,
                                                                                                  entry_ItemSellPrice,
                                                                                                  entry_ItemBuyPrice))
    update_btn.place(x=370, y=200, width=200, height=50)

    back_btn = tk.Button(admin_Update_frame, text="뒤로 가기", command=admin_print)
    back_btn.place(x=50, y=400, width=200, height=50)


    admin_UpdateList_frame = tk.Frame(width=1000, height=400)
    admin_UpdateList_frame.pack(fill="both", expand=True, side="top")

    res = menu.AdminFuction_TablePrint()

    columns = ('상품번호', '상품명', '판매가', '구매가')
    tree = ttk.Treeview(admin_UpdateList_frame, columns=columns, show='headings', height=len(res))

    col_widths = {'상품번호': 100, '상품명': 100, '판매가': 100, '구매가': 100}
    for col in columns:
        tree.column(col, width=col_widths[col])
        tree.heading(col, text=col)

    tree.pack(fill="x", expand=True, anchor="n")
    admin_UpdateList_frame.rowconfigure(0, weight=1)  # row 0을 윈도우 크기에 맞춤

    create_treeview(tree, res)

    admin_Update_frame.mainloop()
# 변경 함수
def admin_Update_func(entry_ItemName, entry_ItemSellPrice, entry_ItemBuyPrice):
    menu.AdminFuction_Update(entry_ItemName.get(), entry_ItemSellPrice.get(),
                             entry_ItemBuyPrice.get())
    Clear_window()
    admin_Update_print()


# 관리자 리스트 출력
def admin_TableList_print():
    w.title("구매내역 창")
    Clear_window()

    # Frame 생성 및 배치
    admin_TableList_frame = tk.Frame(w)
    admin_TableList_frame.pack(fill="both", expand=True)

    res = menu.AdminFuction_TableSelect()

    # Treeview 생성
    columns = ('판매날짜', 'id', '상품명', '판매가', '수량', '총액')
    tree = ttk.Treeview(admin_TableList_frame, columns=columns, show='headings', height=len(res))

    # 컬럼 설정
    col_widths = {'판매날짜': 200, 'id': 100, '상품명': 100, '판매가': 100, '수량': 50, '총액': 100}
    for col in columns:
        tree.column(col, width=col_widths[col])
        tree.heading(col, text=col.replace('id', '구매자명'))

    tree.pack(fill="x", expand=True, anchor="n")
    admin_TableList_frame.rowconfigure(0, weight=1)  # row 0을 윈도우 크기에 맞춤

    back_btn = tk.Button(admin_TableList_frame, text="뒤로 가기", command=admin_print)
    back_btn.place(x=50, y=650, width=200, height=50)

    create_treeview(tree, res)

    admin_TableList_frame.mainloop()

# 관리자 메뉴
def admin_print():
    w.title("관리자 메뉴")
    Clear_window()
    admin_frame = tk.Frame(w)
    admin_frame.pack(fill="both", expand=True)

    admin_insert_btn = tk.Button(admin_frame, text="상품 삽입",
                                 padx=5, pady=5,
                                 font=("맑은 고딕", 15, "bold"),
                                 command=admin_Insert_print)
    admin_insert_btn.place(x=200, y=200, width=200, height=70)

    admin_update_btn = tk.Button(admin_frame, text="상품 변경",
                                 padx=5, pady=5,
                                 font=("맑은 고딕", 15, "bold"),
                                 command=admin_Update_print)
    admin_update_btn.place(x=600, y=200, width=200, height=70)

    admin_delete_btn = tk.Button(admin_frame, text="상품 제거",
                                 padx=5, pady=5,
                                 font=("맑은 고딕", 15, "bold"),
                                 command=admin_Delete_print)
    admin_delete_btn.place(x=200, y=400, width=200, height=70)

    admin_tableSelect_btn = tk.Button(admin_frame, text="상품 리스트 출력",
                                      padx=5, pady=5,
                                      font=("맑은 고딕", 15, "bold"),
                                      command=admin_TableList_print)
    admin_tableSelect_btn.place(x=600, y=400, width=200, height=70)

    admin_frame.mainloop()
#===================================================

# 트리뷰 데이터 초기화 & 삽입
def create_treeview(tree, res):
    # 트리뷰 모든 행 삭제 => 초기화
    for item in tree.get_children():
        tree.delete(item)
    # 데이터 삽입
    for row in res:
        tree.insert('', 'end', values=row)

# => 사용자 섹션
#---------------------------------------------------

def user_print():
    w.title("사용자 메뉴")
    Clear_window()
    user_frame = tk.Frame(w)
    user_frame.pack(fill="both", expand=True)

    user_purchaseList_btn = tk.Button(user_frame, text="구매 내역 보기",
                                 padx=5, pady=5,
                                 font=("맑은 고딕", 15, "bold"),
                                 command=user_TableList_print)
    user_purchaseList_btn.place(x=400, y=300, width=200, height=70)

    user_purchase_btn = tk.Button(user_frame, text="상품 구매하기",
                                 padx=5, pady=5,
                                 font=("맑은 고딕", 15, "bold"),
                                 command=user_Purchase_print)
    user_purchase_btn.place(x=400, y=400, width=200, height=70)

    user_frame.mainloop()

def user_TableList_print():
    w.title("구매내역 창")
    Clear_window()

    # Frame 생성 및 배치
    user_TableList_frame = tk.Frame(w)
    user_TableList_frame.pack(fill="both", expand=True)

    # 구매 내역 데이터 가져오기
    res = menu.UserFuction_PurchaseList(user_id)

    # Treeview 생성
    columns = ('판매날짜', 'id', '상품명', '판매가', '수량', '총액')
    tree = ttk.Treeview(user_TableList_frame, columns=columns, show='headings', height=len(res))

    # 컬럼 설정
    col_widths = {'판매날짜': 200, 'id': 100, '상품명': 100, '판매가': 100, '수량': 50, '총액': 100}
    for col in columns:
        tree.column(col, width=col_widths[col])
        tree.heading(col, text=col.replace('판매', '구매').replace('id', '구매자명'))

    tree.pack(fill="x", expand=True, anchor="n")
    user_TableList_frame.rowconfigure(0, weight=1)  # row 0을 윈도우 크기에 맞춤

    if res:
        create_treeview(tree, res)
    else:
        m.showwarning("시스템 알림", "구매 내역이 없습니다.")
        user_print()

    back_btn = tk.Button(user_TableList_frame, text="뒤로 가기", padx=20, pady=15, command=user_print)
    back_btn.pack(padx=20, pady=15, expand=True, side="bottom")

    user_TableList_frame.mainloop()

def user_Purchase_print():
    w.title("상품 구매하기 창")
    Clear_window()
    user_PurchaseList_frame = tk.Frame(width=1200, height=400)
    user_PurchaseList_frame.pack(fill="both", expand=True, side="top")

    res = menu.UserFuction_ItemList()

    columns = ('상품번호', '상품명', '판매가')
    global tree
    tree = ttk.Treeview(user_PurchaseList_frame, columns=columns, show='headings', height=len(res))

    col_widths = {'상품번호': 100, '상품명': 100, '판매가': 100}
    for col in columns:
        tree.column(col, width=col_widths[col])
        tree.heading(col, text=col)

    tree.pack(fill="x", expand=True, anchor="n")
    user_PurchaseList_frame.rowconfigure(0, weight=1)  # row 0을 윈도우 크기에 맞춤

    create_treeview(tree, res)

    # => 상품 선택과 구매하기 버튼 있는 프레임 ------------------------------------
    user_Purchase_frame = tk.Frame(width=1200, height=400)
    user_Purchase_frame.pack(fill="both", expand=True, side="bottom")

    columns2 = ('상품번호', '상품명', '판매가', '갯수', '총액')
    global tree2
    tree2 = ttk.Treeview(user_Purchase_frame, columns=columns2, show='headings', selectmode='extended')
    tree2.pack(fill="x", expand=True, side="top", anchor="n")

    col_widths2 = {'상품번호': 100, '상품명': 100, '판매가': 100, '갯수': 30, '총액': 100}
    for col in columns2:
        tree2.column(col, width=col_widths2[col])
        tree2.heading(col, text=col)

    tree.bind("<<TreeviewSelect>>", on_Select)

    purchase_btn = tk.Button(user_Purchase_frame,
    text="상품 구매", padx=5, pady=5,
    font=("맑은 고딕", 15, "bold"), command=lambda: purchase_btn_pressed(db_userNum))
    purchase_btn.place(x=400, y=350, width=200, height=70)

    back_btn = tk.Button(user_Purchase_frame, text="뒤로 가기", padx=20, pady=15, command=user_print)
    back_btn.place(x=50, y=400, width=200, height=70)

    w.protocol("WM_DELETE_WINDOW", on_close)

selected_data = []
purchase_soon_list = []

def on_close():
    purchase_soon_list.clear()
    w.destroy()

def purchase_btn_pressed(db_userNum):
    if len(tree2.get_children()) > 0:
        for i in tree2.get_children():
            item_values = tree2.item(i, "values")
            item_no, item_name, item_price, item_Entity, total_price = item_values
            menu.UserFuction_Purchase(item_name, item_Entity, db_userNum)
        m.showinfo("시스템 알림", "상품 구매가 완료되었습니다.")
    else:
        m.showwarning("시스템 알림", "선택한 상품이 없습니다.")
    user_print()

def on_Select(event):
    selected_item = tree.selection()
    selected_data.clear()
    if len(tree2.get_children()) > 0:
            item_values = tree.item(selected_item[0], "values")
            item_no, item_name, item_price = item_values
            for j in tree2.get_children():
                tr2_item_values = tree2.item(j, "values")
                if tr2_item_values[0] == item_no:
                    m.showwarning("시스템 알림", "중복된 품목은 선택할 수 없습니다.")
                else:
                    item_Entity = simpledialog.askinteger("상품 갯수 입력 창", "몇 개 구매하시겠습니까?",
                                                          parent=w,
                                                          minvalue=1, maxvalue=100)
                    if item_Entity is not None:
                            item_values = tree.item(selected_item[0], "values")
                            item_no, item_name, item_price = item_values
                            item_price = int(item_price)
                            total_price = item_price * item_Entity
                            values = (item_no, item_name, item_price, item_Entity, total_price)
                            tree2.insert('', 'end', values=values)
                            selected_data.append(values)
                            m.showinfo("시스템 알림", f"{item_name}이 {item_Entity}개 담겼습니다.")
                            print(selected_data)
                    else:
                        pass
    else:
        item_Entity = simpledialog.askinteger("상품 갯수 입력 창", "몇 개 구매하시겠습니까?",
                                              parent=w,
                                              minvalue=1, maxvalue=100)
        if item_Entity is not None:
                item_values = tree.item(selected_item[0], "values")
                item_no, item_name, item_price = item_values
                item_price = int(item_price)
                total_price = item_price * item_Entity
                values = (item_no, item_name, item_price, item_Entity, total_price)
                tree2.insert('', 'end', values=values)
                selected_data.append(values)
                m.showinfo("시스템 알림", f"{item_name}이 {item_Entity}개 담겼습니다.")
                print(selected_data)


#---------------------------------------------------

login_print()



