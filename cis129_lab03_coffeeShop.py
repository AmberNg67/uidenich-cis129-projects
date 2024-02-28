# Program to calculate the price for coffee and muffins ordered at a coffee shop.

# Divider line to create sections
print("**************************************** \n My Coffee and Muffin Shop")

# Assigning input values to coffee and muffin
coffee = int(input("How many coffees did you order?\n"))
muffin = int(input("How many muffins did you order?\n"))

print("****************************************\n\n****************************************")
print("My Coffee and Muffin Shop Receipt")

# if statements to determine grammar and calculate total cost per item type
if coffee == 1:
    print(coffee, "Coffee at $5 each: $", f'{coffee*5.00:.2f}')
if coffee > 1:
    print(coffee, "Coffees at $5 each: $", f'{coffee*5.00:.2f}')
if muffin == 1:
    print(muffin, "Muffin at $4 each: $", f'{muffin*4.00:.2f}')
if muffin > 1:
    print(muffin, "Muffins at $4 each: $", f'{muffin*4.00:.2f}')

# Defining total item costs and tax
coffee_cost = coffee*5.00
muffin_cost = muffin*4.00
tax = 0.06*(coffee_cost + muffin_cost)

# Printing tax and total
print("6% tax: $", f'{tax:.2f}')
print("-------------")
print("Total: $", f'{coffee_cost + muffin_cost + tax:.2f}')
print("****************************************")
