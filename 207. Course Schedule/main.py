class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            dic[crs].append(pre)
        visit=set()
        print(dic)

        def dfs(curr):
            if(curr in visit):
                return False
            if(dic[curr]==[]):
                return True
            visit.add(curr)
            for pre in dic[curr]:
                if not dfs(pre):
                    return False
            visit.remove(curr)
            dic[curr]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True







