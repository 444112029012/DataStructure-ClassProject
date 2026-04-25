
import patient_add_tk
import patient_mod_tk
import patient_del_tk
from AVL_Tree import AVLTree
import patient_searchName_tk
import heapq
import re

root = None
Tree = AVLTree()
level = 0
def set_tree(r):
    global root
    root = r

def set_total_level(l):
    global level
    level = l

def Set(r, t, l):
    global level
    global root
    global Tree
    level = l
    root = r
    Tree = t

def send():
    global level
    global root
    global Tre
    return root, Tree, level

class PatientNode:
    def __init__(self, name, age, gender):
        self.name = name
        self.gender = gender
        self.age = age
        self.next = None

def patient_add(name='', age=-1, gender='', weight = -1):
    global level
    global root
    global Tree
    t = 1
    name = name.strip()
    
    
    if  name != '':
        if  not (re.fullmatch(r'[A-Za-z\u4e00-\u9fff]+', name)) or not (len(name)>0 and len(name)<= 30):
            return
        if weight_inside_level(weight):
            patient = PatientNode(name, age, gender)
            temp = Tree.search_node(root, weight)
            if temp.patient_hend == None:
                temp.patient_hend = patient
                print("新增成功")
            else:
                current = temp.patient_hend
                if current.name == name and current.gender == gender and current.age == age:
                    t = 0
                if t == 1:
                    while current.next != None:
                        current  = current.next
                        if current.name == name and current.gender == gender and current.age == age:
                            t = 0
                    if t == 1:
                        current.next = patient
                        print("新增成功")
                    else:
                        print("已存在相同資料")
                else:
                    print("已存在相同資料")
            
        else:
            print("輸入等級超過範圍")
    else:
        data = patient_add_tk.Patien_add_access()
        if data != []:
            name = data[0]
            age = data[1]
            gender = data[2]
            weight = data[3]
    
            if weight_inside_level(weight):
                patient = PatientNode(name, age, gender)
                temp = Tree.search_node(root, weight)
                if temp.patient_hend == None:
                    temp.patient_hend = patient
                    print("新增成功")
                    print(f'新增的資料: 姓名:{name}, 年齡:{age}, 性別:{gender}, 緊急程度:{weight}')
                else:
                    current = temp.patient_hend
                    if current.name == name and current.gender == gender and current.age == age:
                        t = 0
                    if t == 1:
                        while current.next != None:
                            current  = current.next
                            if current.name == name and current.gender == gender and current.age == age:
                                t = 0
                        if t == 1:
                            current.next = patient
                            print("\n新增成功")
                            print(f'新增的資料: 姓名:{name}, 年齡:{age}, 性別:{gender}, 緊急程度:{weight}')
                        else:
                            print("已存在相同資料")
                    else:
                        print("已存在相同資料")
                
            else:
                print("輸入緊急程度不在範圍")
        else:
            print("已取消新增")
    
def patient_mod():
    global data_list
    global root
    data_list = []
    build_link(root)
    n = 0
    for v, j in data_list:    
        if j !=[]:
            n = 1
    if n == 0:
        print('無資料可更改')
        return
    data = patient_mod_tk.Patien_mod_access()
    if data != []:
        name = data[0]
        age = data[1]
        gender = data[2]
        weight = data[3]
        if weight_inside_level(weight):
            temp = Tree.search_node(root, weight)
            if temp.patient_hend == None:
                print("該分級無資料")
            else:
                current = temp.patient_hend
                while current != None:
                    if current.name == name and current.gender == gender:
                        break
                    current = current.next
                if current == None:
                    print("查無資料: ", end="")
                    print("姓名:%s, 年齡:%s, 性別:%s, 緊急程度:%s" %(name, age, gender, weight))
                else:
                    if current.age == age:
                        print("已存在相同資料")
                    else:
                        print(f"修改成功\n姓名:{name} 年齡: {current.age} -> {age}")
                        current.age = age
                        
        else:
            print("輸入等級超過範圍")
    else:
        print("已取消更改")

def patient_del():
    global data_list
    global root
    data_list = []
    build_link(root)
    n = 0
    for v, j in data_list:    
        if j !=[]:
            n = 1
    if n == 0:
        print('無資料可刪除')
        return
    data = patient_del_tk.Patien_del_access()
    if data != []:
        name = data[0]
        age = data[1]
        gender = data[2]
        weight = data[3]
        if weight_inside_level(weight):
            temp = Tree.search_node(root, weight)
            if temp.patient_hend == None:
                print("該分級無資料")
            else:
                current = temp.patient_hend
                forward = None
                while current != None:
                    if current.name == name and current.gender == gender and current.age == age:
                        break
                    forward = current
                    current = current.next
                if current == None:
                    print("查無資料: ", end="")
                    print("姓名:%s, 年齡:%s, 性別:%s, 緊急程度:%s" %(name, age, gender, weight))
                else:
                    if forward == None:
                        temp.patient_hend = current.next
                    else:
                        forward.next = current.next
                    print("刪除成功")
                    print(f'刪除的資料: 姓名:{name}, 年齡:{age}, 性別:{gender}, 緊急程度:{weight}')
        else:
            print("輸入等級超過範圍")
    else:
        print("已取消刪除")
            
def patient_search():
    global root
    global data_list
    data_list = []
    build_link(root)
    n = 0
    for v, j in data_list:    
        if j !=[]:
            n = 1
    if n == 0:
        print('無資料可查詢')
        return
    print("\n=========================")
    print("1.分級搜尋    2.特定病人搜尋")
    n = input("搜尋方式: ")
    try:
        n = int(n)
        if n == 1:
            weight = input("欲搜尋緊急程度: ")
            try:
                weight = int(weight)
                while not weight_inside_level(weight):
                    print("輸入錯誤")
                    try:
                        weight = int(input("欲搜尋緊急程度: "))
                        if weight <= 0:
                            print("程度輸入錯誤")
                            raise Exception("<=0")
                    except Exception:
                        weight = -1
                        
                weight_search(weight)
            except Exception:
                print("輸入錯誤，請輸入數字")
            
        elif n == 2:
            patient_search_access()
        else:
            print('輸入無效，請重新操作')
    except Exception:
        print("輸入錯誤，請重新操作")
    
    
        
    
def weight_search(key):
    global Tree
    global root
    temp = Tree.search_node(root, key)
    if temp.patient_hend == None:
        print("該分級無資料")
    elif not weight_inside_level(key):
        print("輸入範圍無效")
    else:
        current = temp.patient_hend
        print("--------------------------------")
        print("緊急程度:%s" %key)
        while current != None:
            
            print("\n姓名:%s, 年齡:%s, 性別:%s" %(current.name, current.age, current.gender))
            current = current.next
    
def patient_search_access(name = ""):
    global level
    global Tree
    global root
    l = []
    if name == "":
        name = patient_searchName_tk.create_main_window()
    for i in range(1, level +1):
        temp = Tree.search_node(root, i)
        current = temp.patient_hend
        while current != None:
            if current.name == name:
                l.append([current.name, current.age, current.gender, i])
                
            current = current.next
    if l != []: 
        for n, a, g, i in l:
            print("姓名:%s, 年齡:%s, 性別:%s, 緊急程度:%d" %(n, a, g, i))
    print(f"共找到{len(l)}筆資料")
    
def weight_inside_level(weight):
    global level
    if weight <= level and weight >0:
        return True
    else:
        print(f'當前資料樹最高層級:{level}, 輸入層級:{weight} 不在範圍內')
        return False
    
def display():
    global root
    global data_list
    global level
    print("================")
    print('讀取中...')
    print()
    heap = []
    data_list = []
    build_link(root)
    num = 0
    print(f'總層級:{level}')
    print('------------------------------')
    for i in range(len(data_list)):
        heapq.heappush(heap, data_list[i])
    for i in range(len(heap)):
        v, j = heapq.heappop(heap)    
        if j != []:
            print("\n緊急程度:%d" %v)
            for n, a, g in j:
                print(f"姓名:{n}, 年齡:{a}, 性別:{g}")
                num+=1
            print('------------------------------')
    print(f'共{num}筆資料')
        

data_list = []    
def build_link(root):
    global data_list
    lis = [-1, []]
    if root != None:
        lis[0] = root.key
        current = root.patient_hend
        while current != None:
            lis[1].append([current.name, current.age, current.gender])
            current = current.next
        if lis not in data_list:
            data_list.append(lis)
        if root.left != None:
            build_link(root.left)
        if root.right != None:
            build_link(root.right)
    else:
        print('無資料樹')

    
