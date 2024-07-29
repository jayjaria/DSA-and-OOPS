class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# Using recursion
# def insert(root,data):
#     if root is None:
#         return Node(data)
#     else:
#         if root.data == data:
#             return root
#         elif root.data > data:
#             root.left = insert(root.left,data)
#         else:
#             root.right = insert(root.right,data)

#     return root

class BST:
    def __init__(self):
        self.root = None

    # Optimised Insertion
    def Insert(self,data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return self.root
        
        prev = None
        temp = self.root
        while(temp!=None):
            if(temp.data > data):
                prev = temp
                temp = temp.left
            elif(temp.data < data):
                prev = temp
                temp = temp.right
            
        if prev.data > data:
            prev.left = new_node
        else:
            prev.right = new_node


    # Optimised Inorder
    def Inorder(self):
        temp = self.root
        stack = []

        while(temp!=None or len(stack)!=0):
            if temp!=None:
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                print(temp.data)
                temp = temp.right



# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data)
#         inorder(root.right)


# root = Node(50)
# root = insert(root,30)
# root = insert(root,70)
# root = insert(root,40)
# root = insert(root,10)
# root = insert(root,60)


tree = BST()
tree.Insert(30)
tree.Insert(50)
tree.Insert(15)
tree.Insert(20)
tree.Insert(10)
tree.Insert(40)
tree.Insert(60)
tree.Inorder()