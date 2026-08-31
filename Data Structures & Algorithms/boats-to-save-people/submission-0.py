class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i,j,boats=0,len(people)-1, 0

        while i<=j:
            if people[i]+people[j]<=limit:
                boats+=1
                j-=1
                i+=1
            else:
                j-=1
                boats+=1
        return boats
