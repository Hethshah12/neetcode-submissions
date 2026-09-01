class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt=0
        ksum=sum(arr[:k])
        cnt=1 if ksum>=threshold*k else 0
        for j in range(k,len(arr)):
            ksum+=arr[j]-arr[j-k]
            if (ksum)>=threshold*k:
                cnt+=1
        return cnt
        # for i in range(len(arr)-k+1):
        #     if (sum(arr[i:i+k-1]))/k >threshold:
        #         cnt+=1
        # return cnt

