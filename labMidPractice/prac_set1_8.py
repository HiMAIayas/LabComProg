fir = input("Give me a character: ")
sec = input("Give me another character: ")
if fir.isalpha() and sec.isalpha():
    al = "abcdefghijklmnopqrstuvwxyz"
    i1 = al.find(fir)
    i2 = al.find(sec)
    print(al[min(i1,i2):max(i1,i2)+1])
    
else:print("You need to input two characters.")