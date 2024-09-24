combined_total = 0

number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))


for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    combined_total += item_price

if combined_total >= 100:
    total_price = combined_total - combined_total * 0.1
else:
    total_price = combined_total
print(f"Total price for {number_of_items} is ${total_price:.2f}")