

class Node:
    def __init__(self, key):
        self.key1 = key
        self.key2 = None
        self.left = None
        self.middle = None
        self.right = None
    def isLeaf(self):
        return self.left is None and self.middle is None and self.right is None
    def isFull(self):
        return self.key2 is not None
    def hasKey(self, key):
        if (self.key1 == key) or (self.key2 is not None and self.key2 == key):
            return True
        else:
            return False
    def getChild(self, key):
        if key < self.key1:
            return self.left
        elif self.key2 is None:
            return self.middle
        elif key < self.key2:
            return self.middle
        else:
            return self.right
        
root = None
l = []


def insert_f(key):
    global root 
    if root == None:
        root = Node(key)
    else:
        pKey, pRef = put_f(root, key)
        if pKey is not None:
            newNode = Node(pKey)
            newNode.left = root
            newNode.middle = pRef
            root = newNode

    return root

def put_f(node, key):
    if node.hasKey(key):
        return None, None
    elif node.isLeaf():
        return addtoNode(node, key, None)
    else:
        child = node.getChild(key)
        pKey, pRef = put_f(child, key)
        if pKey is None:
            return None, None
        else:
            return addtoNode(node, pKey, pRef)
def addtoNode(node, key, pRef):
    if node.isFull():
        return splitnode(node, key, pRef)
    else:
        if key< node.key1:
            node.key2 = node.key1
            node.key1 = key
            if pRef is not None:
                node.right = node.middle
                node.middle = pRef
        else:
            node.key2 = key
            if pRef is not None:
                node.right = pRef
        return None, None
    
def splitnode(node, key, pRef):
    newnode = Node(None)
    if key < node.key1:
        pKey = node.key1
        node.key1 = key
        newnode.key1 = node.key2
        if pRef is not None:
            newnode.left = node.middle
            node.middle = newnode.right
            node.middle = pRef
    elif key< node.key2:
        pKey = key
        newnode.key1 = node.key2
        if pRef is not None:
            newnode.left = pRef    
            newnode.middle = node.right
    else:
        pKey = node.key2
        newnode.key1 = key
        if pRef is not None:
            newnode.left = node.right    
            newnode.middle = pRef
    node.key2 = None
    node.right = None
    return pKey, newnode

def show_f(node):
    print(node.key1, end='')
    if node.key2 != None:
        print(',', node.key2)
    else:
        print()
    if node.left != None:
        show_f(node.left)
    if node.middle != None:
        show_f(node.middle)
    if node.right != None:
        show_f(node.right)

def inside_f(node, key):
    
    if node.hasKey(key):
        return True
    if node.isFull():
        if key < node.key1:
            if node.left != None and inside_f(node.left, key):
                return True
        elif key < node.key2:
            if node.middle != None and inside_f(node.middle, key):
                return True
        else:
            if node.right != None and inside_f(node.right, key):
                return True
    else:
        if key < node.key1:
            if node.left != None and inside_f(node.left, key):
                return True
        else:
            if node.middle != None and inside_f(node.middle, key):
                return True
    return False
    
def send_f(node):
    global l
    if node.key1 not in l:
        l.append(node.key1)
    if node.key2 != None:
        if node.key2 not in l:
            l.append(node.key2)
    if node.left != None:
        send_f(node.left)
    if node.middle != None:
        send_f(node.middle)
    if node.right != None:
        send_f(node.right)
    return l


    
        
        
        
