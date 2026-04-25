import os
import patient
import AVL_Tree
import Tree_2_3
import patient_notes_list
import chardet

num = ''
def update_data():
    global num
    s = input("讀取舊有資料樹資料(y/n): ")
    while s != 'y' and s != 'n':
        print('輸入錯誤')
        s = input("讀取舊有資料樹資料(y/n): ")
        
    if s =="y":
        while True:
            try:
            
                num = int(input("請輸入該資料樹文件編號: "))
                if num <=0:
                    raise Exception('輸入非大於0')
                break
            except Exception as e:
                print(f"輸入錯誤，需輸入大於0的整數\n{e}")
        print('讀取中...')
        if read_notes(num):
            return True
    num = ''
    return False
    
def read_notes(n):
    t = 0
    if patient_notes_list.get_node() == None:
        print(f"當前無資料樹文件")
        return False
    if not Tree_2_3.inside_f(patient_notes_list.get_node(), n):
        print(f"未找到編號為 {n} 的資料樹文件")
        return False
    
    try:
        result = {}
        with open(f"patient_notes_{n}.txt", "rb") as f:
            result = chardet.detect(f.read())

        inputStream = open(f"patient_notes_{n}.txt", "r", encoding=result['encoding'])
    except FileNotFoundError:
        t = 1
        print(f"patient_notes_{n}.txt not found")
        return False
    if t ==0:
        total_level =  eval(inputStream.readline().strip("\n"))
        patient.set_total_level(total_level)
        tree = AVL_Tree.AVLTree()
        root = None
        for i in range(1, total_level+1):
            root = tree.insert_node(root, i)
        patient.set_tree(root)
        print(f"已建立層級樹: {total_level} 層")
        try:
            while True:
                n, a, g, w = inputStream.readline().strip("\n").split(" ")
                print(n, a, g, w)
                patient.patient_add(n, int(a), g, int(w))
        except Exception  as e:
            pass
        inputStream.close()
        return True
    
def store_notes(root):
    global num
    if num =='':
            try:
                num = input("請輸入該資料樹文件編號: ").strip()
                if not num.isdigit() or int(num) <= 0:  # 檢查是否為正整數
                    raise ValueError("資料樹文件編號必須是正整數！")
                if os.path.exists(f"patient_notes_{num}.txt"):
                    raise ValueError("該資料樹文件編號已經存在！")
                if num != '':
                    pass  # 輸入合法，跳出迴圈
            except ValueError as e:
                print(f"輸入錯誤: {e}請重新操作。")
                num = ''
                return
    print(f"儲存當前資料樹的文件編號: {num}")
    # 定義文件名稱
    filename = f"patient_notes_{num}.txt"
    Str = creat_str(root)
    # 如果文件不存在，創建一個新的文件
    if not os.path.exists(filename):
        print("創建新資料樹文件")
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(Str)
    print(f"\n病患資料樹文件 patient_notes_{num}.txt has be stored!")
    return int(num)

    
def creat_str(root):
    current_tree = root
    s = ''
    n = 0
    Tree = AVL_Tree.AVLTree()
    while current_tree.right != None:
        current_tree = current_tree.right
    s = str(current_tree.key) + "\n"
    for i in range(1, current_tree.key +1):
        temp = Tree.search_node(root, i) 
        if temp.patient_hend == None:
            pass
        else:
            current_node = temp.patient_hend
            while current_node != None:
                n+=1
                ss= ""
                ss = current_node.name + " " + str(current_node.age) + " " + current_node.gender + " " + str(i) + "\n"
                s+=ss
                current_node = current_node.next
    print(f'共有{n}筆資料')
    return s
            


