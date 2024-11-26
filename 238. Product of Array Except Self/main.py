class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans=[1]*n
        curr=1
        for i in range(n):
            ans[i] *= curr
            curr *= nums[i]
            print(ans[i])
        curr = 1
        for i in range(len(nums)-1,-1,-1) :
            ans[i] *= curr
            curr *= nums[i]
            print(ans[i])
        
        return ans
        

        

            
        
