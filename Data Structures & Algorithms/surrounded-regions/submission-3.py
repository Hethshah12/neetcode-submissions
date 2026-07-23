class Solution:
    def solve(self, board: List[List[str]]) -> None:
        border_o=set()
        o_q=deque()
        rows=len(board)
        cols=len(board[0])

        for r in range(rows):
            if board[r][0]=="O":
                o_q.append([r,0])
                

        for r in range(rows):
            if board[r][cols-1]=="O":
                o_q.append([r,cols-1])
                
        for c in range(cols):
            if board[0][c]=="O":
                o_q.append([0,c])
                    
        
        for c in range(cols):
            if board[rows-1][c]=="O":
                o_q.append([rows-1,c])
                

        def x_checker(r,c):
            if(r<0 or r>=rows) or (c<0 or c>=cols) or ((r,c) in border_o) or (board[r][c]=="X"):
                return 0
            border_o.add((r,c))
            x_checker(r+1,c)
            x_checker(r-1,c)
            x_checker(r,c+1)
            x_checker(r,c-1)
        
        while o_q:
            r,c=o_q.popleft()
            x_checker(r,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and ((r,c)) not in border_o:
                    board[r][c]="X"
        