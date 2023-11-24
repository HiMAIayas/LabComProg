while True:
    line = input("Enter three values (or 'DONE' to exit): ")
    if line=="DONE":break
    try:
        a,b,c = [float(i) for i in line.split(',')]
        if a<=0 or b<=0 or c<=0:raise Exception
        
        print(f'Values: {a:.4f} : {b:.4f} : {c:.4f}')
        total = a+b+c
        print(f'Proportion: {a*100/total:.4f}% : {b*100/total:.4f}% : {c*100/total:.4f}%')
    except:
        print("Incorrect input, try again!")
        continue
    
print("Exitting the program. Thank you!")