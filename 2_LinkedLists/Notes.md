# Notes on Linked Lists

* <b>Linked Lists</b> represent a sequence of <b>nodes</b>. Each node points to a <b>next</b> node (even the last node, i.e. the <b>tail node</b>, which points to _None_). These <b>next</b> pointers are how we traverse through a linked list, rather than by indices (which linked lists do not have).
* No constant time access because traversal requires `O(n)` time, where `n = the number of nodes`.
* Key benefits: constant time adding + removing

### Creating a Linked List
* Referencing to the head Node to begin traversal for lookup or adding or deleting
* To ensure references all point to the correct Node for the head, we can create a `LinkedList` class that wraps the `Node` class and preserves the correct reference to the head Node.

### Deleting a Node from a Singly Linked List
* If you want to delete node `n`, find `n`'s previous node (`prev`) and set `prev.next` to equal `n.next`.
* Ensure you are checking for the null pointer (the tail's) and update the head/tail pointers as needed.

### Additional
* The "runner" method, AKA the "second pointer" method, involves the use of two pointers at the same time. The "fast" pointer might be ahead by a predetermined number of nodes.
* Many linked list problems rely on recursion. Recursive problems often require `O(n)` time; this is often faster than iterative solutions (`O(n^2)` time in many cases) but more complex to implement.