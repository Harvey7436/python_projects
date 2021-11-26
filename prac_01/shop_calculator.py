total_price = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number")
    number = int(input("Number of items: "))
for n in range(number):
    price = float(input("Enter Price of Item:"))
    total_price += price
if total_price > 100:
    total_price *= 0.9
    print("Number of items is", number, f" The total price is{total_price:.2f}")
else:
    print("Number of items is", number, f" The total price is{total_price:.2f}")
