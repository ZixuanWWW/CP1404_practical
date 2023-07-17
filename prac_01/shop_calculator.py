DISCOUNT_PRICE = 100
DISCOUNT_RATE = 0.9
def shop_calculator():
    total = 0
    num_items = int(input("Number of items: "))
    while num_items < 0:
        print("Invalid number of items")
        num_items = int(input("Number of items: "))
    for i in range(num_items):
        price = float(input("Price of item: "))
        total += price
    if total > DISCOUNT_PRICE:
        total *= DISCOUNT_RATE
    print(f"Total price for {num_items} items is ${total:.2f}")

shop_calculator()
