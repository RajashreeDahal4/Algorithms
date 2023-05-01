/*
Question 3
Successor with delete. Given a set of n integers S={0,1,...,n−1} and a sequence of requests of the following form:
Remove x from S
Find the successor of x: the smallest y in S such that y≥x.
design a data type so that all operations (except construction)  take logarithmic time or better in the worst case.
Hint: use the modification of the union−find data discussed in the previous question.
//task: to find the successor of x such that it is least greatest element after x.
*/

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class SuccessorWithDelete {
    int[] order;
    int remove_element;

    public SuccessorWithDelete(int n, int remove_element) {
        remove_element = remove_element;
        order = new int[n];
        for (int i = 0; i < n; i++) {
            order[i] = -i - 1;
        }
    }

    int[] remove(int x, int[] order) {
        // I need to remove element x from the array order
        int[] new_order = new int[order.length - 1];
        for (int i = 0, j = 0; i < new_order.length; i++) {
            if (i != x) {
                new_order[j] = order[i];
                j++;
            }
        }
        System.out.println("new order is " + new_order.length);
        return new_order;
    }


    //testing if the two people are friends or not previously
    boolean connected(int p, int q, int[] id) {
        if (id[p] == id[q]) {
            return true;
        } else {
            return false;
        }
    }

    /*adding relation if the people were not friends before and assigning the latest time as root node in the
     union to all its children*/
    int[] union(int[] order, int p, int q, int time) {
        int p_nodes = order[p];
        int q_nodes = order[q];
        for (int i = 0; i < order.length; i++) {
            if (order[i] == p_nodes || order[i] == q_nodes) {
                order[i] = time;
            }
        }
        return order;
    }

    int find_node_successor(int remove_element, int[] order) {
        int successor = -10;
        int k = -10;
        for (int i = 0; i < order.length; i++) {
            if (i == remove_element) {
                successor = order[i];
                k = successor;
            }
        }
        int min_value = remove_element;
        int count = 0;
        for (int j = 0; j < order.length; j++) {
            if (order[j] == k && j != remove_element) {
                if (j > min_value && count == 0) {
                    min_value = j;
                    count = count + 1;

                } else if (j < min_value && count != 0) {
                    min_value = j;
                }
            }
        }
        return min_value;
    }


    public static void main(String[] args) {
        int p, q;
        //reading the file which contains friendship data
        File file = new File(("/Users/rajashreedahal/IdeaProjects/Algorithms/relationship.txt"));
        int n = 0, time;
        Scanner scan;
        try {
            scan = new Scanner(file);
            n = Integer.parseInt(scan.nextLine());

            int[] id = new int[n];
            int[] id1 = new int[n];
            int[] id2 = new int[n];
            int[] order = new int[n];
            for (int i = 0; i < n; i++) {
                order[i] = -i - 1;
            } //assuming they are ordered this way initially.
            int remove_element = 7;

            SuccessorWithDelete sc = new SuccessorWithDelete(n, remove_element);
            String line;
            boolean is_connected = false;
            int i = 0, least_time = -5; //passing random negative value as least time
            while ((line = scan.nextLine()) != null && scan.hasNextLine()) {
                String[] values = line.split(" ");
                time = Integer.parseInt(values[0]);
                p = Integer.parseInt(values[1]);
                q = Integer.parseInt(values[2]);
                is_connected = sc.connected(p, q, order);
                if (is_connected == false) {
                    order = sc.union(order, p, q, time);
                }
            }

            int node_successor = sc.find_node_successor(remove_element, order);
            if (node_successor != remove_element) {
                System.out.println("The node successor is " + node_successor);
            } else {
                System.out.println("This node has no successor");
            }
            ;
            int[] new_order = sc.remove(remove_element, order);

        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + e.getMessage());
        }

    }

}

