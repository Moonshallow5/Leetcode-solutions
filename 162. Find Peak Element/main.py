class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=1
        end=len(nums)-2
        if(len(nums)==1):
            return 0
        if(nums[0]>nums[1]):
            return 0
        if(nums[-1]>nums[-2]):
            return len(nums)-1
        while(start<=end):
            mid=start+(end-start)//2
            if(nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]):
                return mid
            if(nums[mid]<nums[mid+1]):
                start=mid+1
            elif(nums[mid]<nums[mid-1]):
                end=mid-1
        
