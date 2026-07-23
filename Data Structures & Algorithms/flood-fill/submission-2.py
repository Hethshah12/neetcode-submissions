class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows=len(image)
        cols=len(image[0])

        target=image[sr][sc]

        q=deque()
        q.append([sr,sc])
        seen=set()
        seen.add((sr,sc))
        image[sr][sc]=color
        
        def flood(r,c, target):
            if(r<0 or r>rows-1) or (c<0 or c>cols-1) or ((r,c) in seen) or ((image[r][c]!=target)):
                return 0
            seen.add((r,c))
            q.append([r,c])
            image[r][c]=color
            flood(r+1,c, target)
            flood(r-1,c, target)
            flood(r,c-1,target)
            flood(r,c+1,target)
            
        
        while q:
            r,c=q.popleft()
            for nr, nc in [(r-1,c), (r+1,c), (r,c+1), (r,c-1)]:
                flood(nr,nc,target)
        return image
