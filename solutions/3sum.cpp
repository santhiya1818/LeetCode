class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>>ans;
sort(nums.begin(),nums.end());
for(int i=0; i<nums.size(); i++){
int target=0-nums[i];
int j= i+1;
int k= nums.size()-1;
while(j<k){
int sum=nums[j]+nums[k];
if(sum<target){
j++;
}
else if(sum>target){
k--;
}
else{
vector temp={nums[i],nums[j],nums[k]};
ans.push_back(temp);
while(j<k && temp[1]==nums[j]){
j++;
}
while(j<k && temp[2]==nums[k]){
k--;
}
}
}
while(i+1<nums.size() && nums[i]==nums[i+1]){
i++;
}
}
return ans;
    }
};