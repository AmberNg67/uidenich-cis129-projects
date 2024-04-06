# CIS129 Module 6 Lab
# Amber Uidenich
# Main Module (using MOD)
# Determine the total number of hot dogs needed

import math

def getTotalHotDogs():
    # Determine the total number of hot dogs needed
    people = 0 # Number of people attending the cookout
    hotdogsPerPerson = 0 # Number of hotdogs that will be served to each person
    people = int(input("How many people will be attending the cookout? "))
    hotdogsPerPerson = int(input("How many hot dogs will you serve each person? "))
    totalDogsNeeded = people * hotdogsPerPerson
    print("You will need", totalDogsNeeded, "hotdogs for the cookout.")
    
    #Determine the minimum number of packages of hotdogs needed
    DOGS = 8 # Number of buns in a package
    minDogsNeeded = math.ceil(totalDogsNeeded / DOGS)
    print("You will need", minDogsNeeded, "packages of hotdogs.")
    
    #Determine the minimum number of packages of buns needed
    BUNS = 10 # Number of buns in a package
    bunsNeeded = totalDogsNeeded # The number of buns needed will equal the number of hotdogs served
    minBunsNeeded = math.ceil(bunsNeeded / BUNS)
    print("You will need", minBunsNeeded, "packages of buns.")
    
    #Determine number of hotdogs left over
    dogsLeft = (DOGS - totalDogsNeeded % DOGS) % DOGS
    print("You will have", dogsLeft, "hotdogs left over.")

    
    #Determine number of buns left over
    bunsLeft = (BUNS - bunsNeeded % BUNS) % BUNS
    print("You will have", bunsLeft, "buns left over.")
    
getTotalHotDogs()
