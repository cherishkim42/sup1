'''Given string `s` of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them. We repeatedly make duplicate removals on the string until we no longer can. /// Return the final string after all such duplicate removals have been made. It is guaranteed the answer is unique.

NOTE: No specifications for runtime required. Do not worry about this for now.

-the Linked version will work well for this.
-input [aabbcd] --> return [cd] at the end. Dupes removed.

-LinkedList-ify the input STRING `s`.
-a --> a --> b --> b --> c --> d
-we're gonna be using "temp" nodes again as placeholders (refer to linked list problems)
-a --> a {MEANS THAT} current.data == next.data
-So, set current = next.next
-This effectively "corrects" the linked list to:
-b --> b --> c --> d . And again, we see that
-b --> b {MEANS THAT} current.data. So, again -->
-Set current = next.next
-Wow amazing here we have just
-c --> d

Pass in the head Node. (Build up like Node = whatever, then Node.push etc. etc. in the method, that's how it knows they're all together. Not passing in the WHOLE LINKED LIST.)

The if __name__ == __main__ thing will merely pass in the STRING, NOT the node (this problem is a lil different from linked list problems in the Linked Lists folder).
'''

from stack import Stack

#input_string must be at least length 2
def adjacent_removal(input_string):
    #push, pop, and peek ONLY

    #first, let's make the input string an array.
    string_stack = Stack()
    input_array = list(input_string)
    i = len(input_array)-1
    return_string = ""
    
    #Construct the stack
    while (i >= 0):
        print('stack node: ' + input_array[i])
        string_stack.push(input_array[i])
        i -= 1

# Each iteration should do only 1 comparison to prevent range errors
    compare_value1 = string_stack.pop()
    return_string += compare_value1
    while (string_stack.peek() is not None):
        compare_value2 = string_stack.pop()
        if (compare_value1 == compare_value2):
            pass
        else:
            return_string += compare_value2
        compare_value1 = compare_value2
    return return_string

if __name__ == "__main__":
    print(adjacent_removal("aabbbbccde"))
