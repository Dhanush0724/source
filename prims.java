import java.util.Scanner;
public class prims{
    public static void main(String[] args) {
    int i,j,n,s,k=0;
    int w[][] = new int[10][10];
    int u =0;
    int v = 0;
    int sum = 0;
    int min;
    int flag = 0;
    int sol[] = new int[10];
    Scanner sc = new Scanner(System.in);
    System.out.println("enter the number of vertices:");
    n = sc.nextInt();
    for(i=1;i<=n;i++)
    sol[i] = 0;
    System.out.println("enter the weighted graph:");
    for(i=1;i<=n;i++)
    for(j=1;j<=n;j++)
    w[i][j] = sc.nextInt();
    System.out.println("enter the source vertex");
    s = sc.nextInt();
    sol[s]=1;
    k=1;
    while(k<=n-1)
    {
        min = 99;
        for(i=1;i<=n;i++)
        for(j=1;j<=n;j++)
        if(sol[i]==1&&sol[j]==0)
        if(i!=j&&min>w[i][j])
        {
            min =  w[i][j];
            u =i;
            v = j;
        }
        sol[v] =1;
        sum+=min;
        k++;
        System.out.println(u+"->"+v+"="+min);
    }
    for(i=1;i<=n;i++)
    if(sol[i]==0)
    flag =1;
    if(flag==1)
    System.out.println("no spanning tree");
    else
    System.out.println("The cost minimum spanning tree is "+sum);
    sc.close();



}}