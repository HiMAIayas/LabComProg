def UserInput():
    w=float(input("Input your weight (kilogram): "))
    h=float(input("Input your height (meter): "))
    return w,h

def FindBMI(hh,ww):
    UserBMI = ww/hh**2
    return UserBMI

def showBMI(MyBMI):
    print(f"The user BMI is {MyBMI:.2f}")

ww,hh=UserInput()
UserBMI=FindBMI(hh,ww)
showBMI(UserBMI)
