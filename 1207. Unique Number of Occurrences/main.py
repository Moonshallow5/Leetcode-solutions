class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        x=Counter(arr)
        print(x)
        y=[]
        for i in x.values():
            y.append(i)
        length=len(y)
        z=set(y)
        if(len(z)==length):
            return True
        else:
            return False

