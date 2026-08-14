class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed=[0]+flowerbed+[0]
        if n==0:
            return True
        for i in range(1,len(bed)-1):
            if bed[i-1]==0 and bed[i]==0 and bed[i+1]==0:
                bed[i]=1
                n-=1
                if n==0:
                    return True
        return True if n==0 else False
    
                
        
