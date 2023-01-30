BOOKINGS_FILE = open("bookings.txt", "a")

def makeBooking():
    name = input("Please enter booking name: ")
    movie = input("Please enter movie name: ")
    seats = int(input("Please enter number of seats: "))
    vip = input("VIP seats? true or false: ")
    booking_str = f"Name: {name}  movie: {movie}  seats: {seats}  vip: {vip}\n"
    return booking_str

booking = True

while booking:
    BOOKINGS_FILE.write(makeBooking())
    choice = input("Do you want to keep adding orders? Y / N: ") 
    if choice.lower() == "n":
        booking = False
    else:
        booking = True

# BOOKINGS_FILE.write(makeBooking())

BOOKINGS_FILE.close()

