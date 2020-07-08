from sys import maxsize

def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0 #return len(stack) == 0 if len(stack) == 0 is true

def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack.")

def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize - 1)
    return stack.pop()

def peek(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1) # return minus infinite
    return stack[-1]

stack = createStack()
#push(stack, '100')
#push(stack, '200')
#push(stack, '300')
#push(stack, '400')
#pop(stack)
print(peek(stack))
print(stack)
