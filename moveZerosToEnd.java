public class moveZerosToEnd{
    public static void moveZeros(int nums[]){

        int left = 0;
        int right = 0;
        int temp;
        while(right<nums.length){
            if(nums[right]!=0){
                temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;

            }
            right++;
        }
    }
    public static void main(String[] args) {
        int nums[] = {2,0,6,1,0,8,9,4};
         moveZeros(nums);
         for(int i =0;i<=nums.length;i++){
            System.out.println(nums[i]);
         }
         System.out.println();
       
    }
}