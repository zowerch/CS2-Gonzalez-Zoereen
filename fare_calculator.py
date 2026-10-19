#Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ")
while name == "":
    print("Name cannot be empty!")
    name = input("Enter passenger name: ")
    

distance = float(input("Enter distance (km): "))
while distance <= 0:
    print("Distance must be greater than 0!")
    distance = float(input("Enter distance (km): "))
 

passengers = int(input("Enter number of passengers: "))
while passengers <= 0:
    print("Please enter a positive whole number!")
    passengers = float(input("Enter number of passengers: "))


total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number
