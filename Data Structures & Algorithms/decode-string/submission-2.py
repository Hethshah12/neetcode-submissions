class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        for i in range(len(s)):
            if s[i]!=']':
                st.append(s[i])
            else:
                substr=""
                while st[-1]!='[': #until the top of the stack is a opening bracket keep popping
                    substr=st.pop()+substr
                st.pop() #to remove the last bracket
                k="" #before the bracket we would have some number now if it is a two digit we gotta keep on popping if it is a 2 digit num
                while st and st[-1].isdigit():
                    k=st.pop()+k

                st.append(int(k)*substr)
        return "".join(st)
