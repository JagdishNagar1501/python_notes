"""
Create a program in which the user types 5 car names as input and shows the 
car's name at end of program.
"""

# Solution

print("Car name display program")
car_name=[]  # Create a empty list

# For 5 input we will use for loop.
for i in range(1, 6):
    # This sentax use to take input from users
    a = input("Enter the car: ")
    # We use append inbuilt function to store car's name to car_name list.
    car_name.append(a)

print("-------------------------------------")
print("------------ Car's Name -------------")
# Display all car's name
for i in car_name:
    # To print one by one car's name
    print(i)
