class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for char in s:
            
            if char!=']':
                stack.append(char)
                continue
            print(stack)
            innerString=""
            while stack and stack[-1]!='[':
                innerString=stack.pop()+innerString
                print(innerString)
            stack.pop()
            multiplier=""
            while stack and stack[-1].isdigit():
                multiplier=stack.pop()+multiplier
            stack.append(int(multiplier)*innerString)
        return ''.join(stack)



        return "asf"
        
