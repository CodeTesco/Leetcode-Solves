import java.util.Arrays;

public class pivotIndex {
    public static int pivot(int[] nums) {
        int[] lArr = new int[nums.length];
        int[] rArr = new int[nums.length];
        int lSum = 0;
        int rSum = 0;

        for (int i = 0; i < nums.length; i++) {
            lSum += nums[i];
            rSum += nums[nums.length - i - 1];

            lArr[i] = lSum;
            rArr[nums.length - i - 1] = rSum;
        }

        for (int i = 0; i < nums.length; i++) {
            if (lArr[i] == rArr[i]) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int arr = pivot(new int[] {1,2,3});
        System.out.println(arr);
    }
}