#!python

from linkedlist import LinkedList

"""
Use the LINKED LIST version of this to implement MIN
There is no way to get findMin down to O(1) runtime using the ArrayStack implementation.
"""

# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        self.lowest = float('inf')
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        return self.list.length()

    #hi push, you're going to have added functionality now
    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Finding the top of the stack and inserting an item at the start of it will always be constant time
        
        functionality added HERE to check for whether or not "item" anti-exceeds the globally declared "lowest". That way, MIN() just has to FETCH the already established global value.
        """
        #COMMENT NEXT 2 LINES BACK IN IF MIN FUNCTIONALITY NEEDED:
        # if (item < self.lowest): #O(1)
        #     self.lowest = item #O(1)
        return self.list.prepend(item) #O(1). also this happens no matter what, EVEN IF we are not changing the value of min.

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if not self.list.is_empty():
            return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – Finding the head takes constant time since you're not looping through anything"""
        if not self.list.is_empty():
            original_top = self.list.head
            self.list.delete(original_top.data)
            # self.list.pop(len(self.list)-1)
            return original_top.data
        else:
            raise ValueError('oh no! the stack is empty')

    #COMMENT THIS METHOD BACK IN IF MIN FUNCTIONALITY NEEDED
    # def min(self):
    #     """Assuming this works: O(1). Fastest return ever! Because you are simply returning a global variable!"""
    #     return self.lowest















# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        if len(self.list) == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – index n-1 is the top; so appending to the end will take constant time"""
        return self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if not self.is_empty():
            return self.list[-1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – it's on the top! constant time"""
        if not self.is_empty():
            original_top = self.list[-1]
            self.list.pop()
            return original_top
        raise ValueError('oh no! the stack is empty')

# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
