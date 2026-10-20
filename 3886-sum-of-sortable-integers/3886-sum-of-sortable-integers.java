class Solution {
    public int sortableIntegers(int[] nums) {
        int n = nums.length;
        int ans = 0;

        for (int k = 1; k <= n; k++) {
            if (n % k != 0) continue;
            if (check(nums, n, k)) ans += k;
        }
        return ans;
    }

    private boolean check(int[] a, int n, int k) {
        int prevMax = Integer.MIN_VALUE;

        for (int start = 0; start < n; start += k) {
            int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
            int descents = 0;

            for (int j = 0; j < k; j++) {
                int cur = a[start + j];
                int next = a[start + (j + 1) % k];   // cyclic neighbour inside the block
                if (cur > next) descents++;
                min = Math.min(min, cur);
                max = Math.max(max, cur);
            }

            if (descents > 1) return false;          // block cannot be rotated into sorted order
            if (prevMax > min) return false;         // blocks do not fit together
            prevMax = max;
        }
        return true;
    }
}