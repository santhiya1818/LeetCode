class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        j=len(nums)-1
        i=j+1
        while j>=0:
            if nums[j]==val:
                i -= 1
                nums[i],nums[j]=nums[j],nums[i]
            j-=1
            print(nums,i,j)
        return i
        