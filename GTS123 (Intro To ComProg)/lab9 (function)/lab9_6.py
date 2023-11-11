def CelsiusToFahrenheit(c):
    return c*9/5 + 32

cel=float(input("Input temperature in degree Celcius: "))
print("%.2f"%CelsiusToFahrenheit(cel))