class MinStack:

    def __init__(self):
        self.stk=[]
        self.min_stk=[]

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk:
            self.min_stk.append(val)

        elif self.min_stk[-1]<val:
            #if the new value is greater than the previous one then we need the same val to continue 
            self.min_stk.append(self.min_stk[-1])
        else:
            self.min_stk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()


    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
