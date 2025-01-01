class Solution:
    def maxScore(self, s: str) -> int:
        q_r=deque(s)
        q_l=deque()
        res=[]
        left_zero=0
        right_ones=0
        for i in s:
            if(i=='1'):
                right_ones+=1
        
        for i in range(len(s)-1):
            if(s[i]=='0'):
                left_zero+=1
            q_l.append(s[i])
            x=q_r.popleft()
            if(x=='1'):
                right_ones-=1
            res.append(left_zero+right_ones)
        return max(res)
            

            

            

        
