class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max=299999999999999999999
        max2=2999999999999999999
        counter=0
        for i in range(len(nums)):
            if(nums[i]<=max):
                max=nums[i]
            elif(nums[i]<=max2):
                max2=nums[i]
            else:
                return True
        return False
            


        
