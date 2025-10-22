public class Reversal {
    static Node head;

    static class Node {
        int data;
        Node next;

        Node(int value) {
            data = value;
            next = null;
        }
    }

    // display the list
    static void printList(Node node) {
        System.out.print("\n[");

        // start from the beginning
        while (node != null) {
            System.out.print(" " + node.data + " ");
            node = node.next;
        }
        System.out.print("]");
    }

    static Node reverseList(Node head) {
        Node prev = null;
        Node cur = head;
        Node temp = null;
        while (cur != null) {
            temp = cur.next;
            cur.next = prev;
            prev = cur;
            cur = temp;
        }
        head = prev;
        return head;
    }

    public static void main(String args[]) {
        Reversal list = new Reversal();
        list.head = new Node(33);
        list.head.next = new Node(50);
        list.head.next.next = new Node(44);
        list.head.next.next.next = new Node(22);
        list.head.next.next.next.next = new Node(12);
        System.out.print("Linked List: ");

        // print list
        list.printList(head);
        head = list.reverseList(head);
        System.out.print("\nReversed linked list ");
        list.printList(head);
    }
}