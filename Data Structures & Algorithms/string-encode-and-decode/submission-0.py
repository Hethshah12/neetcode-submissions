class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str=""
        for word in strs:
            enc_str+=str(len(word))+"#"+word
        return enc_str
        

    def decode(self, s: str) -> List[str]:
        res=[]  #empty list to store decoded string 
        i=0 #keep a i pointer to check such that i does not exceed the length of s
        while i<len(s):
            j=i #another pointer to scan further than i so that, we can know what is coming up
            while s[j]!="#": #check till j reaches a # , because we want to kow length first and it might be 2 digit also 
                j+=1 #increase the j pointer incase it is two digit it will increase until # is found 
#mow our length will be equal to from where i starts initially that is 0 and then till where j discovers #
#all of this will help us determine how long the string is , currently j is poiniting to #

            length=int(s[i:j]) 
#now in order to trace word , we need to do j+1, so that 3#<-(j)Rat points to the R
#now j is pointing to R and length says word is 3 letters long , so we can write j+1+length as stop val

            word=s[j+1 : j+1+length]

#after discovering the word append it and then increment i to the point before the next number and while loop continues as such 

            res.append(word)
            i=j+1+length
        return res
