import sys
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.patient_hend = None
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    #插入新結點
    def insert_node(self, root, key):

        # Find the correct location and insert the node
        if not root:
            return TreeNode(key)
        #判斷key與root的大小關係
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)
            
        #最頂端與擁有最大深度的子樹
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        #左子樹是否大於右子樹
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        #左子樹是否小於右子樹
        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to delete a node
    def delete_node(self, root, key):

        if not root:
            return root
        #判斷key與root的大小關係
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None: #連接右子樹
                temp = root.right
                root = temp
                return temp
            elif root.right is None: #連接左子樹
                temp = root.left
                root = temp
                return temp
            temp = root.right #設定刪除位置之後的節點
            root.key = temp.key
            root.data = temp.data
            root.right = temp.right
            
        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balanceFactor = self.getBalance(root)
        
        #判斷當前子樹的平衡狀況
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    
    def search_node(self, root, key):
        current = root
        #在確保樹大小的範圍下尋找key
        while current != None and key != current.key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        
        return current
    
    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right #y是z的右子樹
        T2 = y.left #t2是y的左子樹
        y.left = z #y左子樹換成z
        z.right = T2 #z右子樹換成t2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left #y是z的左子樹
        T3 = y.right #t3是y的右子樹
        y.right = z #y右子樹換成z
        z.left = T3 #z左子樹換成t3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        #了解現在樹的架構
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        #一直往左子樹向下找
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)


    # Print the tree
    def printHelper(self, currPtr, indent, last):
        #空格長度表示深度
        #先判斷是否為空
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)
            
    
