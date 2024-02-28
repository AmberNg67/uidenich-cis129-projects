# Program to calculate the price for coffee and muffins ordered at a coffee shop.

# Divider line to create sections
# 1.1 Changed shop's name
print("**************************************** \n Amber's Coffee and Muffin Shop \n\n")

# Assigning input values to coffee and muffin
# 1.1 Added tea and scones
coffee = int(input("How many coffees did you order?"))
muffin = int(input("How many muffins did you order?"))
tea = int(input("How many teas did you order?"))
scone = int(input("How many scones did you order?"))

print("****************************************\n\n\n\n****************************************")
print("Amber's Coffee and Muffin Shop Receipt \n\n")

# if statements to determine grammar and calculate total cost per item type
# 1.1 Update to add tea and scones
if coffee == 1:
    print(coffee, "Coffee at $5 each: $", f'{coffee*5.00:.2f}')
if coffee > 1:
    print(coffee, "Coffees at $5 each: $", f'{coffee*5.00:.2f}')
if muffin == 1:
    print(muffin, "Muffin at $4 each: $", f'{muffin*4.00:.2f}')
if muffin > 1:
    print(muffin, "Muffins at $4 each: $", f'{muffin*4.00:.2f}')
if tea == 1:
    print(tea, "Tea at $3 each: $", f'{tea*3.00:.2f}')
if tea > 1:
    print(tea, "Teas at $3 each: $", f'{tea*3.00:.2f}')
if scone == 1:
    print(scone, "Scone at $2 each: $", f'{scone*2.00:.2f}')
if scone > 1:
    print(scone, "Scones at $2 each: $", f'{scone*2.00:.2f}')

# Defining total item costs and tax
# 1.1 Update to add tea and scones
coffee_cost = coffee*5.00
muffin_cost = muffin*4.00
tea_cost = tea*3.00
scone_cost = scone*2.00
tax = 0.06*(coffee_cost + muffin_cost + tea_cost + scone_cost)

# Printing tax and total
#1.1 Added a thank you statement
print("6% tax: $", f'{tax:.2f}')
print("-------------")
print("Total: $", f'{coffee_cost + muffin_cost + tax:.2f}')
print("\n\n    Thank you for coming in. \n You really perked up our day!")
print("****************************************")
