def UserInput():
    l=[]
    while True:
        inp=input("Enter an input: ")
        if inp=="Done":return l,True
        if not (inp.isnumeric() and int(inp)>=0):
            return l,False
        l.append(int(inp))

def SumOut(l):
    return sum(l)
def MinOut(l):
    return min(l)  
def MaxOut(l):
    return max(l)     



xList,isValid = UserInput()
if isValid:
    print()
    print(f'The summation is {SumOut(xList)}')
    print(f'The minimum is {MinOut(xList)}')
    print(f'The maximum is {MaxOut(xList)}')
else:
    print("Error")
    


