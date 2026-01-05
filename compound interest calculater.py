# python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Principle: "))
    if principle < 0:
        print("Principle is negative")
    else:
        break

while True:
    rate = float(input("Rate: "))
    if rate < 0:
        print("Rate is negative")
    else:
        break

while True:
    time = float(input("Time: "))
    if time < 0:
        print("Time is negative")
    else:
        break

amount = principle * pow((1 + rate / 100),time)
print(f"Amount : {amount}")