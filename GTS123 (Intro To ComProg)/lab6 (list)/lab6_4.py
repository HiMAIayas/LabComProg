namelist= ["Satawat","Pisit","Thanapong","Pished","Nut","Amon"]

while True:
    nameInp = input("Please enter a student's name that you want to delete (q = exit): ")
    if nameInp=="q":break
    print(f"You will remove '{nameInp}' from this class.")
    isConferm = input("Please (conferm: 'y', cancel: 'n'):")
    if isConferm=="y":
        namelist.remove(nameInp)
    print(namelist)
    print()