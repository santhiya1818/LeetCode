import java.util.*;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length < 4) return res;

        Arrays.sort(nums);
        int n = nums.length;

        for (int i = 0; i < n - 3; i++) {
            // Skip duplicates for the first pointer
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            for (int j = i + 1; j < n - 2; j++) {
                // Skip duplicates for the second pointer
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                // Use long to prevent integer overflow for large targets/sums
                long targetSum = (long) target - nums[i] - nums[j];
                int front = j + 1;
                int back = n - 1;

                while (front < back) {
                    long twoSum = (long) nums[front] + nums[back];

                    if (twoSum < targetSum) {
                        front++;
                    } else if (twoSum > targetSum) {
                        back--;
                    } else {
                        res.add(Arrays.asList(nums[i], nums[j], nums[front], nums[back]));

                        // Correctly skip duplicates for third and fourth pointers
                        while (front < back && nums[front] == nums[front + 1]) front++;
                        while (front < back && nums[back] == nums[back - 1]) back--;

                        front++;
                        back--;
                    }
                }
            }
        }
        return res;
    }
}
