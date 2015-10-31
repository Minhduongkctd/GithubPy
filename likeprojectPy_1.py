#Print string forma
print("Twinkle, Twinkle, littlestart,\n\tHow I wander what you are! \n\t\tUp above the world so high,\n\t\tLike a diamond in the Sky.\nTwinkle, twinkle, little star,\n\tHow I wander what you are")

#to get the Python version you are using.
import sys
print(sys.version)

#print the current date and time.
#version1
import datetime
now = datetime.datetime.now()
print("current date and time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

#version2

import time
print("\nThis is another version!")
print(time.strftime("%x %X"))
print(time.strftime("%Y-%m-%d %X"))

#Question 4 write cycle area

from math import pi
r = 1.1
def compute():
    Area = pi*r*r
    print ("r =",r)
    print ("Area =", Area)

compute()
#another version
r = float(input("Enter the radius of the circle: "))
print("The area of the circle with radius " + str(r) + "is: " +str(pi*r**2))


#Question 5 write your first and last name and reverse with space
firstname = input("Enter Your First Name: ")
lastname = input("Enter Your Last Name:")
print(lastname + " " + firstname)
