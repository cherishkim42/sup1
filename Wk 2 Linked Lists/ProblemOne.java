//"Palindrome Permutation":

import java.util.List;

public class ProblemOne {

  public static void main(String[] args) {

    Node newNode = new Node(1);
    newNode.appendToTail(2);
    newNode.appendToTail(3);
    newNode.appendToTail(4);
    String stringify = newNode.toString();
    System.out.println(stringify);
    List otherStringify = newNode.newToString();
    System.out.println(otherStringify);
  }
}