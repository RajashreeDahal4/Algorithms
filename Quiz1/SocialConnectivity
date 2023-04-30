/*Social network connectivity. Given a social network containing n members and a log file containing m timestamps at
 which times pairs of members formed friendships, design an algorithm to determine the earliest time at which all
 members are connected (i.e., every member is a friend of a friend of a friend ... of a friend).
 Assume that the log file is sorted by timestamp and that friendship is an equivalence relation.
The running time of your algorithm should be mlogn or better and use extra space proportional to n
Hint use Union-Find Data Structure
given m timestamp at which two members formed friendship. earliest time at which all members are connected is
equivalent to setting the higher id as root when doing individual union but also considering complexity
To find: when is the latest time  they all form friendship

Date: April 30,2023
Author: Rajashree Dahal
Problem: Algorithms course by Princeton University Week 1 Quiz problem 1
Solution: Efficiently implemented without using Find method. This implementation replaces the values with the latest time, 
which represents the root of the connected component. 
Therefore, we can find the earliest time at which all members are connected by finding the minimum value in the order array, 
which is the root of the connected component containing all members.
*/



import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class SocialConnectivity {
    int[] order;

    public SocialConnectivity(int n) {
        order = new int[n];
        for (int i = 0; i < n; i++) {
            order[i] = -i - 1;
        }
    }

    //testing if the two people are friends or not previously
    boolean connected(int p, int q, int[] id) {
        if (id[p] == id[q]) {
            return true;
        } else {
            return false;
        }
    }

    // testing if all people are connected
    boolean all_connected(int[] order) {
        int count = 0;
        for (int i = 1; i < order.length; i++) {
            if (order[i] == order[i - 1]) {
                count = count + 1;
            }
        }
        int max_len = order.length - 1;

        if (count == (max_len)) {
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
            SocialConnectivity sc = new SocialConnectivity(n);
            String line;
            int i = 0, least_time = -5; //passing random negative value as least time
            while ((line = scan.nextLine()) != null) {
                String[] values = line.split(" ");
                time = Integer.parseInt(values[0]);
                p = Integer.parseInt(values[1]);
                q = Integer.parseInt(values[2]);
                boolean is_connected = sc.connected(p, q, order);
                if (is_connected == false) {
                    order = sc.union(order, p, q, time);
                    boolean all_relation = sc.all_connected(order);
                    if (all_relation == true) {
                        least_time = order[0];
                        System.out.println("The least required time to get all the people connected is " + least_time);
                        break;
                    }
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + e.getMessage());
        }

    }
}

