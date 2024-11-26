class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res=[0]*len(temperatures)
        stack=[]
        for i,v in enumerate(temperatures):
            while( stack and v>stack[-1][0]):
                stacktemp, stackind=stack.pop()
                res[stackind]=(i-stackind)
            stack.append((v,i))
        return res



        
