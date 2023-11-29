import java.util.Scanner;
public class quicksort{
    public static int parition(int arr[],int low,int high)
    {
        int temp;
        int pivot = arr[high];
        int i = (low-1);
        for(int j =low;j<=high-1;j++)
        {
            if(arr[j]<=pivot)
            {
                i++;
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        temp = arr[i+1];
        arr[i+1] = arr[high];
        arr[high] = temp;
        return i+1;        
    }
    public static void quicksort(int arr[],int low,int high)
    {
        if(low<high)
        {
            int pi = parition(arr, low, high);
            quicksort(arr, low, pi-1);
            quicksort(arr, pi+1, high);
        }
    }
    public static void print(int arr[],int n)
    {
        for(int i=0;i<=n;i++)
        {
            System.out.println(arr[i]+" ");
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr[] = new int[10];
        System.out.println("enter the no of elements");
        int n = sc.nextInt();
        System.out.println("entertt the elemenets");
        for(int i=0;i<n;i++)
        {
            arr[i] = sc.nextInt();
        }
        quicksort(arr, 0, n-1);
        print(arr, n);
    }

    
}
