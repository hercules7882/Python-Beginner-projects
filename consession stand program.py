# concession stand program

menu = {"pizza":5.0,
        "nacho":3.0,
        "chicken":2.0,
        "popcorn":4.0,
        "fries":2.0,
        "coke":4.0,
        "chips":3.0}

cart =[]
total = 0
print("--------------MENU----------------")
for key,value in menu.items():
    print(f"{key:10}: ${value: .2f}")
print("----------------------------------")

while True:
    food = input("Select an Item( q to quit ): ").lower()
    if food == "q":
        break

    elif menu.get(food) is not None:
        cart.append(food)

print("---------YOUR ORDER---------")
for food in cart:
    total += menu.get(food)
    print(food, end = " ")

print()
print(f"your total is ${total: .2f}")