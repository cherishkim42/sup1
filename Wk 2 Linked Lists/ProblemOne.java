//Merge two sorted lists; return it as a new sorted list. The new list should be made by splicing
// together the nodes of the input lists.

//Stretch goal: make a NEW linked list!

import java.util.List;

public class ProblemOne {

  public static Node mergeTwoLinkedLists(Node headNode1, Node headNode2) {
    Node fakeHead = new Node(0);
    Node p = fakeHead;

    Node currentNode1 = headNode1;
    Node currentNode2 = headNode2;
    while(currentNode1 != null && currentNode2 != null) {
      if(currentNode1.data < currentNode2.data) {
        p.next = currentNode1;
        currentNode1 = currentNode1.next;
      } else {
        p.next = currentNode2;
        currentNode2 = currentNode2.next;
      }
      p = p.next;
    }

    if (currentNode1 != null) {
      p.next = currentNode1;
    }

    if (currentNode2 != null) {
      p.next = currentNode2;
    }

    return fakeHead.next;
  }

  public static void main(String[] args) {
    Node newNode1 = new Node(1);
    newNode1.appendToTail(2);
    newNode1.appendToTail(3);
    Node newNode2 = new Node(1);
    newNode2.appendToTail(4);
    newNode2.appendToTail(5);
    System.out.println(newNode1.intToString());
    System.out.println(newNode2.intToString());
    System.out.println(mergeTwoLinkedLists(newNode1, newNode2).intToString());
  }
}


//John 11:35
//  //this linked list is the "master branch" of GitHub lol
//  Node currentNode1 = headNode1;
//  Node nextNode1 = headNode1.next;
////    Node nextNextNode1 = nextNode1.next;
//
//  //and this is someone else's branch getting merged in
//  Node currentNode2 = headNode2;
//  Node nextNode2 = headNode2.next;
////    Node nextNextNode2 = nextNode2.next;
//
//    while (nextNode2 != null) {
//        if (currentNode1.data < currentNode2.data) {
//    currentNode1.next = currentNode2;
//    currentNode1 = nextNode1;
//    }
//    else {
//    currentNode2.next = currentNode1;
//    currentNode2 = nextNode2;
//    }
//    }