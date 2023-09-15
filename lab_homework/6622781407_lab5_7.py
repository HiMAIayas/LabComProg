store={"L":0,"S":0,"H":0}

for i in range(10):
    feel=input('Feeling Like ("L"), Sad ("S"), and Heart("H")?')
    if feel not in ["L","S","H"]:print("Invalid input, accepts only (L/S/H).")
    else:store[feel]+=1
    
total=store["L"]+store["S"]+store["H"]
print(f"============\nTotal is {total}\n============")
print(f'Like: {store["L"]/total*100:.2f}%')
print(f'Sad: {store["S"]/total*100:.2f}%')
print(f'Heart: {store["H"]/total*100:.2f}%')