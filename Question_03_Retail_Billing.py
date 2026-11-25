
n = int(input("Enter number of products: "))

items = []
subtotal = 0
total_tax = 0

for i in range(n):
    print("\nEnter details of product", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (electronics/clothing/grocery): ").lower()

    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity

    if category == "electronics":
        tax_rate = 18
    elif category == "clothing":
        tax_rate = 5
    else:
        tax_rate = 0

    tax = amount * tax_rate / 100

    subtotal = subtotal + amount
    total_tax = total_tax + tax

    items.append((name, quantity, amount, tax))

if subtotal >= 5000:
    discount = subtotal * 0.10
elif subtotal >= 2000:
    discount = subtotal * 0.05
else:
    discount = 0

if discount > 1000:
    discount = 1000

grand_total = subtotal + total_tax - discount

print("\n--------- RETAIL INVOICE ---------")

for item in items:
    print("Product:", item[0])
    print("Quantity:", item[1])
    print("Amount: Rs.", item[2])
    print("Tax: Rs.", item[3])
    print("--------------------------------")

print("Subtotal: Rs.", subtotal)
print("Total Tax: Rs.", total_tax)
print("Discount: Rs.", discount)
print("Final Bill: Rs.", grand_total)

print("---------------------------------")
