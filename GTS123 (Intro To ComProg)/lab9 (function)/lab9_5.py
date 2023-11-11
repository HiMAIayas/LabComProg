def SeatType():
    while True:
        seat = input("Select the seat type (P or D or H): ")
        if seat in ["P","D","H"]:return seat
        else:print("Wrong seat type! Please select again")

def MovieType():
    while True:
        movie=input("Select the movie type (1 or 2): ")
        if movie in ["1","2"]:return int(movie)
        else:print("Wrong movie type! Please select again")

def TicketPrice(seat,movie):
    table={
        "P":[100,120],
        "D":[140,200],
        "H":[400,500]
    }
    price=table[seat][movie-1]
    return price

seat=SeatType()
movie=MovieType()
print(f"\nThe ticket price is {TicketPrice(seat,movie)}")

    
        