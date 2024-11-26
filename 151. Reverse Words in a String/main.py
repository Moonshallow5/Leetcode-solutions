class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.lstrip()
        s=s.rstrip()
        start=0
        
        x=s.split()
        end=len(x)-1

        while(start<end):
            x[start],x[end]=x[end],x[start]
            start+=1
            end-=1
        return ' '.join(x)
       


        
        
