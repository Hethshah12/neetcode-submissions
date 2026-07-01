class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return True
#for c in s it will take only the charchters that are alphabets, all the special char will be ignored 
#apart from that they will also be lowered and join will help us glue them together
        news="".join(c.lower() for c in s if c.isalnum())
        i,j=0, len(news)-1 #two pointer approach where we  will iterate from front and back
        while i<j:
            if news[i]!=news[j]:
                return False 
            j-=1
            i+=1
        return True