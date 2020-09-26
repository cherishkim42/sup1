//last in, first out.
//like a STACK of plates at a diner.


//This is simple sample code to implement a stack. Note that a stack can also be implemented
// using a linked list, if items were added and removed from the same side.

public class MyStack<T> {
  private static class StackNode<t> {
    private T data;
    private StackNode<T> next;

    public StackNode(T data) {
      this.data = data;
    }
  }

  private StackNode<T> top;

  public T pop() {
    if (top == null) throw new EmptyStackException();
    T item = top.data;
    top = top.next;
    return item;
  }

  public void push(T item) {
    StackNode<T> t = new StackNode<T>(item);
    t.next = top;
    top = t;
  }

  public T peek() {
    if (top == null) throw new EmptyStackException();
    return top.data;
  }

  public boolean isEmpty() {
    return top == null;
  }


}