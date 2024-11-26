class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        combined_cards=sorted(zip(nums2,nums1),reverse=True)
        
        heap=[]
        sums=0
        max_score=0
        for card_2val, card_1val in combined_cards:
            if(len(heap)!=k):
                heapq.heappush(heap,card_1val)
                sums+=card_1val
            if(len(heap)==k):
                max_score=max(max_score,sums*card_2val)
                sums-=heapq.heappop(heap)
        return max_score

        return 1


        
