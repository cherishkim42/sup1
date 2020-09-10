public class Node {
  Node next = null;
  int data;

//  is used when we say new Node();
  //This is a *special* constructor method
  public Node(int d) {
    data = d;
  }

  //I am a steering wheel not the car manual
  //we don't say static b/c this applies to an instance
  //could say public. defaults to "package private"
  //the d is the data
  public void appendToTail(int d) {
    Node end = new Node(d);
    Node n = this; //I am literally referring to myself
    while (n.next != null) {
      n = n.next;
    }
    n.next = end;
  }


  //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  // write this to print out all values of the linked list
  //write the iterative ver first, should be similar to appendtotail
  //if i can do that, write it as a recursive version

  //let's make this recursive; print not just the head node,
  //but all the values.
  //put a delimeter, like a space, in between each one so
  //not all smushed together
  //making a toString method
  public String toString() {
    //while thisNode.next != null;
    //call myself on the current node;
    return Integer.toString(data);
  }
}
