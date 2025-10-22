public class  Search{
    static class node {
        int data;
        node next;

        node(int value) {
            data = value;
            next = null;
        }
    }

    static node head;

    // display the list
    static void printList() {
        node p = head;
        System.out.print("\n[");

        // start from the beginning
        while (p != null) {
            System.out.print(" " + p.data + " ");
            p = p.next;
        }
        System.out.print("]");
    }

    // insertion at the beginning
    static void insertatbegin(int data) {

        // create a link
        node lk = new node(data);
        ;

        // point it to old first node
        lk.next = head;

        // point first to new first node
        head = lk;
    }

    static int searchlist(int key) {
        node temp = head;
        while (temp != null) {
            if (temp.data == key) {
                return 1;
            }
            temp = temp.next;
        }
        return 0;
    }

    public static void main(String args[]) {
        int k = 0;
        insertatbegin(12);
        insertatbegin(22);
        insertatbegin(30);
        insertatbegin(44);
        insertatbegin(50);
        insertatbegin(33);
        System.out.print("Linked List: ");

        // print list
        printList();
        int ele = 44;
        System.out.print("\nElement to be searched is: " + ele);
        k = searchlist(ele);
        if (k == 1)
            System.out.println("\nElement is found");
        else
            System.out.println("\nElement is not found in the list");
    }
}