class Node:
    def __int__(self,data):
        self.data = data
        self.next = None

def InsertAtEnd(self,data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return 

    curr = self.head
    while(curr.next):
        curr = curr.next

    curr.next = new_node