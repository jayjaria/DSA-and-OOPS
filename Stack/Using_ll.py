class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    # Method to add at the start of the stack.(at the position of head)
    def push(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        return self.head

    # Removes element that is the curernt head
    def pop(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return self.head
    
    # Returns the head node of the linked list
    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data
        
    def printList(self):
        curr = self.head
        while(curr):
            print(curr.data)
            curr = curr.next

ll = Stack()
ll.push(1)
ll.push(2)
ll.push(3)
ll.pop()
ll.peek()
ll.printList()
