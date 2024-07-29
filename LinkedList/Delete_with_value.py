class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def DeleteWithValue(self,val):
    if self.head is None:
        return 
    
    curr = self.head
    while(curr!=None and curr.next.data!=val):
        curr=curr.next

    if curr is not None:
        curr.next = curr.next.next
    else:
        return