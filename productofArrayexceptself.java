public class productofArrayexceptself{
    public int[] productExceptSelf(int[] nums) {
    int n = nums.length;
    int[] result = new int[n];

    // Initialize result with all 1s.
    for (int i = 0; i < n; i++) {
        result[i] = 1;
    }

    int leftProduct = 1;
    int rightProduct = 1;

    // Calculate the product of elements to the left of each element.
    for (int i = 0; i < n; i++) {
        result[i] *= leftProduct;
        leftProduct *= nums[i];
    }

    // Calculate the product of elements to the right of each element and multiply it with the result.
    for (int i = n - 1; i >= 0; i--) {
        result[i] *= rightProduct;
        rightProduct *= nums[i];
    }

    return result;
}

public static void main(String[] args) {
    int[] nums = {2, 3, 4, 5};
    int[] result = productExceptSelf(nums);

    System.out.print("Input Array: [");
    for (int i = 0; i < nums.length; i++) {
        System.out.print(nums[i]);
        if (i < nums.length - 1) {
            System.out.print(", ");
        }
    }
    System.out.println("]");

    System.out.print("Result Array: [");
    for (int i = 0; i < result.length; i++) {
        System.out.print(result[i]);
        if (i < result.length - 1) {
            System.out.print(", ");
        }
    }
    System.out.println("]");
}}
