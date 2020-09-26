# Notes on Stacks

### Quick Overview
* Stack of data -- think of a stack of plates at a diner.
    * Credit to Alan Davis for this top-tier metaphor
* Last In First Out (LIFO)
* Your computer's folder structure works this way when you are navigating around.
    * Hit the back button --> top of the stack is popped off
* DOES NOT have constant-time access to the ith item
    * BUT, it DOES allow constant-time ADDITION + REMOVAL
* Useful for some recursive algorithms.

### Operations
* `pop()` removes the topmost plate
* `push(item)` adds a plate to the top of the stack
* `peek()` returns the topmost plate
* `isEmpty()` returns true iff the stack is empty (i.e., no plates!)