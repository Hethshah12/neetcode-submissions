class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp=temperatures
        n=len(temp)
        diff=[0]*n
        st=[]
        #we use enumerate here because we need to return both the values and the index simantaneously
        #both to compare and then to compute the diff in array 

        for i,t in enumerate(temp):
            while st and st[-1][0] < t:
                st_t, st_i= st.pop()
                diff[st_i]=i - st_i
            
            st.append((t,i))
        return diff