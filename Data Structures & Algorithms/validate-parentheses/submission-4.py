class Solution:
    def isValid(self, s: str) -> bool:
        pair={'}':'{',']':'[', ')':'('}
        stk=[]
        for c in s:
            if c not in pair:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped=stk.pop()
                    if popped!=pair[c]:
                        return False
        return not stk