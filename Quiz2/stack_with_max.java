/*
Stack with max. Create a data structure that efficiently supports the stack operations (push and pop)
and also a return-the-maximum operation.
 Assume the elements are real numbers so that you can compare them
*/

import java.util.EmptyStackException;

public class stack_with_max {
    private Node first = null;

    private class Node {
        Integer num;
        Integer max_value;
        Node next;
    }

    public void push(Integer num) {
        Node oldfirst = first;
        first = new Node();
        first.num = num;

        if ((oldfirst == null) || (oldfirst.max_value < first.num)) {
            first.max_value = num;
        } else {
            first.max_value = oldfirst.max_value;
        }
        first.next = oldfirst;

    }

    public Integer pop() {

        Integer num = first.num;
        Node second = first.next;
        first = first.next;
        first.max_value = second.max_value;
        return num;
    }

    public Integer get_max() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        return first.max_value;
    }

    public boolean isEmpty() {
        if (first == null) {
            return true;
        } else return false;
    }

    public static void main(String[] args) {
        stack_with_max stack = new stack_with_max();
        stack.push(5);
        stack.push(4);
        stack.push(6);
        stack.pop();
        stack.pop();
        System.out.println("the max element is: " + stack.get_max());

    }
}
