Age=28
height=5.8
complex_number=4+3j

#calculating area of a triangle by prompting user
base=float(input("enter base :"))
height=float(input("enter height :"))
area_of_triangle = 0.5 * base * height
#print("The area of a triangle is" ,area_of_triangle)  
print(f"The area of the triangle is {int(area_of_triangle)}")    

#writing a script that prompt the user to write sides
a=float(input("enter side a:"))
b=float(input("enter side b:"))
c=float(input("enter side c:"))
perimeter = a + b + c
print(f"The perimeter of the triangle is {int(perimeter)}")
#CALCULATING AREA OF A RECTANGLLE
length=float(input("Enter the length of the rectangle:"))
width=float(input("Enter the width of the rectangle:"))
#calculating area and perimeter
area=length*width
perimeter=2*(length+width)
#printing the results
print(f"The area of the rectabgle is {area}")
print(f"The preimeter of the rectangle is {perimeter}")
#Area and circumfrence of a circle
pi=3.14
r= float(input("Enter the radius of a circle :"))
#Calculate the area and circumfrence 
area = pi * r *r
circumfrence = 2* pi *r

# Output results
print(f"The area of the circle is {area}")
print(f"The circumference of the circle is {circumfrence}")
#calculating the slope and euclean distance
slope=2
x_intercepts=-(-2)/2                 #x_intercepts is found when y=0
y_intercepts=-2                      #y_intercepts is found when x= 0

#print the outputs 
print(f"slope: {slope}")
print(f"x_intercepts:{x_intercepts}")
print(f"y_intercepts:{y_intercepts}")

#SLOPE AMD INTERCEPTS
import math
#dEFIBE POINTS
x1, y1 = 2, 2
x2, y2 = 6, 10
#calculate slope
slope=(y2-y1)/(x2-x1)
#calculate the eucledean distance
eucledean_distance = math.sqrt((x2 -x1) ** 2 + (y2 - y1)**2)
print(f"slope:{slope}")
print(f"eucledean_distance:{eucledean_distance}")

#Comparing the slopes from task 8 and 9
slope_1=2            #slope from y=2x-2
slope_2=(10-2)/(6-2)     #slope from two points
#output comparisons
if slope_1 == slope_2:
    print("The slopes are the same.")
else:
    print("The slopes are different.")
#finding the values of x when x = 0
#define the equation       y = x^2+6x + 9
for x in range (-10,10):     #trying different values of x
    y=x**2 +6*x + 9
    if y==0:
        print(f"y is o when x is:{x}")   #y is 0 when x is -3
#lemgths
len_python=len("python") 
len_dragon=len("dragon")  
#Falsy comparion statement 
falsy_statement = len_python !=len_dragon

#Output results
print(f"Length of 'python':{len_python}")
print(f"Length of 'dragon':{len_dragon}")
print(f"Falsy statement:{falsy_statement}")

#checking for on
word1 ="python"
word2 = "dragon"

#check if on is in both words
contains_on = "on" in word1 and "on" in word2

#output result
print(f"'on' is found in both 'python' and 'dragon':{contains_on}")
#jargon
sentence="i hope this course is not full of jargon."
contains_jargon = "jargon" in sentence
print(f"Does the sentence contain 'jargon'? {contains_jargon}")

#check if 'on' is not in both 'dragon' and python'
print('on' not in 'dragon' and 'on' not in 'python')      #output:False

#finding lenght for python and conversion
length = len('python')
#convert to float
length_float = float(length)
#convert to string
length_str =str(length_float)
print(length_str) 

#check a number is even or not
#prompt user for a number
number = int(input("Enter a number:"))
#check if it's even
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is not even")
#checking floor devision
result = 7 // 3
print(result == int(2.7))

#checking for type
print(type('10')== type(10))
#check int '9.8' is equal 10
# Convert '9.8' to a float first, then to an integer
number = int(float('9.8'))
print(number == 10)  


# Prompt the user for hours worked
hours = int(input("Enter hours: "))
# Prompt the user for rate per hour
rate_per_hour = float(input("Enter rate per hour: "))

# Calculate weekly earnings
weekly_earning = hours * rate_per_hour

# Display the weekly earnings as an integer value
print(f"Your weekly earning is {int(weekly_earning)}")


# Prompt the user to enter the number of years they have lived
years_lived = int(input("Enter number of years you have lived: "))

# Calculate the number of seconds in a year
seconds_per_year = 365 * 24 * 60 * 60  # 365 days, 24 hours, 60 minutes, 60 seconds
# Calculate the total seconds lived
total_seconds = years_lived * seconds_per_year
print(f"You have lived for {total_seconds} seconds.")


# Print the header row
print("Number  Square  Cube  Fourth Power  Fifth Power")
# Loop through the rows
for num in range(1, 6):
    square = num ** 2
    cube = num ** 3
    fourth_power = num ** 4
    fifth_power = num ** 5
    print(f"{num:<7} {1:<7} {num:<5} {square:<12} {cube:<12}")




