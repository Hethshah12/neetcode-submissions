class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t)
        best_l, best_len=0, float('inf')
        required=len(need)
        formed=0
        window, left={}, 0

        for right ,c in enumerate(s):
            window[c]= 1+window.get(c,0)
            if c in need and window[c]==need[c]:
                formed+=1

            while formed==required:
                if right-left+1<best_len:
                    best_len=right-left+1
                    best_l=left

                d=s[left]

                if d in need and window[d]==need[d]:
                    formed-=1
                window[d]-=1
                left+=1
        return "" if best_len==float('inf') else s[best_l:best_l+best_len]
