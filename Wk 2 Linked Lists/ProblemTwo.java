//Remove duplicates from an unsorted linked list.

import java.util.HashSet;
import java.util.List;

public class ProblemTwo {

  public static void fixedLinkedList(Node headNode) {
    //instantiate a HashSet
    HashSet<Integer> hashSetData = new HashSet<>();
    //current = first
    Node currentNode = headNode; //no "this". not inside the Class
    Node nextNode = headNode.next;
    Node nextNextNode = nextNode.next;

    hashSetData.add(currentNode.data); //def need to add th is
    //loop through the linked list by saying "while current/next != null"
    while (nextNode != null) {
      if (hashSetData.contains(nextNode.data)) {
        currentNode.next = nextNextNode; //currentNode has been updated so this is ok
      }
      else {
        hashSetData.add(currentNode.data);
        currentNode = currentNode.next;
      }
      nextNode = currentNode.next; //currentNode's been updated so it's ok
      if (nextNode != null) {
        nextNextNode = nextNode.next;
      }
    }
  }

  public static void main(String[] args) {
    Node newNode = new Node(1);
    newNode.appendToTail(1);
    newNode.appendToTail(2);
    newNode.appendToTail(3);
//    String stringify = newNode.toString();
//    List listify = newNode.newToString();
    fixedLinkedList(newNode);
    List uniqueNodeList = newNode.intToString();
    System.out.println(uniqueNodeList);
  }

}

//1, 1_ 2, 3
//hashSetData { 1 , 2 , 3}
// currentNode: 3   ; nextNode : null     ; nextNextNode: null
// current .next: 3    ;  .next:  null     ;     .next.next:  null
