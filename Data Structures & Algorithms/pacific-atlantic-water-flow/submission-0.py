class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_q=deque()
        a_q=deque()
        p_seen=set()
        a_seen=set()
        res=[]
        row=len(heights)
        col=len(heights[0])

        for r in range(row):
            # print(heights[r][0])
            p_seen.add((r,0))
            p_q.append([r,0])

        for c in range(col):
            # print(heights[0][c])
            p_seen.add((0,c))
            p_q.append([0,c])
        
        for r in range(row):
            # print(heights[r][col-1])
            a_seen.add((r,col-1))
            a_q.append([r,col-1])

        for c in range(col):
            # print(heights[row-1][c])
            a_seen.add((row-1,c))
            a_q.append([row-1,c])

        # print(a_q)
        # print(p_q)
        def p_checker(r,c,nr,nc):
            if (nr<0 or nr>=row) or ((nr,nc) in p_seen) or (nc<0 or nc>=col) or (heights[r][c]>heights[nr][nc]):
                return 0
            p_q.append([nr,nc])
            p_seen.add((nr,nc))
        def a_checker(r,c,nr,nc):
            if (nr<0 or nr>=row) or ((nr,nc) in a_seen) or (nc<0 or nc>=col) or (heights[r][c]>heights[nr][nc]):
                return 0
            a_q.append([nr,nc])
            a_seen.add((nr,nc))
        # print(res)
        while p_q:
            r,c=p_q.popleft()
            for nr,nc in [(r+1,c),(r-1,c), (r,c-1), (r,c+1)]:
                p_checker(r,c,nr,nc)
        
        while a_q:
            r,c=a_q.popleft()
            for nr,nc in [(r+1,c),(r-1,c), (r,c-1), (r,c+1)]:
                a_checker(r,c,nr,nc)

        for r in range(row):
            for c in range(col):
                if (r,c) in p_seen and (r,c) in a_seen:
                    res.append([r,c])
        return res
        
