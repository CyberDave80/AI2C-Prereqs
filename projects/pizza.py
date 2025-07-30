'''
Problem 2 - Pizza Shop Shenanigans
Your local pizza shop (“Byte da Pi”) is rolling out so-called ‘deals’ on the regular, but you’ve become suspicious if they are actually deals.
For instance, this week Byte da Pi is offering two small pizzas (10” diameter) for $19.99.  However, their regular priced large pizza (16” diameter) is priced $20.99.  Are the two small pizzas really a deal at $19.99?
Implied:  You need to determine the area of the pizzas.
Solve for this specific deal, and then create two functions to help you solve for any deal.
The first function should determine the price per square inch of pizza.  How many parameters will this function have?
The second function should compare deals based on $/in2 and quantity of pizzas offered in the deal.  This function should have four parameters. What are they?
BONUS:  If your program finds it to be a good deal, your python script should open the webpage of a local pizza shop.  If your program finds it to be a bad deal, tell the user, and open the webpage of a pizza chain (Dominoes/Papa Johns…).  Also add ASCII Art.
'''



import math

def price_per_square():
    pass

def circle_math():
# Get the radius from the user
    radius = float(input("Enter the radius of the circle: "))
# Calculate the area
    area = math.pi * (radius ** 2)
# Display the result
    print(f"The area of the circle with radius {radius} is: {area}")

def compare_deals():
    pass
