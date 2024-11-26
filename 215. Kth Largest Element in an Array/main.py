class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        heapq.heapify(nums)
        z=len(nums)-k
        while(z!=0):
            heapq.heappop(nums)
            z-=1
        return nums[0]
        
        
