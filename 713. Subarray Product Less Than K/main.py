class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prod=1
        l=0
        count=0
        if(k<=1):
            return 0
        for r in range(len(nums)):
            prod*=nums[r]
            while(prod >=k):
                prod//=nums[l]
                l+=1
            count+=(r-l)+1
        return count




        
        
