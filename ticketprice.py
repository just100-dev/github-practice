age = int(input("Enter your Age:"))

if age <= 2:
    print("Ticket Price: Free")
elif 3 <= age <= 12:
    print("ticket price: $10")
elif 13 <= age <= 65:
    print("Ticket Price: $15")
else:
    print("Ticket Price: $10")