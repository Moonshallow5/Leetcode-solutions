class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        count[0]=1
        print(count)
        res=0
        l=0
        prefix_sum=0
        for r in range(len(nums)):

            prefix_sum+=nums[r]


            if(prefix_sum-k in count):
                res+=count[prefix_sum-k]
            count[prefix_sum]+=1
        return res
            



        
