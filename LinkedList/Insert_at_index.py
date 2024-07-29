class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        curr = self.head
        while(curr):
            print(curr.data)
            curr=curr.next

    def InsertAtIndex(self,data,index):
        new_node = Node(data)
        curr = self.head
        position = 0
        if position == index:
            new_node.next = self.head
            self.head = new_node
        else:
            while(curr!=None and position+1!=index):
                position+=1
                curr = curr.next
            
            if curr is not None:
                new_node.next = curr.next
                curr.next = new_node
            else:
                print("This index does not exists")

ll = LinkedList()
ll.head = Node(1)
n2 = Node(2)
n3 = Node(3)
ll.head.next = n2
n2.next = n3

ll.printList()
print("New")
ll.InsertAtIndex(4,2)
ll.printList()
