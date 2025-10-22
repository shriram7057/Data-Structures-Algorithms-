package Arrays;
public class Traversal
{
    public static void main(String[] args) 
    {
        int LA[]=new int [10];
        System.out.println("Array ELements Are:");
        for (int i=0;i<LA.length;i++)
        {
            LA[i]=i+1;
            System.out.println("LA["+i+"]="+LA[i]);
        }    
    }
}

// Explanation:
// ------------
// → Traversal means visiting each element of the array sequentially.
// → In this program, we create an integer array of 10 elements.
// → Each element is assigned a value equal to (index + 1).
// → The loop then prints every element with its index.