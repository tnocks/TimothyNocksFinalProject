#Timothy Nocks Final Project
#Website advertising a Tavern, with an ordering service

#test output for the closing and opening times
print("Hours Mon-Thurs: ")
print("12-9pm")
print("Hours Fri and Sat: ")
print("12-11pm")
print("Hours Sun: ")
print("10am-7pm")

#ordering system
def get_order():
    
    print("Menu:")
    print("1. Cheeseburger Dinner- $10")
    print("2. Fried Chicken Dinner- $12")
    print("3. Porkchop Dinner- $11")
    print("4. Fish Dinner- $14")
    print("5. Pasta Dinner- $13")
    print("All dinners come with a choice of side (Fries, Tater Tots, or Onion Rings)")

    while True:
        order = int(input("What would you like to order? (Please enter 1-5 to choose your order)"))   