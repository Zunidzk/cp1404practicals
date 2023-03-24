import math

items = int(input("Number of items: "))
list_items = []
for i in range(items):
    price = float(input('the price of item: '))
    list_items.append(price)
total = math.fsum(list_items)
if total > 100:
    total = total - (total * 0.1)
print(f'Total price for {items} items is ${total}')
