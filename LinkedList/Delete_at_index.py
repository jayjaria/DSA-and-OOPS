class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def DeleteAtIndex(self,index):
    if self.head is None:
        return 
    
    position = 0
    if position == index:
        self.head = self.head.next

    curr = self.head
    while(curr!=None and position+1!=index):
        position+=1
        curr = curr.next
        
    if curr!=None:
        curr.next = curr.next.next
    else:
        print("This index does not exists")