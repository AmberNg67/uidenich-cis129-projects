#Amber Uidenich
# CIS 129 Lab 7: Theater Seating Lab
# Section A 300 seats at $20
# Section B 500 seats at $15
# Section C 200 seats at $10
# Collect number of tickets sold per section
# Validate number is legitimate for the section
# Calculate to total sale (numberA*20 + numberB*15 + numberC*10)
# Need subtotals after each section
# Display total and each section seats sold and subtotal

def main():

    sectionA = 300
    sectionB = 500
    sectionC = 200
    
    
    print("Welcome to Dramatic Theater!")
    print("We have",(sectionA),"seats availabe in Section A,",(sectionB),"seats availabe in Section B, and",(sectionC),"seats availabe in Section C.")
    print()
    
    subtotal()

    
def subtotal():
    subtotalA = 0
    numberA = 0
        
    
    numberA = int(input("How many seats were sold in Section A? "))
    while numberA > 300:
        numberA = int(input("How many seats were sold in Section A? "))
    
    else:
        subtotalA = numberA * 20
    
    print("Subtotal for Section A: $", subtotalA)
    

    subtotalB = 0
    numberB = 0
    
    print()
    numberB = int(input("How many seats were sold in Section B? "))
    while  numberB > 500:
        numberB = int(input("How many seats were sold in Section B? "))
    else:
        subtotalB = numberB * 15
   
    print("Subtotal for Sections A and B: $", subtotalB + subtotalA)   
    
        
    subtotalC = 0
    numberC = 0
    
    print()    
    numberC = int(input("How many seats were sold in Section C? "))
    while numberC > 200:
        numberC = int(input("How many seats were sold in Section C? "))
        
    else:
        subtotalC = numberC * 10
        
    print("Subtotal for Section A, B and C: $", subtotalC + subtotalB + subtotalA)
    print()
    print( "You have purchased:")
    if numberA == 1:
        print("", numberA, "seat in Section A for $", subtotalA)
             
    else:
        print("", numberA, "seats in Section A for $", subtotalA)
   
    if numberB == 1:
        print("", numberB, "seat in Section B for $", subtotalB)
             
    else:
        print("", numberB, "seats in Section B for $", subtotalB)
        
    if numberC == 1:
        print("", numberC, "seat in Section C for $", subtotalC)
             
    else:
        print("", numberC, "seats in Section C for $", subtotalC)
        
    
    print("    Your total cost is: $",subtotalC + subtotalB + subtotalA) 

    # Can I get them to align? I can add a space before seat to adjust for that, but what if there are different digits sold?
    
    return subtotalA
    return subtotalB
    return subtotalC


main()  
