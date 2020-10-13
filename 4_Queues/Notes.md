# Notes on Queues

### Quick Overview
* Queue of data -- think of a real-life queue, like at a theme park. (*Pretend Rapid Passes do not exist LOL*)
* First In First Out (FIFO) -- **just like** a real-life queue
* Like a **stack**, a queue can be implemented with an **array** or a **linked list**
* Common use cases:
    * Breadth-first search (trees!)
    * Implementation of a cache

### Operations
* `enqueue(item)` adds a newcomer element to the queue
    * _This is_ `add(item)` _in CTCI_
* `dequeue()` admits the first element in line, thus removing it from the queue
    * _This is_ `remove()` _in CTCI_
* `front()` returns the first in line (without admitting them)
    * _This is_ `peek()` _in CTCI_ 
* `is_empty()` returns true iff the queue is empty (i.e., no one is in line!)