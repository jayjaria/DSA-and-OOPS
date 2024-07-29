class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listPrint(self):
        curr = self.head
        while(curr):
            print(curr.data)
            curr = curr.next

def InsertAtStart(self,data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    else:
        new_node.next = self.head
        self.head = new_node

ll = LinkedList()
ll.head = Node(1)
n2 = Node(2)
n3 = Node(3)

ll.head.next = n2
n2.next = n3

ll.listPrint()