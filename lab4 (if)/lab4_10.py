inc=float(input("Welcome to tax computation program\nPlease enter your income: "))
if inc<0:print("You are in dept")
elif inc<=15000: print("Tax expense:",0,"\nYour net income after tax:",inc)
elif inc<=50000: print("Tax expense:",(inc-15000)*0.05,"\nYour net income after tax:",inc-((inc-15000)*0.05))
elif inc<=100000: print("Tax expense:",(inc-50000)*0.075+(35000*0.05),"\nYour net income after tax:",inc-((inc-50000)*0.075+(35000*0.05)))
else: print("Tax expense:",(inc-100000)*0.1+(35000*0.05)+(50000*0.075),"\nYour net income after tax:",inc-((inc-100000)*0.1+(35000*0.05)+(50000*0.075)))
#อันนี้เน้นบรรทัดน้อย อย่าหาทำเลยนะ;-;
