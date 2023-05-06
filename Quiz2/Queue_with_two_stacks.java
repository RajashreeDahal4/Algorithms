/*
Queue with two stacks:
Implement a queue with two stacks so that each queue operations takes a constant
amortized number of stack operations.

 */
public class Queue_with_two_stacks {
    private Node first = null;

    private class Node {
        Integer num;
        Node next;
    }

    public void push(Integer num) {
        Node oldfirst = first;
        first = new Node();
        first.num = num;
        first.next = oldfirst;
    }

    public Integer pop() {
        Integer num = first.num;
        Node second = first.next;
        first = first.next;
        return num;
    }

    public boolean isEmpty() {
        if (first == null) {
            return true;
        } else return false;
    }

    public static void main(String[] args) {
        Queue_with_two_stacks stack1 = new Queue_with_two_stacks();
        Queue_with_two_stacks stack2 = new Queue_with_two_stacks();
        stack1.push(5);
        stack1.push(4);
        stack1.push(6);
        int num;
        //removing elements from first stack and putting it in the second stack
        while (!stack1.isEmpty()) {
            num = stack1.pop();
            System.out.println(num);
            stack2.push(num);
        }
        //removing from the second stak
        while (!stack2.isEmpty()) {
            num = stack2.pop();
            System.out.println(num);
        }
    }
}
