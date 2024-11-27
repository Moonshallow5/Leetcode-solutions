class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap=[]
        res=[]
        for j in range(min(len(nums2),k)):
            heapq.heappush(heap,(nums1[0]+nums2[j],0,j))
        while heap and len(res)<k:
            sums,i,j=heapq.heappop(heap)
            res.append([nums1[i],nums2[j]])
            if ((i+1)<len(nums1)):
                heapq.heappush(heap,(nums1[i+1]+nums2[j],i+1,j))
        return res
