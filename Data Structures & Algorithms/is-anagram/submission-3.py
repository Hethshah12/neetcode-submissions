class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        # s=sorted(s)
        # t=sorted(t)
        # #now the strings are immutable so we cannot use s.sort(), always use sorted(s)
        # #they return a list 
        # for i in range(len(s)):
        #     if s[i]!=t[i]:
        #         return False
        # return True

        #faster method with o(n) complexity
        # if len(s)!=len(t):
        #     return False 
        # s_h=dict()
        # t_h=dict()
        # for ch in s:
        #     s_h[ch] = s_h.get(ch,0)+1

        # for ch in t:
        #     t_h[ch] = t_h.get(ch,0)+1

        # return s_h==t_h
        

        #shortest answer would be (always use C not 'c')
        return Counter(s)==Counter(t)
        