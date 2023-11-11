import random

l=[]
for i in range(4):
    inp=input(f"Enter string#{i+1}: ")
    l.append(inp)
    
random.shuffle(l)
ans=" ".join(l)
print(f"Random order of sequence: {ans}")