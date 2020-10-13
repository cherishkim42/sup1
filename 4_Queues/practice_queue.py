"""There goes the loudest woman this town has ever seen. I had a marvelous time ruining everything!"""

from queue import Queue

if __name__ == "__main__":
    newQueue = Queue()
    print(newQueue.is_empty())
    newQueue.enqueue(1)
    print(newQueue)
    print(newQueue.is_empty())
    newQueue.enqueue(2)
    print(newQueue)
    newQueue.enqueue(3)
    print(newQueue)
    newQueue.dequeue()
    print(newQueue)
    newQueue.enqueue(4)
    print(newQueue)
    newQueue.dequeue()
    print(newQueue)