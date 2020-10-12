//Cut dupes from a sorted linked list.

import java.util.List;

//Just check if the next node's data equals current's data.
//if it does, set current's next to next's next.
public class ProblemFour {

  public static void removeDupes(Node headNode) {
    Node currentNode = headNode;

    while(currentNode != null) {
      Node placeHold = currentNode;
      while (placeHold != null && placeHold.data == currentNode.data) {
        placeHold = placeHold.next;
      }
      currentNode.next = placeHold;
      currentNode = currentNode.next;
    }
  }

  public static void main(String[] args) {
    Node newNode = new Node(1);
    newNode.appendToTail(1);
    newNode.appendToTail(2);
    newNode.appendToTail(3);
    newNode.appendToTail(4);
    newNode.appendToTail(5);
    removeDupes(newNode);
    List newNodePrint = newNode.intToString();
    System.out.println(newNodePrint);
  }

}
