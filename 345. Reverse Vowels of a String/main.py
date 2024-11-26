class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels={'a','e','i','o','u','A','E','I','O','U'}
        start=0
        end=len(s)-1
        x=list(s)
        while(start<end):
            if(x[start] in vowels and x[end] in vowels):
                x[start],x[end]=x[end],x[start]
                start+=1
                end-=1
            elif(x[start] in vowels and x[end] not in vowels):
                end-=1
            elif(x[end] in vowels and x[start] not in vowels):
                start+=1
            
            else:
                start+=1
        print(x)
            
        return ''.join(x)
                

        
