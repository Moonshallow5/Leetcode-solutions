class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        currSum=maxSum=sum(nums[:k])
        

        for i in range(k,len(nums)):
            currSum+=nums[i]-nums[i-k]

         

            if(currSum>maxSum):
                maxSum=currSum
            
        return maxSum/(float(k))
       







        
