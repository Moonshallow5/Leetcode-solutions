class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic={}
        nums2=sorted(nums)
        for i,v in enumerate(nums2):
            if(v not in dic):
                dic[v]=i
        res=[]
        print(dic)
        for num in nums:
            res.append(dic[num])
        return res



        
