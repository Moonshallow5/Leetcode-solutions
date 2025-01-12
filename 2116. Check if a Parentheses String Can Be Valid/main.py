class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if(len(s)%2!=0):
            return False
        open_c=0
        closed_c=0
        for i in range(len(s)):
            if(s[i]=='(' or locked[i]=='0'):
                open_c+=1
            else:
                open_c-=1
            if(open_c<0):
                return False
        for i in range(len(s)-1,-1,-1):
            if(s[i]==')' or locked[i]=='0'):
                closed_c+=1
            else:
                closed_c-=1
            if(closed_c<0):
                return False
        return True
        
