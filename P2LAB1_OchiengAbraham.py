#Abraham Ochieng 
#the program will calculate the diamater, circumfrence, and area of a circle 

#omport math module to us the constan, math pi
import math

#get the radius from the user
radius = float(input("Enter the radius of the circle?" )) 
print()

#calculate diameter
diameter = 2 * radius 

#display diameter with 1 demical point 
print(f"the diameter of the circle is {diameter:.1f}\n")

#calculate circumfrence
circumfrence = 2 * math.pi * radius

#display circumfrience with 2 decimal  places 
print(f"the circumfrence of the circle is {circumfrence:.2f}\n")

#calculate area
area = math.pi * radius **2 

#display area with 3 decimal places
print(f"the area of the circle is {area:.3f}\n")
