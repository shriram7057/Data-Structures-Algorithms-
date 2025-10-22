package Arrays;

public class Display
{
    public static void main(String[] args) {
        int LA[] = new int [5];
        System.out.println("The array elements are: ");
        for (int i=0;i<5;i++)
        {
            LA[i]=i+1;
            System.out.println("LA["+i+"] = "+LA[i]);
        }
    }    
}
