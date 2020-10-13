"""Didn't you calm my fears with a Cheshire cat smile?"""

'''Imagine a literal stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.

TASK:
-- Implement a data structure `SetOfStacks` that mimics this.
-- `SetOfStacks` should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
--- `SetOfStacks.push()` and `SetOfStacks.pop()` should behave identically to a single stack (that is, `pop()` should return the same values as it would if there were just a single stack).
'''

#uses ArrayStack, not LinkedStack
from stack import Stack

class SetOfStacks(object):

    def __init__(self):
        #Initialize a new list to store each ArrayStack.
        #Arbitrarily set capacity for the stack at each index.
        self.array_of_stacks = list()
        self.capacity = 4


    def __repr__(self):
        return 'SetOfStacks({} items, top={})'.format(len(self.array_of_stacks), self.array_of_stacks[-1])

    """
    (1) Find the size of the Stack at the last index.
    (2) If the size exceeds capacity (4),
        --- Start a new stack at the next index and push the new element into that new stack at that new index.
    (3) If the size DOES NOT exceed capacity,
        --- Take the Stack at that index and append."""
    def push(self, item):
        if len(self.array_of_stacks) == 0:
            self.array_of_stacks.append([item])
        else:
            if len(self.array_of_stacks[-1]) > 3:
                self.array_of_stacks.append([item])
            else:
                self.array_of_stacks[-1].append(item)


    """
    (1) Find the size of the Stack at the last index.
    (2) If the size is just 1,
        --- Use the Stack .pop() operation to 
            (1) save the value and return it, and also 
            (2) remove the whole Stack from that index in the Array.
    (3) If the size exceeds 1,
        -- Just take the Stack at that index and use the stack .pop() method.
    """
    def pop(self):
        if len(self.array_of_stacks) == 0:
            raise NameError("Can't remove anything from an empty array of stacks!")
        else:
            target_element = self.array_of_stacks[-1][-1]
            if len(self.array_of_stacks[-1]) == 1:
                del self.array_of_stacks[-1]
            else:
                del self.array_of_stacks[-1][-1]
            return target_element
    
SetOfStacks = SetOfStacks