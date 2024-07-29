def createStack():
    stack = []
    return stack

def push(stack, item):
    stack.append(item)
    return stack

def pop(stack):
    stack.pop()
    return stack

def peek(stack):
    return stack[-1]


stack = createStack()
push(stack,1)
push(stack,2)
push(stack,3)
print("Stack", stack)


p = peek(stack)
print("peek", p)
pop(stack)
print("Stack after Pop",stack)
