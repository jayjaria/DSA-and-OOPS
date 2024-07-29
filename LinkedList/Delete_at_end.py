class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def DeleteAtEnd(self):
    if self.head is None:
        return
    
    curr = self.head
    while(curr.next.next):
        curr = curr.next

    curr.next=None