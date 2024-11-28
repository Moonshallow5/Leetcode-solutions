class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack=[0]
        visit=set()
        visit.add(0)
        count=0

        while stack:
            key=stack.pop()
            for i in rooms[key]:
                if(i not in visit):
                    visit.add(i)
                    stack.append(i)
                    count+=1
        return count==len(rooms)-1
        
