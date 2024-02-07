import java.util.*;

public class reversinginArray {
    public static void main(String[] args) {
        int array[] = {1, 2, 3, 4, 5};
        int i;
        System.out.println("Input Array: " + Arrays.toString(array));

        System.out.print("Reversed array is: [");
        for (i = array.length - 1; i >= 1; i--) {
            System.out.print(array[i] + ", ");
        }
        System.out.print(array[i] + "]");
    }
}
