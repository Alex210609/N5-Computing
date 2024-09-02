# Code using 1d array
#30.08.2024
#Alex Blyth

travel_agent = []
booking_number = []
dates = []

for index in range(3) :
    travelagent = input("Enter travel agent")
    bookingnumber = int(input("Enter booking number"))
    date = input("Enter date")
    travel_agent.append(travelagent)
    booking_number.append(bookingnumber)
    dates.append(date)

print(travel_agent)
print(booking_number)
print(dates)
