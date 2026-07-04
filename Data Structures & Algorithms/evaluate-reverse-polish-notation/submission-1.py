class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations={"+", "-", "*", "/"}
        st=[]
        for tok in tokens:
            if tok not in operations:
                st.append(tok)
            else:
                if st:
                    op2=int(st.pop())
                    op1=int(st.pop())
                    if tok=='+':
                        st.append(op1+op2)
                    elif tok=='-':
                        
                        st.append(op1-op2)
                    elif tok=='/':
                        
                        st.append(op1/op2)
                    elif tok=='*':
            
                        st.append(op1*op2)
        return int(st[-1])