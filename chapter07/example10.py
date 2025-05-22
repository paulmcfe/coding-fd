import my_module

counter = 0

while (counter < 3):
    # Get the price
    price = float(input("Enter the price: "))

    # Get the total with tax and shipping
    total = my_module.calculate_total(price)

    print(f"Total with tax and shipping: ${total:.2f}")

    counter += 1