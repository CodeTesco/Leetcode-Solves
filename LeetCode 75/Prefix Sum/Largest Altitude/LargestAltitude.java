public class LargestAltitude {
    public static int largestAltitude(int[] gain) {
        int highest = 0;
        int sum = 0;

        for (int i = 0; i < gain.length; i++) {
            sum += gain[i];
            highest = Math.max(sum, highest);
        }

        return highest;
    }

    public static void main(String[] args) {
        int largest = largestAltitude(new int[] {-5, 1, 5, 0, -7});
        System.out.println(largest);
    }
}