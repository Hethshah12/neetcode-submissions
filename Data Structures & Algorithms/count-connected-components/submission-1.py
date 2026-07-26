class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #maikng a dict or a adj list at first 
        g=defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        seen=set()
        def dfs(i):
            seen.add(i)
            for nei in g[i]:
                if nei not in seen:
                    dfs(nei)
        
        count=0
        for i in range(n):
            if i not in seen:
                count+=1
                dfs(i)
        return count
                

