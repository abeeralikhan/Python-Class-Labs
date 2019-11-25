##(1)This Program will convert Farenheit to Celcius

tempF = int(input("Enter temperatue in Farenheit: "))
tempC = (tempF - 32)/(9/5)
print(str(tempF)+"F in Degree Centigrade is "+str("%.2f" % tempC)+"C")

##(2)This Program will convert Degree Centigrade to Farenheit

tempC = float(input("Enter temperatue in Degree Centigrade: "))
tempF = (tempC * (9/5))+32
print(str(tempC)+"C in Farenheit is "+str("%.2f" % tempF)+"F")

##(3)To calculate area of Rectangle

l = int(input("Enter Length of Rectangle(in cm): "))
b = int(input("Enter Breadth of Rectangle(in cm): "))
area = l*b
print("Area of the Rectangle: ", area)

#(4)This program will calculate volume of sphere.

r = float(input("Enter radius of the Sphere(in cm): "))
pi = 3.142
volume = (4/3)*pi*r**3
print("Volume of the sphere is "+str("%.2F" % volume)+"cm cube")

#(5)This program will write your name in title, upper and lower case format.

name=input("Enter your name in mix format: ")
print("Your name in title case format is "+name.title())
print("Your name in upper case format "+name.upper())
print("Your name in lower case format "+name.lower())