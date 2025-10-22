package Arrays;
import java.util.Scanner;
public class Searching 
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int LA[] = {3, 4, 5, 6, 7};

        System.out.print("Enter element to search: ");
        int item = sc.nextInt();

        boolean found = false;
        for (int i = 0; i < LA.length; i++) {
            if (LA[i] == item) {
                System.out.println("Element " + item + " is found at index -> " + i);
                found = true;
                break;
            }
        }

        if (!found)
            System.out.println("Element not found in the array.");
    }
}


// Explanation:
// ------------
// → The program uses a for loop to traverse each element of the array.
// → It compares each element with the value entered by the user.
// → If a match is found, the position (index) of that element is displayed.
// → If no match is found after traversing the entire array, it displays a message that the element is not found.

// Example Output:
// ---------------
// Enter element to search: 6
// Element 6 is found at index -> 3
// */
