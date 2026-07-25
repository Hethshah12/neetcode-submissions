class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q=[]
        g=defaultdict(list)
        courses=prerequisites
        for a,b in courses:
            g[a].append(b)
        un=0
        vi=1
        vis=2
        states=[0]*numCourses
        def dfs(node):
            state=states[node]
            if state==vi:
                return []
            elif state==vis:
                return True
            states[node]=vi
            for nei in g[node]:
                if not dfs(nei):
                    return []
            q.append(node)
            states[node]=vis
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return []
        return q
