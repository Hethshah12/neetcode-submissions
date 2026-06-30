class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s=sorted(s)
        t=sorted(t)
        #now the strings are immutable so we cannot use s.sort(), always use sorted(s)
        #they return a list 
        for i in range(len(s)):
            if s[i]!=t[i]:
                return False
        return True

        