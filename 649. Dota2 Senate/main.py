class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        res=[]
        q_R=deque()
        q_D=deque()
        for i in senate:
            res.append(i)
        print(res)
        x=len(senate)
        for i in range(len(res)):
            if(res[i]=='R'):
                q_R.append(i)
            if(res[i]=='D'):
                q_D.append(i)
        while q_R and q_D:
            if(q_R[0]<q_D[0]):
                q_R.append(x)
            else:
                q_D.append(x)
            q_R.popleft()
            q_D.popleft()
            x+=1
        if(q_R):
            return "Radiant"
        else:
            return "Dire"

    

    
