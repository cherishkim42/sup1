# Notes on Arrays and Strings

* Author notes/hopes that most readers are familiar enough with arrays and strings to not warrant an in-depth discussion of them. Fair! LOL
* Array and string questions are often interchangeable.

### Hash Tables

<b>Hash Tables</b> map keys to values for efficient lookup. Steps to implement:

1. Compute the key's hash code (typically `int` or `long`) using the in-built hash function.
2. Map the hash code from step #1 to an index in the array.
3. At this mapped index there is a <b>linked list</b> containing <b>keys</b> and <b>values</b>. Store the key and value in this index. (Linked lists are useful because they handle <b>hash collisions</b> very well -- simply by sticking the incoming colliding element onto the end!)

### ArrayList & Resizable Arrays

* In some languages, arrays/lists resize **automatically**. (Python is one such language.)
* In other languages, array sizes are **fixed**. (Java is one such language.) To get around this in Java, use `ArrayList<>`, which resizes as needed by doubling when appending to an array that is full.
    * Doubling time takes `O(n)` time, but it happens rarely enough that the overall runtime is still `O(1)`.

### StringBuilder

* To avoid getting the horrendous runtime of `O(xn^2)`, we can use `StringBuilder`.
* `StringBuilder` creates a resizable array of all the strings and copy them back only when necessary. This is how it saves on runtime!