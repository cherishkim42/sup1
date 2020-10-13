from stack import Stack

def tryStackMethods(param):
    newStack = Stack()
    newStack.push(1);
    newStack.push(1);
    newStack.push(5);
    if newStack.peek() is None:
        print("I am an empty stack")
    else:
        print("Not empty")
    print(newStack)

if __name__ == "__main__":
    tryStackMethods("omg")
    # pos_inf = float('inf')
    # print(pos_inf - pos_inf)