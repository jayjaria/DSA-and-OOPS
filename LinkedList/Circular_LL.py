class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLL:
    def __init__(self):
        self.head = None

    def InsertAtEnd(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
            new.next = new
            return
        
        curr = self.head
        while(curr.next!=self.head):
            curr=curr.next
        curr.next = new
        new.next = self.head

    def printList(self):
        curr = self.head
        while(curr.next!=self.head):
            print(curr.data)
            curr = curr.next
        print(curr.data)

cll = CircularLL()
cll.InsertAtEnd(1)
cll.InsertAtEnd(2)
cll.InsertAtEnd(3)

cll.printList()