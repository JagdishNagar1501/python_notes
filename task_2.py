
"""Create a program in which the user store 5 car names as input.
Perform task: 
        a.  Show first all cars name
        b.  Add one more car name into given list and show
        c.  Remove “maruti” car from list
"""

# Solution

print("Car name display program")

# For 5 input we will use for loop.
car_name=['Bmw' , 'Porsche' , 'Ford' , 'Maruti' , 'Honda']  

print("-------------------------------------")
print("------------ Car's Name -------------")
# Display all car's name
for i in car_name:
    # To print one by one car's name
    print(i)

print("-------------------------------------")

print("Remove “Maruti” car from list")
car_name.remove("Maruti")

for i in car_name:
    # To print one by one car's name
    print(i)
