class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in s:

            if(i!='*'):
                stack.append(i)
            else:
                if(len(stack)>=1):
                    stack.pop()
                else:
                    return ""
            
        return ''.join(stack)
