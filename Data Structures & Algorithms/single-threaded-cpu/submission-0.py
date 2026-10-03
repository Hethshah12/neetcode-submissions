class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n=len(tasks)
        arr=[]
        for i in range(n):
            arr.append((tasks[i][0], tasks[i][1], i))
        arr.sort()
        # print(arr)
        avail, res, time, p=[], [], 0, 0
        while len(res)<n:
            if not avail and time<arr[p][0]:
                time=arr[p][0]
            while p<n and arr[p][0]<=time:
                enq, proc, i=arr[p]
                heapq.heappush(avail, (proc, i))
                p+=1
            proc, i=heapq.heappop(avail)
            time+=proc
            res.append(i)
        return res

    