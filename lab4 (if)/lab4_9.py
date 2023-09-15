time=int(input("Input parking time (minutes): "))
if (time%60)>15:time+=60
print(f"The charge is {(time//60)*20} baht.")