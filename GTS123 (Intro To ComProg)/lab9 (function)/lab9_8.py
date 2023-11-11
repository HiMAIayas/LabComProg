def myRange(FirstVal, UpperBound, StepSize):
    arr=[]
    if StepSize<0:
        while FirstVal>UpperBound:
            arr.append(FirstVal)
            FirstVal+=StepSize
    else:
        while FirstVal<UpperBound:
            arr.append(FirstVal)
            FirstVal+=StepSize
    return arr




begin=int(input("Enter the first number: "))
end=int(input("Enter the upper bound: "))
step=int(input("Enter the step: "))
print("Range =",myRange(begin,end,step))

