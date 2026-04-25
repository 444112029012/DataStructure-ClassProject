import tkinter as tk
from tkinter import messagebox

def on_close(root):
    """處理視窗關閉事件"""
    if messagebox.askokcancel("退出", "確定要退出程式嗎？"):
        root.destroy()

def create_main_window():
    """創建主視窗"""
    root = tk.Tk()
    root.title("創建新資料樹文件")
    root.geometry("300x150")
    
    result_var = tk.DoubleVar()
    add_widgets(root, result_var)
    root.mainloop()
    print(f"總層級: {int(result_var.get())}")
    return int(result_var.get())

def add_widgets(root, result_var):
    """添加視窗部件"""
    # 標籤
    label = tk.Label(root, text="請輸入資料樹的緊急程度總級數(1~100)：")
    label.pack(pady=10)

    # 輸入框
    entry = tk.Entry(root, width=20)
    entry.pack(pady=5)

    # 按鈕
    submit_button = tk.Button(root, text="提交", command=lambda: on_submit(entry, root, result_var))
    submit_button.pack(pady=10)

def on_submit(entry, root, result_var):
    """處理數字提交並關閉視窗"""
    try:
        user_input = entry.get()
        number = int(user_input) 
        if number <= 0 or number > 100:
            raise KeyError("層級範圍無效，範圍須介於0到100")
        messagebox.showinfo("輸入成功", f"總層級為：{number}" )
        messagebox.showinfo("提示", '請回到終端機操作')
        result_var.set(number)
        root.destroy()  # 關閉視窗
        return number
    except KeyError as e:
        messagebox.showwarning("輸入錯誤", e)

    except ValueError:
        messagebox.showerror("輸入錯誤", "請輸入一個有效的數字！")

