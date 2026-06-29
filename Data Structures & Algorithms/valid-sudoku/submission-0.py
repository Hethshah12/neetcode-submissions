class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #for columns
        for i in range(9):
            s=set() #creating an empty set for every column so that we have a track of things in each column 
            for j in range(9):
                item=board[j][i] #reverse i and j to traverse through columns 
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
        #for rows
        for i in range(9):
            s=set()
            for j in range(9):
                item=board[i][j]  #traverse through rows proeprly 
                if item in s:
                    return False
                elif item != '.': #if the item is anything else but period and has come to elif after checking no duplicates then add to set 
                    s.add(item)

        #for boxes 
        for boxes_row in range(0,9,3):
            for boxes_col in range(0,9,3):
                s=set()
                for i in range(boxes_row, boxes_row+3):
                    for j in range(boxes_col, boxes_col+3):
                        item=board[i][j]
                        if item in s:
                            return False
                        elif item != ".":
                            s.add(item)
        return True