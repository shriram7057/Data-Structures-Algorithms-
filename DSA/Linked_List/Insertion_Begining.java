public class Insertion_Begining {
    static class node {
        int data;
        node next;

        node(int value) {
            data = value;
            next = null;
        }
    }

    static node head;

    static void printList() {
        node p = head;
        System.out.print("\n[");

        // Start from the beginning
        while (p != null) {
            System.out.print(" " + p.data + " ");
            p = p.next;
        }
        System.out.println("]");
    }

    static void insertAtBegining(int data) {
        node lk = new node(data);
        lk.next = head;
        head = lk;
    }

    public static void main(String[] args) {
        int k = 0;
        insertAtBegining(12);
        insertAtBegining(22);
        insertAtBegining(30);
        insertAtBegining(44);
        insertAtBegining(50);
        System.out.print("Linked List after insertion at begining: ");
        printList();
    }
}
