# Reference queueofstacks.py

"""Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks."""

from myqueue import MyQueue

if __name__ == "__main__":
    newqueue = MyQueue()
    newqueue.enqueue(1)
    print(newqueue)
    newqueue.enqueue(2)
    print(newqueue)
    newqueue.enqueue(3)
    newqueue.enqueue(4)
    print(newqueue)
    newqueue.dequeue()
    newqueue.dequeue()
    newqueue.enqueue(7)
    print(newqueue)