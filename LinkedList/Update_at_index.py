class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def UpdateAtIndex(self,val,index):
    curr = self.head
    position =0
    if position == index:
        curr.data = val
    else:
        while(curr!=None and position!=index):
            position+=1
            curr = curr.next
        if curr!=None:
            curr.data = val
        else:
            print("This index does not exists")