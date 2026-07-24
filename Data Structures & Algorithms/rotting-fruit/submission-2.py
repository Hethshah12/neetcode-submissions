class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # rows=len(grid)
        # cols=len(grid[0])
        # coll=[0,1,2]
        # seen=set()
        # target=coll[2]
        # q=deque()
        # fresh=[0]
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c]==1:
        #             fresh[0]+=1
        #         if grid[r][c]==2:
        #             q.append([r,c])
        #             # print(q)
        # def check(nr,nc):
        #     nonlocal fresh
        #     if not(0<=nr <rows and 0 <=nc<cols) or ((nr,nc) in seen):
        #         return
        #     if(grid[nr][nc]!=1):
        #         return
        #     seen.add((nr,nc))
        #     q.append([nr,nc])

        #     grid[nr][nc]=2
        #     fresh[0]-=1



        # minn=[0]
        # while q and fresh[0]>0:
        #     for _ in range(len(q)):
        #         r,c=q.popleft()
        #         for nr,nc in [(r+1,c), (r-1,c), (r,c-1), (r,c+1)]:
                
        #             check(nr,nc)
        #     minn[0]+=1
        # return minn[0] if fresh[0]==0 else -1

        rows=len(grid)
        cols=len(grid[0])
        fresh=[0]
        minn=[0]
        q=deque()
        seen=set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh[0]+=1
                if grid[r][c]==2:
                    q.append([r,c])
        
        while q and fresh[0]>0:
            for _ in range(len(q)): #basically for every iteration of element appended and popped in the queue
                r,c=q.popleft()
                for nr,nc in [(r+1,c), (r-1,c), (r,c-1), (r,c+1)]:
                    if (nr<0 or nr>=rows) or (nc<0 or nc>=cols) or ((nr,nc) in seen):
                        continue
                    if (grid[nr][nc]!=1):
                        continue
                    seen.add((nr,nc))
                    q.append([nr,nc])

                    fresh[0]-=1
                    grid[nr][nc]=2
            minn[0]+=1
        return minn[0] if fresh[0]==0 else -1
            
            
                    

