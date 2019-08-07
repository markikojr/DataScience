#!/usr/bin/python 

#IMPORTING MODULES
import numpy as np

#GENERATING RANDOM NUMBERS WITH NORMAL DISTRIBUTION (CENTERED, STD, #)
A = np.random.normal(25.0, 5.0, 10)
print ("------")
print ("Random Numbers:", A)

#CREATING LISTS
x = [1, 2, 3, 4, 5, 6]
print ("------")
print ("List:",x)

#LIST'S SIZE
print("List's Size:",len(x))

#ACCESSING FIRST ELEMENTS
print ("First Elements:",x[:3])

#ACCESSING LAST ELEMENTS
print ("Last Elements:",x[3:])

#APPEDING TO THE LIST
x.append(9)
print ("Updated List:",x)

#ACCESSING ONE ELEMENT FROM THE LIST
print ("Element 5:",x[4])

#CREATING DICTIONARIES
captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

print ("------")
print ("Captains' Element:")
print(captains["Voyager"])
print(captains.get("Enterprise"))

#LOOPING THROUGT ALL ELEMENTS
print ("------")
print ("All Elements:")
for ship in captains:
    print(ship + ": " + captains[ship])
    
#FUNCTIONS
def SquareIt(x):
    return x * x
print ("------")
print ("Function Squareit result:",SquareIt(2))
    