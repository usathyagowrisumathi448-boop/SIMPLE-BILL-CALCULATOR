price = float(input("Enter price of the item: "))
quantity = int(input("Enter quantity: "))
subtotal = price * quantity
tax_percent = float(input("Enter tax percentage: "))
tax_amount = (subtotal * tax_percent) / 100
discount_percent = float(input("Enter discount percentage: "))
discount_amount = (subtotal * discount_percent) / 100
total_bill = subtotal + tax_amount - discount_amount
print("\n----- BILL DETAILS -----")
print("Subtotal : Rs.", subtotal)
print("Tax Amount : Rs.", tax_amount)
print("Discount Amount : Rs.", discount_amount)
print("Total Bill : Rs.", total_bill)
