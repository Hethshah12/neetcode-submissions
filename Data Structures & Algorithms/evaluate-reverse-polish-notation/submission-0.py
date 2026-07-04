class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations={"+", "-", "*", "/"}
        st=[]
        res=0
        for tok in tokens:
            if tok not in operations:
                st.append(tok)
            else:
                if st:
                    op2=int(st.pop())
                    op1=int(st.pop())
                    if tok=='+':
                        res=int(op1+op2)
                        st.append(res)
                    elif tok=='-':
                        res=int(op1-op2)
                        st.append(res)
                    elif tok=='/':
                        res=int(op1/op2)
                        st.append(res)
                    elif tok=='*':
                        res=int(op1*op2)
                        st.append(res)
        return int(st[-1])