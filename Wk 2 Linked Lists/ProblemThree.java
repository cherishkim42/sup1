//Given a singly linked list, determine if it is a palindrome.

//Assuming all upper or all lower, and no characters or #'s
//use an array

//While curr.next != null,
//Starting from the head, append the datum of the node to the array.
//Once we've added all the data of all the nodes to the array,

//it is now looking through the array time
//Search the array bidirectionally
//Start front_index = 0,
//      back_index = -1
//IF array[front_index] != array[back_index],
//      return false
//ELSE,
//      front_index ++,
//      back_index --

import java.util.ArrayList;

public class ProblemThree {

//  Linked List: 1 -> 2 -> 3
  public static Boolean isPalindrome(Node headNode) {
    //instantiate ArrayList to hold the Array-ified Linked List
    ArrayList<Integer> arrayList = new ArrayList<Integer>();

    //current = first
    Node currentNode = headNode; //2
//    Node nextNode = headNode.next; //3

    //arrayList = [1 ]
    while (currentNode != null) {
      arrayList.add(currentNode.data);
      currentNode = currentNode.next;
//      nextNode = nextNode.next;
    }
    System.out.println(arrayList);

    //👀starting here. where is the problem? 1->2->3->1 should not
    //return true.
    int front_index = 0;
    int back_index = arrayList.size() - 1;

    while (front_index < (arrayList.size() / 2)) {
      if (arrayList.get(front_index) != arrayList.get(back_index)) {
        return false;
      }
      front_index ++;
      back_index --;
    }
    return true;

    //❌boo doesn't work
//    if (arrayList.get(front_index) != arrayList.get(back_index)) {
//      return false;
//    }
//    else {
//      front_index ++;
//      back_index --;
//    }
//    return true;

    //❌boo doesn't work
//    for (int front_index = 0; front_index < (back_index / 2); front_index++) {
//      if (arrayList.get(front_index) != arrayList.get(back_index)) {
//        return false;
//      }
//      else { back_index--; };
////      back_index --;
//    }
//    return true;
  }

  public static void main(String[] args) {
    Node newNode = new Node(1);
    newNode.appendToTail(2);
    newNode.appendToTail(3);
    System.out.println("Linked List: 1 -> 2 -> 3");
//    String result = String.valueOf()
    System.out.println(isPalindrome(newNode));
    Node anotherNode = new Node(1);
//    anotherNode.appendToTail(2);
    anotherNode.appendToTail(2);
    anotherNode.appendToTail(1);
    System.out.println("Linked List: 1 -> 2 -> 2 -> 1");
    System.out.println(isPalindrome(anotherNode));
    Node newNewNode = new Node(1);
    newNewNode.appendToTail(2);
    newNewNode.appendToTail(3);
    newNewNode.appendToTail(1);
    System.out.println("Linked List: 1 -> 2 -> 3 -> 1");
    System.out.println(isPalindrome(newNewNode));
    Node yetAnother = new Node(7);
    yetAnother.appendToTail(7);
    yetAnother.appendToTail(1);
    yetAnother.appendToTail(1);
    yetAnother.appendToTail(1);
    yetAnother.appendToTail(1);
    yetAnother.appendToTail(7);
    System.out.println("Linked List: 7 -> 7 -> 1 -> 1 -> 1 -> 1 -> 7");
    System.out.println(isPalindrome(yetAnother));
    Node lonelyNode = new Node(1);
    System.out.println("Linked List: 1 -> //");
    System.out.println(isPalindrome(lonelyNode));
  }

}
