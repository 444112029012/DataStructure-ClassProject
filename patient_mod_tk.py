import tkinter as tk
from tkinter import messagebox
import re

def create_main_window():
    """創建主視窗"""
    root = tk.Tk()
    root.title("輸入資料表單")

    def on_close():
        print("取消修改")
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    return root

def mod_form_elements(root):
    """創建表單的所有元素"""
    # 名字欄位
    name_label = tk.Label(root, text="當前患者姓名:")
    name_label.grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    # 年齡欄位
    age_label = tk.Label(root, text="更改後年齡:")
    age_label.grid(row=1, column=0, padx=10, pady=5)
    age_entry = tk.Entry(root)
    age_entry.grid(row=1, column=1, padx=10, pady=5)

    # 性別欄位
    gender_label = tk.Label(root, text="當前性別:")
    gender_label.grid(row=2, column=0, padx=10, pady=5)
    gender_var = tk.StringVar()
    male_rb = tk.Radiobutton(root, text="男性", variable=gender_var, value="男性")
    male_rb.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    female_rb = tk.Radiobutton(root, text="女性", variable=gender_var, value="女性")
    female_rb.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    # 緊急程度欄位
    urgency_label = tk.Label(root, text="當前緊急程度 (數字 1~100):")
    urgency_label.grid(row=4, column=0, padx=10, pady=5)
    urgency_entry = tk.Entry(root)
    urgency_entry.grid(row=4, column=1, padx=10, pady=5)

    return name_entry, age_entry, gender_var, urgency_entry

def create_submit_button(root, name_entry, age_entry, gender_var, urgency_entry, return_data_callback):
    """創建提交按鈕"""
    def submit_data():
        """處理用戶輸入並顯示結果"""
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_var.get()
        urgency = urgency_entry.get()

        if not name.strip() or not age or not gender or not urgency:
            messagebox.showwarning("輸入錯誤", "請填寫所有欄位！")
            return

        try:
            if  (not re.fullmatch(r'[A-Za-z\u4e00-\u9fff]+', name)) or (len(name)<=0 or len(name)> 30):
                raise KeyError("姓名只能輸入中英文，字元數目介於1到30")
            age = int(age)
            urgency = int(urgency)
            if age <= 0 or age > 300 or urgency <= 0 or urgency > 100:
                raise ValueError('輸入錯誤')
        except KeyError as e:
            messagebox.showwarning("輸入錯誤", e)
            return
        except ValueError as e:
            messagebox.showwarning("輸入錯誤", '年齡必須是介於0~300，且緊急程度需介於1~100!')
            print(e)
            return
        

        result = f"姓名: {name}\n年齡: {age}\n性別: {gender}\n緊急程度: {urgency}"
        messagebox.showinfo("輸入資料", result)
        messagebox.showinfo("提示", '請回到終端機操作')
        root.destroy()
        return_data_callback([name, age, gender, urgency])

    submit_button = tk.Button(root, text="提交", command=submit_data)
    submit_button.grid(row=5, column=0, columnspan=2, pady=10)

def Patien_mod_access():
    result_data = []

    def return_data_callback(data):
        nonlocal result_data
        result_data = data

    root = create_main_window()
    name_entry, age_entry, gender_var, urgency_entry = mod_form_elements(root)
    create_submit_button(root, name_entry, age_entry, gender_var, urgency_entry, return_data_callback)
    root.mainloop()

    return result_data


