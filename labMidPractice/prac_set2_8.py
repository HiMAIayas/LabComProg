n = input("Input: ")
if not n.isnumeric():print("Your input is invalid.")
else:
    n=int(n)
    if n<3:print("Your input is invalid.")
    else:
        
        for i in range(1,n+1): #print the upper part
            if i%2==1:print("*" + "0*"*int((i-1)/2) + " "*((n-i)*2) + "*0"*int((i-1)/2) + "*")
            else:print("*0"*int(i/2) + " "*((n-i)*2) + "0*"*int(i/2))
                
        for i in range(n-1,0,-1): #print the lower part
            if i%2==1:print("*" + "0*"*int((i-1)/2) + " "*((n-i)*2) + "*0"*int((i-1)/2) + "*")
            else:print("*0"*int(i/2) + " "*((n-i)*2) + "0*"*int(i/2))