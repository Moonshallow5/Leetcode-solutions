class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        x=[]
        x.append(0)

        x.append(gain[0])
        
        sum=gain[0]

        for i in range(1,len(gain)):
            sum+=gain[i]
            x.append(sum)
            
       
        return max(x)
        
