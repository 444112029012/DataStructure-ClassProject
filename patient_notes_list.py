import Tree_2_3
import os
import heapq
import chardet

l = []
root_23 = None

def read_patient_list():

    global root_23
    t = 0
    inputStream = None
    try:
        
        result = {}
        with open("patient_list.txt", "rb") as f:
            result = chardet.detect(f.read())
            
        inputStream = open("patient_list.txt", "r", encoding=result['encoding'])
    except FileNotFoundError:
        t = 1
        print("patient_list.txt not found")
    s = inputStream.readline().strip("\n")
    if t == 0:
        try:
            while True:
                num = eval(inputStream.readline().strip("\n"))
                l.append(num)
                root_23 = Tree_2_3.insert_f(num)
        except Exception  as e:
            pass
        inputStream.close()
    show_node()


def store_patient_list(num):
    global root_23
    global l
    lis = []
    if num not in l:
        root_23 = Tree_2_3.insert_f(num)
    lis = Tree_2_3.send_f(root_23)
    # 定義文件名稱
    filename = "patient_list.txt"
    if lis != []:
        Str = creat_str(lis)
        if not os.path.exists(filename):
            print("創建新文件")
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(Str)
        print("\n資料樹編號文件 patient_list.txt has be stored!")
    else:
        print("no detail")
        
def show_node():
    global root_23
    heap = []
    print('已存在的資料樹文件編號:')
    if root_23 != None:
        lis = Tree_2_3.send_f(root_23)
        
        for i in lis:
            heapq.heappush(heap, i)
        for i in range(len(heap)):
            print(heapq.heappop(heap), end = ", ")
    else:
        print('無資料')
def creat_str(l):
    Str = '不可直接更改\n'
    ss = ''

    for i in l:
        ss = str(i) + '\n'
        Str+=ss
    return Str

def get_node():
    global root_23
        
    return root_23
        


