class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly:
    def __init__(self):
        self.head = None

    def insertAtStart(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def insertAtEnd(self,data):
        new = Node(data)
        curr = self.head
        if self.head is None:
            self.head = new
        else:
            while(curr.next):
                curr = curr.next
            curr.next = new
            new.prev = curr

    def insertAtIndex(self,index,data):
        new = Node(data)
        curr = self.head
        position = 0
        if position == index:
            new.next = self.head
            self.head.prev = new
            self.head = new

        else:
            while(curr and position+1!=index):
                curr = curr.next
                position+=1
            if curr is not None:
                new.prev = curr
                new.next = curr.next
                curr.next = new
            else:
                print("This index does not exists")


    def printList(self):
        curr = self.head
        while(curr):
            print(curr.data)
            curr = curr.next

        
dll = Doubly()
dll.insertAtStart(1)
dll.insertAtStart(2)
dll.insertAtStart(3)
dll.insertAtEnd(4)
dll.insertAtIndex(2,5)
dll.printList()
