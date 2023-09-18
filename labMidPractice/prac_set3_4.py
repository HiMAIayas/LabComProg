def printline(start,max,step):
    string=""
    for i in range(max):
        if start<1:start=max
        elif start>max:start=1
        string+=str(start)
        start+=step
    return string

w,h = input("Input: ").split()
if w.isnumeric() and h.isnumeric() and 10>int(w)>0 and 10>int(h)>0:
    w,h=int(w),int(h)
    inc = 1
    dec = w
    for i in range(h):
        if i%2==0:
            print(printline(inc,w,1))
            inc+=1
        else:
            print(printline(dec,w,-1))
            dec-=1
else:print("Invalid input")