"""
#accept a file name from the user and then print the extension
import os

filename = input("Enter the file name: ")
_, extension = os.path.splitext(filename)

if extension:
    print("The extension of the file is:", extension[1:])  # remove the dot
else:
    print("No extension found in the file name.")

"""

'''
#calculates the area of a circle given the radius

    r = float(input("Enter the radius: "))
a = 3.14 * r * r
print("Area of the circle is:", a)
'''

'''
# Find the biggest of 3 numbers

print("Enter 3 numbers:")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Compare using if-else
if a > b:
    biggest = a
else:
    biggest = b

if c > biggest:
    biggest = c

print("The biggest number is:", biggest)
'''
'''
#Create a list of colors from comma-separated color names entered by user. Display first and last colors.


# Get comma-separated color names from user
color_input = input("Enter color names separated by commas: ")

# Create a list by splitting the input
color_list = color_input.split(',')

# Display first and last colors
if color_list:
    print("First color is:", color_list[0])
    print("Last color is:", color_list[-1])
else:
    print("No colors entered.")
'''

#Count the occurrences of each word in a line of text.
















#

































#******
