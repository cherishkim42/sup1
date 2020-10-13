# Reference setofstacks.py
# furthermore -- uses ArrayStack, not LinkedStack

"""vintage tee, brand new phone // high heels on cobblestones // when you are young they assume you know nothing"""

'''Imagine a literal stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure `SetOfStacks` that mimics this. `SetOfStacks` should be composed of several stacks and should create a new stack once the previous one exceeds capacity. `SetOfStacks.push()` and `SetOfStacks.pop()` should behave identically to a single stack (that is, `pop()` should return the same values as it would if there were just a single stack).
'''

from setofstacks import SetOfStacks

if __name__ == "__main__":
    newSetOfStacks = SetOfStacks()
    newSetOfStacks.push(3)
    print(newSetOfStacks)
    newSetOfStacks.push(4)
    newSetOfStacks.push(2)
    newSetOfStacks.push(1)
    print(newSetOfStacks)
    newSetOfStacks.push(5)
    print(newSetOfStacks)
    newSetOfStacks.push(6)
    newSetOfStacks.push(7)
    newSetOfStacks.push(8)
    print(newSetOfStacks)
    newSetOfStacks.push(9)
    print(newSetOfStacks)
    newSetOfStacks.pop()
    newSetOfStacks.pop()
    print(newSetOfStacks)