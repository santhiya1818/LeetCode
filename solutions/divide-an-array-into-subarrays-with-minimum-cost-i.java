class Solution {
public int minimumCost(int[] nums) {
if (nums.length < 3) {
// should not happen, or thrown an exception
return -1;
}
int minV = Math.min(nums[1], nums[2]);
int secondMin = Math.max(nums[1], nums[2]);
for (int i = 3; i < nums.length; i++) {
if (nums[i] <= minV) {
secondMin= minV;
minV = nums[i];
} else if (nums[i] < secondMin){
secondMin = nums[i];
}
}

    return nums[0] + minV + secondMin;
}
}