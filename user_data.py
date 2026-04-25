import os
import tkinter as tk
from tkinter import messagebox
import chardet
import re

user_info =[]
username_entry = ''
password_entry = ''
root = tk.Tk()
root.title("登入系統")
root.geometry("300x220")

state = False

#-------------------------------------------------------------------------------------
#註冊
def on_signup():
    global user_info
    """
    打開註冊視窗
    """
    def on_close():
        print("取消註冊")
        signup_window.destroy()
        
    def register_user():
        global user_info
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()
        
        if not new_username or not new_password:          
            messagebox.showerror("註冊錯誤", "帳號與密碼不能為空！")
            return
        if  not re.fullmatch(r'[A-Za-z0-9_]+', new_username) or not re.fullmatch(r'[A-Za-z0-9_]+', new_password):
            messagebox.showerror("註冊錯誤", "帳號密碼只能為英文數字與底線！")
            return
        elif len(new_username)<=2 and len(new_username) >= 20:
            messagebox.showerror("註冊錯誤", "帳號長度需介於2~20！")
            return
        elif len(new_password)<=2 and len(new_password) >= 20:
            messagebox.showerror("註冊錯誤", "密碼長度需介於2~20！")
            return
        if  not verify_login(new_username, new_password):
            user_info.append([new_username, new_password])
            print(f'{new_username} 註冊成功')
            print(f'帳號: {new_username}, 密碼: {new_password}')
            messagebox.showinfo("註冊成功", "帳號已成功註冊！")
            
            creat_user_info()
            signup_window.destroy()  # 關閉註冊視窗
        else:
            messagebox.showerror("註冊錯誤", "該帳號已存在！")
    
    signup_window = tk.Toplevel(root)
    signup_window.title("註冊")
    signup_window.geometry("300x200")
    signup_window.protocol("WM_DELETE_WINDOW", on_close)
    # 帳號輸入
    tk.Label(signup_window, text="新帳號：").pack(pady=5)
    new_username_entry = tk.Entry(signup_window, width=25)
    new_username_entry.pack(pady=5)
    
    # 密碼輸入
    tk.Label(signup_window, text="新密碼：").pack(pady=5)
    new_password_entry = tk.Entry(signup_window, width=25, show="*")
    new_password_entry.pack(pady=5)
    
    # 註冊按鈕
    register_button = tk.Button(signup_window, text="註冊", command=register_user)
    register_button.pack(pady=20)


#-------------------------------------------------------------------------------------
def verify_login(username, password):
    global state
    global user_info
    for a, p in user_info:
        if a==username and p == password:
            state = True
            return True
            break
    return False
    

def on_login():   
    global username_entry
    global password_entry
    global root
    """
    處理登入按鈕點擊事件
    """
    username = username_entry.get()
    password = password_entry.get()
    
    if not username or not password:
        messagebox.showerror("登入錯誤", "帳號與密碼不能為空！")
        return
    if  not re.fullmatch(r'[A-Za-z0-9_]+', username) or not re.fullmatch(r'[A-Za-z0-9_]+', password):
        messagebox.showerror("登入錯誤", "帳號密碼只能為英文數字與底線！")
        return
    elif len(username)<=2 and len(username) >= 20:
        messagebox.showerror("登入錯誤", "帳號長度需介於2~20！")
        return
    elif len(password)<=2 and len(password) >= 20:
        messagebox.showerror("登入錯誤", "密碼長度需介於2~20！")
        return
    if verify_login(username, password):
        print(f'{username} 登入成功')
        messagebox.showinfo("登入成功", f"歡迎，{username}！")
        messagebox.showinfo("提示", '請回到終端機操作')
        root.destroy()  # 關閉視窗
    else:
        messagebox.showerror("登入失敗", "帳號或密碼錯誤！")

def creat_login_tk():
    
    global username_entry
    global password_entry
    global root
    
    def on_close():
        print("取消登入")
        root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_close)
    # 帳號輸入
    tk.Label(root, text="帳號：").pack(pady=5)
    username_entry = tk.Entry(root, width=25)
    username_entry.pack(pady=5)

    # 密碼輸入
    tk.Label(root, text="密碼：").pack(pady=5)
    password_entry = tk.Entry(root, width=25, show="*")
    password_entry.pack(pady=5)

    # 登入按鈕
    login_button = tk.Button(root, text="登入", command=on_login)
    login_button.pack(pady=10)

    # 註冊按鈕
    signup_button = tk.Button(root, text="註冊", command=on_signup)
    signup_button.pack(pady=8)

    root.mainloop()


def user_login():
    global state
    update_user_info()
    creat_login_tk()
    if state == True:
        
        return True
    return False
    
    
def update_user_info():
    global user_info
    try:
        
        result = {}
        with open("user_info.txt", "rb") as f:
            result = chardet.detect(f.read())
        
        inputStream = open("user_info.txt", "r", encoding=result['encoding'])
    except FileNotFoundError:
        print("user_info.txt not found")
        creat_user_info()
    
    try:
        while True:
            l = []
            a, p = inputStream.readline().strip("\n").split(" ")
            l.append(a)
            l.append(p)
            user_info.append(l)
            print(f'帳號: {a}, 密碼: {p}')
    except Exception  as e:
        pass
    inputStream.close()
    
def creat_user_info():
    global user_info
    Str = ''
    
    for a, p in user_info:
        ss = ''
        ss = a + " " + p + "\n"
        Str += ss
    # 如果文件不存在，創建一個新的文件
    if not os.path.exists('user_info.txt'):
        print("創建使用者資料表")
    
    with open('user_info.txt', 'w', encoding='utf-8') as file:
        file.write(Str)
    print("\nuser_info.txt has be stored!")
    

