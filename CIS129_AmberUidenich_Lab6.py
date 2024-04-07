# Amber Uidenich
# CIS129 Module 6 Lab
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
    return totalDogsNeeded
    
    #Determine the minimum number of packages of hotdogs needed

def showResults(dogsLeft, minDogs, bunsLeft, minBuns):
    print("You will need", minDogs, "packages of hotdogs.")
    print("You will need", minBuns, "packages of buns.")
    print("You will have", dogsLeft, "hotdogs left over.")
    print("You will have", bunsLeft, "buns left over.")
    

# Main Module

# Local variable for the total number of hot dogs needed.
total = 0

# Input --------------------------------------
# Get the total number of hot dogs needed.
total = getTotalHotDogs()

# Processing ----------------------------------
# Named constants for the package sizes
DOGS = 10   # Hot dogs in a package
BUNS = 8    # Hot dog buns in a package

# Local variables
dogsLeft = 0  # Left over hot dogs
bunsLeft = 0 # Left over hot dog buns
minDogs = 0  # Minimum packages of hot dogs
minBuns = 0  # Minimum packages of hot dog buns

# Calculate the number of left over hot dogs.
dogsLeft = (DOGS - total % DOGS) % DOGS

# Calculate the minimum number of packages of hot dogs.
minDogs = math.ceil(total / DOGS)

# Calculate the number of left over hot dog buns.
bunsLeft = (BUNS - total % BUNS) % BUNS

# Calculate the minimum number of packages of hot dogs buns.
minBuns = math.ceil(total / BUNS)

# Output ----------------------------------------
# Display the results.
showResults(dogsLeft, minDogs, bunsLeft, minBuns)
