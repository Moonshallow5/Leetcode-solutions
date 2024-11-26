class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        count=[0]*n
        for first,sec in edges:
            count[sec]+=1
        print(count)

        z=0
        count2=0

        for index,val in enumerate(count):
            if(val==0):
                count2+=1
                z=index
        if(count2>1):
            return -1
        return z
                


        
        
