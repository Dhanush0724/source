import java.util.Scanner;
import java.util.Random;
public class mergesort {

    public static void main(String[] args) {
        Random rand = new Random();
        long start,end;
        int a[] = new int[10];
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the number of elemnts:");
        int n = sc.nextInt();
        System.out.println("the elements to be sorted are:");
        for(int i =0;i<=n;i++)
        {
            a[i] = rand.nextInt(2000);
            System.out.println(a[i]+" ");
        }
        
        start = System.nanoTime();
            mergesort(a,0,n-1);
        end = System.nanoTime();
        System.out.println("the sorted array is:");
        for(int i =0;i<=n;i++)
        {
            System.out.println(a[i]+" ");
        }
        
    }
    static void mergesort(int a[],int low,int high)
    {
        int mid;
        if(low<high){
        mid =(low+high)/2;
        mergesort(a,low,mid);
        mergesort(a,mid+1,high);
        merge(a,low,mid, high);
    }
}
    public static void merge(int a[],int low, int mid, int high)
    {
        int i,j,h,k;
        int b[] = new int[2210];
        h=low;i=low;j=mid+1;
        while((h<=mid)&&(j<=high))
        {
            if(a[h]<a[j])
            {
                
                b[i] = a[h];
                h++;
            }
            else 
            {
                b[i] = a[j];
                j++;
            }
            i++;
        }
        if(h>mid)
        {
            for(k=j;k<=high;k++)
            {
                b[i] = a[k];
                i++;
            }
        }
        else {
            for(k=h;k<=mid;k++)
            {
                b[i] = a[k];
                h++;
            }
        }
        for(k=low;k<=high-1;k++)
        {
            a[k] = b[k];
        }
    }
}