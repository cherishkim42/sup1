"""don't you dream impossible things?"""

"""Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks."""

#okay, so format it like I formatted setofstacks.py. I am making my own class! It is class making time

#ArrayStack

class MyQueue(object):
    def __init__(self):
        self.stack_one = []
        self.stack_two = []

    def __repr__(self):
        front_value = 0
        if len(self.stack_two) == 0:
            if len(self.stack_one) == 0:
                front_value = None
            else:
                front_value = self.stack_one[-1]
        else:
            front_value = self.stack_two[-1]
        return 'Queue({} items, front={})'.format((len(self.stack_one) + len(self.stack_two)), front_value)

    def is_empty(self): #Boolean
        if len(self.stack_one) == 0 and len(self.stack_two) == 0:
            return True
        return False
    
    def enqueue(self, item):
        self.stack_one.append(item)

    def dequeue(self):
        if not self.stack_two:
            while self.stack_one:
                self.stack_two.append(self.stack_one.pop())
        return self.stack_two.pop()

MyQueue = MyQueue
