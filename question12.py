## Question 12 ##

temp = input("Please enter in the degrees in fahrenheit: ")

fahTemp = int(temp)

celsius = ((fahTemp - 32) / 1.8)

cel = int(celsius)
finalTemp = str(cel)

print("The temprature " + temp + " in fahrenheit is " + finalTemp + " degrees in celsius")


