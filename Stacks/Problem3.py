# draw a picture and think thru the strategy first before committing any code

'''Imagine a literal stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure `SetOfStacks` that mimics this. `SetOfStacks` should be composed of several stacks and should create a new stack once the previous one exceeds capacity. `SetOfStacks.push()` and `SetOfStacks.pop()` should behave identically to a single stack (that is, `pop()` should return the same values as it would if there were just a single stack).

Pseudocode:

Using Array of Stacks to implement.

In construction:
* Arbitrarily set limit on size of the Stack at each  index; let's say 4.
*

SetOfStacks.push():
* Find the size of the Stack at the last index.
* If the size exceeds capacity (set in construction),
* Start a new stack at the next index and push the new element into that new stack at that new index.
* If the size DOES NOT exceed capacity,
* Take the Stack at that index and use the stack .push() method.

SetOfStacks.pop():
* Find the size of the Stack at the last index.
* If the size is just 1,
* Use the Stack .pop() operation to save the value and return it, and also remove the whole Stack from that index in the Array.
* If the size exceeds 1,
* Just take the Stack at that index and use the stack .pop() method.'''


from stack import LinkedStack

class SetOfStacks(object):

    def __init__(self):
        self.array_of_stacks = LinkedStack()
        self.size_limit = 4

    def push(self, item):
        