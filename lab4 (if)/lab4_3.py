day=int(input("Input number of days: "))
hrs=int(input("Input number of hours: "))
method=input("Please select a choice:\n1-to calculate the total number of seconds or\n2-to calculate the total number of minutes\nEnter your selected choice: ")
if method=="1":
    ans=(day*24+hrs)*3600
    print(f"The total numbber of seconds are {ans}.")
elif method=="2":
    ans=(day*24+hrs)*60
    print(f"The total numbber of minutes are {ans}.")
