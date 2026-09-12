class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.length == 0 || k <= 0) {
            return new int[0];
        }

        int n = nums.length;
        int[] result = new int[n - k + 1];
        int[] deque = new int[n];   // stores indices
        int head = 0, tail = 0;     // head inclusive, tail exclusive
        int resIndex = 0;

        for (int i = 0; i < n; i++) {
            // remove index out of window
            if (head < tail && deque[head] <= i - k) {
                head++;
            }

            // remove smaller values from the back
            while (head < tail && nums[deque[tail - 1]] < nums[i]) {
                tail--;
            }

            deque[tail++] = i;

            if (i >= k - 1) {
                result[resIndex++] = nums[deque[head]];
            }
        }

        return result;
    }
}