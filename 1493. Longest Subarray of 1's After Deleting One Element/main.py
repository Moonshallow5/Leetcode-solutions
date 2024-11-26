class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count_zero=0
        l=0
        res=0
        for r in range(len(nums)):
            if(nums[r]==0):
                count_zero+=1
            while(count_zero>1):
                if(nums[l]==0):
                    count_zero-=1
                l+=1
            res=max(res,r-l+1-count_zero)
        if(res==len(nums)):
            return res-1
        return res

        
