import sys
import urgency_level_tk
from AVL_Tree import AVLTree
import patient
import patient_data_txt
import user_data
import patient_notes_list

        
root = None
Tree = AVLTree()
level = 0



def main():
    global level
    global Tree
    global root
    if not user_data.user_login():
        print("已取消登入")
        sys.exit(2)
    user_data.creat_user_info()
    main_2()
    while True:
        print("======================================================")
        print("1.新增   2.修改  3.刪除   4.查詢   5.檢視  6.結束並儲存")
        print("======================================================")
        
        s = input("請選擇:  ")
        if s == "1":
            patient.patient_add()
            root, Tree, level = patient.send()
        elif s =="2":
            patient.patient_mod()
            root, Tree, level = patient.send()
        elif s == "3":
            patient.patient_del()
            root, Tree, level = patient.send()
        elif s == "4":
            patient.patient_search()
            root, Tree, level = patient.send()
        elif s == "5":
            patient.display()
        elif s == "6":
            num = patient_data_txt.store_notes(root)
            if num != None:
                patient_notes_list.store_patient_list(num)
                print()
                while True:
                    h = input("是否要繼續使用?(y/n): ")
                    if h == 'y':
                        root = None
                        main_2()
                        break
                    elif h == 'n':
                        
                        sys.exit(1)
                    else:
                        print('輸入無效')
        else:
            print("輸入無效")
 
        root, Tree, level = patient.send()
       
            
#--------------------------------------------------------------------------
def main_2():
    global level
    global Tree
    global root
    patient_notes_list.read_patient_list()
    if patient_data_txt.update_data():
        print("原始資料上傳完畢")
        root, Tree, level = patient.send()
    else:
        print('開始創建新文件')
        level = urgency_level_tk.create_main_window()
        if level == 0:
            print("已取消執行")
            sys.exit(1)
        for i in range(1, level+1):
            
            root = Tree.insert_node(root, i)
        patient.Set(root, Tree, level)
        
    
main()