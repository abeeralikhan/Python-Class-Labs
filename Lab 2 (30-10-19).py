##FIRST PROGRAM
from datetime import date

print("\nProgram 1\n")
date_1= input("Enter first date (dd/mm/yyyy): ")
date_2= input("Enter second date (dd/mm/yyyy): ")

date1 = date(int(date_1[6:10]), int(date_1[3:5]), int(date_1[:2]))
date2 = date(int(date_2[6:10]), int(date_2[3:5]), int(date_2[:2]))

print(abs((date1-date2).days))
##Second Program

from math import sin, pi
print("\nPROGRAM 2\n")
def measure_height(ladder_length, angle_degree):
    if angle_degree>90:
        return('Angle has to be less than 90 degrees')
    #Conversion of angle from degree to radian
    angle_radian = pi*angle_degree/180
    #Caclculating height that ladder reaches
    height = ladder_length*sin(angle_radian)
    return height
def default_values():
    values=[[16, 75], [20, 0], [24, 45], [24, 80]]
    print("\n<-------------------DEFAULT VALUES------------------>")
    print("\nFor "+str(values[0][0])+" feets and "+str(values[0][1])+" degrees ==> "+str(("%.2f"%measure_height(values[0][0], values[0][1])))+" feets.")
    print("For "+str(values[1][0])+" feets and "+str(values[1][1])+" degrees ==> "+str(("%.2f"%measure_height(values[1][0], values[1][1])))+" feets.")
    print("For "+str(values[2][0])+" feets and "+str(values[2][1])+" degrees ==> "+str(("%.2f"%measure_height(values[2][0], values[2][1])))+" feets.")
    print("For "+str(values[3][0])+" feets and "+str(values[3][1])+" degrees ==> "+str(("%.2f"%measure_height(values[3][0], values[3][1])))+" feets.")
    print("\n<--------------------------------------------------->")
    
#Asking if user wants to enter any value
answer = input("Do you wish to enter values by yourself? (y/n): ")
if answer=="y":
    ladder_length = float(input("Enter length of the ladder in feet: "))
    angle_degree = float(input("Enter the angle that ladder makes in degree: "))
    print("\n<-------------------FROM YOUR INPUT----------------->")
    if measure_height(ladder_length, angle_degree)=='Angle has to be less than 90 degrees':
        print("\n\tAngle has to be less than 90 degrees")
        default_values()
    else:
        print("\nLadder of length "+str(ladder_length)+" feets and having "+str(angle_degree)+" degrees angle reaches around "+str("%.2f"%measure_height(ladder_length, angle_degree))+" feets.")
        default_values()
#Evaluating default values if user didnt want to enter any value
else:
    default_values()

##THIRD PROGRAM
print("\nProgram 3\n")
numbers = [1, 2, 3, 4, 5]
print("List of numbers", numbers)
print("Index of the middle element of the list is ", numbers.index(numbers[int(len(numbers)/2)]))
print("Middle element of the list is ", numbers[int(len(numbers)/2)])

numbers.sort(reverse=True)
print("List in descending order",numbers)

fl = numbers.copy()
numbers.remove(numbers[0])
numbers.append(fl[0])
print("Moving first element to last index", numbers)

#PROGRAM 4
print("\nPROGRAM 4\n")
monthsL = ['Jan', 'Feb', 'Mar', 'May']
monthsT = ('Jan', 'Feb', 'Mar', 'May')

#Doing Operations on List Data type
print("Evaluating Operations on List Container")
print("List of months", monthsL)
#Inserting Apr between Mar and May
monthsL.insert(3, 'Apr')
print("**Inserting Apr between Mar and May**")
print("Updated list of months", monthsL)
#Appending Jun in the list of monthsL
print("**Appending Jun in the list**")
monthsL.append('Jun')
print("Updated list of months", monthsL)
#Popping the List Container
print("**Popping the List container**")
monthsL.pop()
print("Updated list of months", monthsL)
#Reversing the List container
print("**Reversing the order of items in the List Container**")
print(monthsL[::-1]) #Or we can else use monthsL.reverse()
#Sorting the List Container
monthsL.sort()
print("**Sorting the List Container**")
print("Updated list of months", monthsL)
#Doing operations on Tuple Data type
print("Evaluating Operations on Tuple Container")
print("List of months in Tuple", monthsT)

#PROGRAM 5
##Changing statements into python expressions 
print("\nPROGRAM#5 \n\nChanging statements into python expressions")
#A) The number of characters in the word "anachronistically" are 1 more than the number of characters in the word "counterintuitive".
print("--------------------------------(A)--------------------------------")
print("STATEMENT : The number of characters in the word \"anachronistically\" \nare 1 more than the number of characters in the word \"counterintuitive\".")
print("\nPYTHON EXPRESSION : len('anachronistically')>len('counterintuitive')")
#B) The word "misinterpretation" appears earlier in the dictionary than the word "misrepresentaion"
print("--------------------------------(B)--------------------------------")
print("STATEMENT : The word \"misinterpretation\" appears earlier in the \ndictionary than the word \"misrepresentaion\".")
print("\nPYTHON EXPRESSION : dictionary=['misinterpretation', 'misrepresentaion']")
#C) The letter 'e' does not appear in the word "floccinaucinihilipilification"
print("--------------------------------(C)--------------------------------")
print("STATEMENT : The letter 'e' does not appear in the word \"floccinaucinihilipilification\".")
print("\nPYTHON EXPRESSION : 'e' not in 'floccinaucinihilipilification'")
#D) The number of characters in the word "counterrevolution" is equal to the sum of the number of characters in words "counter" and "revolution".
print("--------------------------------(D)--------------------------------")
print("STATEMENT : The number of characters in the word \"counterrevolution\" is \nequal to the sum of the number of characters in words \"counter\" and \"revolution\".")
print("\nPYTHON EXPRESSION : len('counterrevolution')==len('counter')+len('revolution')")
print("-------------------------------------------------------------------")

#PROGRAM 6
print("\nPROGRAM 6\n")
#
#A) Assign 6 to variable a and 7 to variable b.
a = 6
b = 7
print("--------------------------------(A)--------------------------------")
print("STATEMENT : Assign 6 to variable a and 7 to variable b.")
print("\nPYTHON EXPRESSION: \na=6 \nb=7")
#B) Assign to variable c the average of variables a and b.
print("--------------------------------(B)--------------------------------")
print("STATEMENT : Assign to variable c the average of variables a and b.")
print("\nPYTHON EXPRESSION: \nc = (a + b)/2")
c = (a + b)/2
#C) Assign to variable inventory the list containing strings 'paper', 'stapples', 'pencils'.
print("--------------------------------(C)--------------------------------")
print("STATEMENT : Assign to variable inventory the list containing strings 'paper', 'stapples', 'pencils'.")
print("\nPYTHON EXPRESSION: \ninventory = ['paper', 'staples', 'pencils']")
inventory = ['paper', 'staples', 'pencils']
#D)Assign to variable first, middle and last the string 'John', 'Fitzgerald' and 'Kennedy'.
print("--------------------------------(D)--------------------------------")
print("STATEMENT : Assign to variable first, middle and last the string 'John', 'Fitzgerald' and 'Kennedy'.")
print("\nPYTHON EXPRESSION: \nfirst = 'John' \nmiddle = 'Fitzgerald' \nlast = 'Kennedy'")
first = 'John'
middle = 'Fitzgerald'
last = 'Kennedy'
#E) Assign to variable fullname the concatenation of string variables first, middle, and last.
print("--------------------------------(E)--------------------------------")
print("STATEMENT : Assign to variable fullname the concatenation of string variables first, middle, and last.")
print("\nPYTHON EXPRESSION: \nfullname = first +" "+middle+" "+last")
fullname = first +" "+middle+" "+last

##PROGRAM 7
print("PROGRAM#7")
def dart_position(x, y):
    #Following expression will run if dart hits the middle.
    if ((x**2)+(y**2))==0:
        return("Bullseye! Right in the middle.")
    #Following expression will run if dart didnt hit the middle but is inside the board.
    elif ((x**2)+(y**2))<100:
        return("Dart hits the Board.")
    #Following expression will run if dart neither hit the middle nor is inside the board.
    elif ((x**2)+(y**2))>100:
        return("Dart went outside the Board.")
def default_values():
    values=[[0, 0], [10, 10], [6, 6], [7, 8]]
    print("\n<----------------DEFAULT CO-ORDINATES--------------->")
    print("\n("+str(values[0][0])+", "+str(values[0][1])+") ==> "+dart_position(values[0][0], values[0][1]))
    print("("+str(values[1][0])+", "+str(values[1][1])+") ==> "+dart_position(values[1][0], values[1][1]))
    print("("+str(values[2][0])+", "+str(values[2][1])+") ==> "+dart_position(values[2][0], values[2][1]))
    print("("+str(values[3][0])+", "+str(values[3][1])+") ==> "+dart_position(values[3][0], values[3][1]))
    print("\n<--------------------------------------------------->")
#Asking if user wants to enter any value
answer = input("Do you wish to input co-ordinates by yourself? (y/n): ")
if answer=="y":
    x = int(input("Enter 'x' co-ordiante of the dart: "))
    y = int(input("Enter 'y' co-ordiante of the dart: "))
    print("\n<-------------------FROM YOUR INPUT----------------->")
    print("\nEntered Co-ordinates "+"("+str(x)+", "+str(y)+") ==> "+dart_position(x, y))
    default_values()
#Evaluating default values if user didnt want to enter any value
elif answer=="n":
    default_values()
else:
    print("Invalid Value")
##END 


    
