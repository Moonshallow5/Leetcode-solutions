class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        arr = [math.ceil(float(success) / potion) for potion in potions]
        arr.sort()
        print(arr)

        res = []
        for spell in spells:
            l, r, M = 0, len(arr) - 1, 0
            while l <= r:
                m = l+(r - l) // 2
                if arr[m] <= spell:
                    l = m + 1
                    M = l
                else:
                    r = m - 1
            res.append(M)
        return res
                

        return [3]
        
