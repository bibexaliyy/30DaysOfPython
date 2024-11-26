#'Day 2:30 Days of python programming'
#Declaring variables
first_name="Habiba"
Last_name="Isah"
fullname=f"{first_name} {Last_name}"
Country="Nigeria"
City="Jigawa"
Age=24
year=2024
is_married=False
is_true=True
is_light_on=False
a,b,c=2,4,6

#Execises:Level 2
print(type(first_name))
print(type(Last_name))
print(type(fullname))
print(type(Country))
print(type(City))
print(type(Age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#length of first name
print(len(first_name))

#compare the length of first name and last name
print(len(first_name)== len(Last_name))
print(len(first_name)> len(Last_name))
print(len(first_name)< len(Last_name))

#Declaring numbers
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
# Print results
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponentiation:", exp)
print("Floor Division:", floor_division)

#Circle calculation
import math
radius=30
area_of_circle=math.pi * radius ** 2
circum_of_circle=math.pi * radius

# Print results
print("Area of a Circle:", area_of_circle)
print("Circumference of a Circle:", circum_of_circle)

#Taking radius as user input
User_input=float(input("Enter radius: "))
User_area=math.pi * User_input**2
print("Area with user radius:",User_area)

#Using built in functions
first_name=input("enter first name:")
Last_name=input("enter last name:")
Country=input("enter Country:")
Age=input("enter age:")

# Print results
print("First Name:", first_name)
print("Last Name:", Last_name)
print("Country:", Country)
print("Age:", Age)

