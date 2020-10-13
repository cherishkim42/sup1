'''Hello, future Cherish. Before running/testing this file, make sure you have un-commented the requisite lines in your PUSH and MIN methods in stack.py.'''


'''Design a stack w/ the following functions: push, pop, and min (the last of which returns the minimum element). All three should operate in constant time.'''

#uses LinkedStack, not ArrayStack
from stack import Stack

#push -- already accounted for; runtime O(1)

#pop -- already accounted for; runtime O(1)

#min -- build and add to Stack.py in the linekdlist version

if __name__ == "__main__":
    newStack = Stack([8, 2, 3, 4, 5])
    print("Min should be 2: ")
    print (newStack.lowest)
    newStack.push(1)
    print("After pushing 1 onto the end, min should be 1")
    print(newStack.min())