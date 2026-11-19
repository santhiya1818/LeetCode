class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);

    int closeSum=Integer.MAX_VALUE;
    int minDiff=Integer.MAX_VALUE;

    for(int i=0; i<nums.length-2; i++){

        int left=i+1;
        int right=nums.length-1;

        while(left<right){

            int currentSum=nums[i]+nums[left]+nums[right];
            int diff=Math.abs(currentSum-target);

            if(diff<minDiff){

                minDiff=diff;
                closeSum=currentSum;
            }
            if(currentSum<target){

                left++;
            }else{
                right--;
            }
        }
    }

    return closeSum;
        
    }
}