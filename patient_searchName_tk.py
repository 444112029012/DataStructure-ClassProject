import tkinter as tk
from tkinter import messagebox
import re

def create_main_window():
    """創建主視窗並回傳使用者輸入的字串"""
    root = tk.Tk()
    root.title("字串輸入器")
    root.geometry("300x150")
    
    result_var = tk.StringVar()  # 使用StringVar來存儲回傳的字串
    add_widgets(root, result_var)
    
    # 在這裡等待視窗關閉並回傳結果
    root.wait_window()  # 等待視窗關閉
    print(f"欲查詢姓名: {result_var.get()}")
    return result_var.get()  # 回傳使用者輸入的字串


def add_widgets(root, result_var):
    def on_close():
        print("取消查詢")
        root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_close)
    """添加視窗部件"""
    # 標籤
    label = tk.Label(root, text="請輸入查詢姓名：")
    label.pack(pady=10)

    # 輸入框
    entry = tk.Entry(root, width=20)
    entry.pack(pady=5)

    # 按鈕
    submit_button = tk.Button(root, text="提交", command=lambda: on_submit(entry, root, result_var))
    submit_button.pack(pady=10)

def on_submit(entry, root, result_var):
    """處理字串提交並關閉視窗"""
    user_input = entry.get()  # 獲取輸入的字串
    try:
        if  (not re.fullmatch(r'[A-Za-z\u4e00-\u9fff]+', user_input)) or (len(user_input)<=0 or len(user_input)> 30):
            raise KeyError("只能輸入中英文，字元數目介於1到30")
    except KeyError as e:
                messagebox.showwarning("輸入錯誤", e)
                return
                
    messagebox.showinfo("輸入成功",  f"查詢姓名是：{user_input}")
    messagebox.showinfo("提示", '請回到終端機操作')
    result_var.set(user_input)  # 將結果儲存至result_var
    root.destroy()  # 關閉視窗




