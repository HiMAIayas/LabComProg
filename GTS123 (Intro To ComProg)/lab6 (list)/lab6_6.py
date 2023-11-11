date=input("Enter dd/mm/yy: ")

day = date[0:2]
month = int(date[2:4])
year = int(date[4:])

if len(date)==8:
    if month>12:print("Error! There are 12 months.")
    else:
        print(f"Date = {day}")
        print(f"Month = {month}")
        print(f"Year = {year-543}")
        
else:
    print("Please enter 8 digits!!!")