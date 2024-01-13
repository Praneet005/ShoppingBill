def calculate_bill(items):
    total = 0

    print("\n*** Shopping Bill ***\n")
    print("{:<15} {:<10} {:<10} {:<10}".format("Item", "Price", "Quantity", "Total"))

    for item, details in items.items():
        price = details['price']
        quantity = details['quantity']
        item_total = price * quantity
        total += item_total

        print("{:<15} ₹{:<10.2f} {:<10} ₹{:<10.2f}".format(item, price, quantity, item_total))

    print("\nTotal Bill: ₹{:.2f}\n".format(total))


def main():
    items = {}

    while True:
        item_name = input("Enter item name (or '' to finish): ").strip().lower()

        if item_name == '':
            break

        price = float(input("Enter the price per unit: "))
        quantity = int(input("Enter the quantity: "))

        items[item_name] = {'price': price, 'quantity': quantity}

    calculate_bill(items)


if __name__ == "__main__":
    main()
