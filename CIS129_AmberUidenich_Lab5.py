# Amber Uidenich
# March 27, 2024
# This program will collect data about the number of bottles retutned to a store per day/
# keep track of the total bottles returned during one week/
# calculate to amount paid out during the week (each bottle earns .10)

# Convert from camelCase to snake_case (I don't know how to do this)


# Define Variables (Initialize phase)

totalBottles = 0
totalPayout = 0 
counter = 1                                                               
keepGoing = "y"
prompt1 = ("Number of bottles collected today: ")
prompt2 = ("Do you want to enter another week’s worth of data?, Enter y or n: ")


# Data Collection and Calculation Loop (Processing Phase)

while keepGoing == "y" and counter <= 7:
    todayBottles = int(input(prompt1))
    totalBottles += todayBottles #pretty sure this is not how to handle this
    totalPayout = totalBottles * 0.10 #maybe I will need to so something here because it is a float
    keepGoing = str(input(prompt2))
    counter += 1

# Output of data (Termination Phase)

print("Number of bottles collected: ", (totalBottles))
print(f"Total Payout: ${totalPayout:.2f}")
