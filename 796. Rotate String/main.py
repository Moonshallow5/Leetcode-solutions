class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s=list(s)
        goal=list(goal)
        if(s==goal):
            return True

        for i in range(len(s)):
            x=s.pop(0)
            s.append(x)
            if(s==goal):
                return True
        return False

            

        
        
