## Question 10 ##

miles = input("Please enter in the number of miles you have driven: ")
gas = input("Now, in gallons, enter in how much gas you have used: ")

milesInt = int(miles)
gasInt = int(gas)

mpgInt = (milesInt / gasInt)

mpg = str(mpgInt)

print("You have been driving " + mpg + " miles per gallon")




