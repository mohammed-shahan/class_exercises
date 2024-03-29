"""
import sys
import re
from unittest.result import STDERR_LINE

print("Hello World")
print(sys.version)

# This is a single line comment
""""""This is a multi line coment""""""

name = "Lucas Scott"
print(name.lower())

myString = 'superman'

print(myString.endswith('man'))
print(myString.endswith('man', 3)) # start checking from index 3
print(myString.endswith('man', 2, 6)) # start checking from index 2 to 6
print(myString.endswith(('man','ma'), 2, 6))

#join() method
seperator = "*"
myTuple = ("h","e","l","l","o")
myNewString = seperator.join(myTuple)
print(myNewString)
print(myNewString.lower())
print(myNewString.upper())

#replace and split methods
myString = "Hello World"
myString= myString.replace('o','i')
print(myString)
myStringSplit = myString.split(' ')
print(myStringSplit)

txt = "bits of paper, bits of paper"
x= re.findall("bi",txt)
print(x)

x= re.search("bi",txt)
print(x)

txt = "bits of paper bits of paper"
x = re.sub(" ","-",txt)
print(x)

#search with metacharacters
txt = "Hello World"
#find all lower case characters between "a" and "m"
x = re.findall("[a-m]",txt)
print(x)

txt = "James Bond is 007"
#find all digits
x = re.findall("\d",txt)
print(x)

txt = "James Bond is 007"
#search for a sequence that starts with j and end with d and has 3 characters in between
x = re.findall("J...s",txt)
print(x)

txt = "Hello World"
#check if the string starts with 'hello'
x = re.findall(r"^Hello",txt)
print(x)

txt = "Hello World"
#check if the string ends with 'world'
x = re.findall(r"World$",txt)
print(x)
#check if the string ends with 'Jam'
#using the special sequence \A
txt = "James Bond is 007"
x = re.findall(r"\AJam",txt)
print(x)
#check if the string ends with 'world'
#using the special sequence \b
txt = "James Bond is 0007"
x = re.findall(r"\b007",txt)
print(x)

#extract email from the text
txt = "Hello test@gmail.com how are you?"
#check for the non-space characters before and after "$"
regex = r"\S+@\S+"
print(re.findall(regex, txt))

#Python lists and list access options
studentAge = [18, 21, 23, 20, 21]

print(studentAge)
print(studentAge[2]) #print particular index
print(studentAge[-1]) #print the last index
print(studentAge[2:4]) #from index 2 to 4
print(studentAge[:3]) #from index 0 to 3-1
print(studentAge[2:6:2]) #from index 2 to 6 in steps of 2
print(studentAge[::-1]) #reverse the list

#append 
studentAge.append(16)
studentAge.append("hi")
print(studentAge)

#delete values from the list
del studentAge[-1]
print(studentAge)

#combine two lists using extend
studentName = ['Anu', 'Sinu', 'Binu']
studentAge.extend(studentName)
print(studentAge)

#to check if a variable is in the list
print('Binu' in studentName)
print('Anushka' in studentName)

#find the no. of items in the list
print(len(studentAge))
print(len(studentName))

#reverse the list using reverse()
studentName.reverse()
print(studentName)
studentName.reverse()
print(studentName)

#sort the list either alphabetically or numerically
studentName.sort()
print(studentName)

#list concatenation using + operator
print(studentName + studentName)

#list duplication/multiplcation using * operator
print(studentName*3)

#Tuples in Python
months  = ("Jan", "Feb", "March")
print(months[0])
print(months[-1])
# months[0] = 'test' 

#Tuple methods in Python
print(len(months))

print("Jan" in months)
print("Janary" in months)

print(months+months)
print(months*3)

#delete the tuple
del months
print(months)

#Dictionary in Python
#declaration
#method 1
myStudents = {"Abhi": 30, "Sibi": 28, "Subi":"Not available"}
#method 2
myStudents = dict(Abhi = 30, Sibi = 28, Subi = "Not available")
#mehod 3
myStudents = dict({"Abhi": 30, "Sibi": 28, "Subi":"Not available"})

print(myStudents)
print(myStudents["Sibi"])

#Dictionary methods
print(myStudents.get("Abhi")) #return the corresponding value
print(myStudents.items()) #return the dict items as tuple
print(myStudents.keys()) #return dict keys as a list
print(myStudents.values()) #return dict values as a list
print("Abhi" in myStudents) #check if key is present
print(30 in myStudents.values()) #check if value is present
print(len(myStudents)) 
myStudents2 = {"Abhi": 31, "Binu": 26}
myStudents.update(myStudents2) #join dictionaries by overwriting duplicate keys
print(myStudents)

myStudents.clear() #deletes all items in the dictionary
print(myStudents)
del myStudents #deletes the dictionary along with the variable
print(myStudents)


#Sets in Python
#method 1
months = {"January", "February", "March", "April"}
#method 2
months = set(["January", "February", "March", "April"])
print(months)
print(type(months))

#looping through elements in a set
for i in months:
    print(i)

#declare an empty set
days = set()
#add values to set
days.add("Monday") #takes only one parameter
days.add("Tuesday")
days.add("Wednesday")
days.update(["Thursday", "Friday", "Saturday"]) #insert multiple value

#looping through elements in a set
for i in days:
    print(i)

#remove items from the set
#using discard(), will not display error if doesn't exist
days.discard("Thursday")
#using remove(), will display error if doesn't exist
# days.remove("Thursday")

#clear the items in the set
days.clear()
print("Cleared the set")
#looping through elements in a set
for i in days:
    print(i)

#Set operations
months1 = {"January", "February", "March", "April"}
months2 = {"March", "April", "May"}
months3 = {"February", "Marh", "January", "July"}
#union operation
months3 = months1 | months2
print(months3)
for month in months3:
    print(month)

#insersection operation
months3 = months1 & months2
print(months3)
for month in months3:
    print(month)

#intersection update method 
# months1.intersection_update(months2, months3)
# print(months1)

#Differance operation
months4 = months1 - months2
print(months4)

#Symmetric difference operation
#will retain all months of the two sets excluding the common oness
months4 = months1 ^ months2
months4 = months1.symmetric_difference(months2)
print(months4)
months4 = months1.symmetric_difference_update(months2)
print(months1)

#Set comparison operators
months1 = {"January", "February", "March", "April", "May", "June"}
months2 = {"March", "April", "May", "February"}
months3 = {"February", "March", "April", "May"}
#checking if months1 is a superset of months2
print(months1 > months2)
#checking if months1 is a subset of months2
print(months1 < months2)
#checking if two sets are equal
print(months2 == months3)
#checking if two sets are equal as well as months1 is a superset of months2 
print(months1 >= months2)
#checking if two sets are equal as well as months2 is a superset of months1
print(months1 <= months2)

#Frozen Set
months4frozen = frozenset(["November", "December"]) #immutable set
print(type(months4frozen))
print(months4frozen)
months4frozen.add("October")

# input and output functions is python
studName = input("Enter your name: ")
studAge = input("Enter your age: ") #always taken as a string
print(studName)
print(type(studName))
print(studAge)
print(type(studAge))

#variations of print statements to include variables
print("Name:",studName, "Age:",studAge)
print("Name: %s Age: %s" %(studName, studAge))
print("Name: {} Age: {}".format(studName, studAge))

#print in multiple lines
print('''Hello World
How are you''')
#print a new line
print("Hello World \nHow are you")
print("This is a backslash \\") #\ is the esape character

#Control flow statements 
#conditional statements
#if condition
userInputNo = input("Enter either 1 or 2 : ")
if(userInputNo == "1"):
    print("You entered 1")
    print("And you are no. 1")
elif(userInputNo == "2"):
    print("You entered 2")
    print("Runner up. Keep it up!")
else:
    print("You didn't enter 1 or 2")

#inline if statement
B = 12
A = 12 if B == 10 else 13
print(A)

print("B is ten" if B == 10 else "B is not ten")

def http_status(status):
    match status:
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case _:
            return "Unknown error occured" 

#calling the function inside print statement
print(http_status(404))

#Looping in python
#use for loop to loop/iterate through a list
fruits = ['apples','oranges','banana', 'cherry']
for fruit in fruits :
    print(fruit)
#to display index also using enumerate method
for index, fruit in enumerate(fruits):
    print(index, fruit)
#use for loop to generate a series of numbers
#using range funtion
for i in range(10):
    print(i)

#while loop 
counter = 5
while counter > 0:
    print("counter =",counter)
    counter = counter - 1

#Break and Continue statement
#break
j = 0
for i in range(10):
    j = j+2
    print("i =",i,"j = ",j)
  i  if(j == 6):
        break

#continue
j = 0
for i in range(10):
    j = j+2
    print("i =",i,"j = ",j)
    if(j == 6):
        continue
    print("j value is:",j)

# try except 
try:
    answer = 12/0
    print(answer)
except:
    print("Some friendly error message")
#Python Functions
#define the function
def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if(numberToCheck%x == 0):
            return False
    return True
#calling the function
print(checkIfPrime(15))

#Return in Python
def calculations(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    mod = a % b
    return (add, sub, mul, div, mod)

output = calculations(40, 30)
print("Addition :", output[0])
print("Subtraction :", output[1])
print("Multiplication :", output[2])
print("Division :", output[3])
print("Modulus :", output[4])

#Yield in Python
#generator is a function that returns an iterator
def calculationsYield(a, b):
    add = a + b
    # yield add
    sub = a - b
    # yield sub
    mul = a * b
    # yield mul
    div = a / b
    # yield div
    mod = a % b
    # yield mod
    yield add, sub, mul, div, mod


#using a for loop, we can loop through the returned value from the function
for values in calculationsYield(40, 30):
    print(values)


#Variable Scope
#declaring a global variable
from distutils.archive_util import make_archive


message1 = "Just a global variable"

def myFunction():
    global message1
    print("reached inside function")
    print(message1) #printing global variable
    message2 = "It's a local variable" #declraing a local variable
    print(message2)
    message1 = "Just modifying the global variable"
    print(message1) #printing global variable

myFunction() #calling the function


#demonstrate passing the arbitrary list of arguments into the function
def make_pizza(size, *toppings): #arbitrary list is prefixed by
    print(f"\making a {size} - inch pizza with following toppings :")
    for topping in toppings :
        print(f"{topping}")

make_pizza(12,"pepperoni")
make_pizza(16,"mushrooms","green pepper")

#passing arguments as required and keyword args
def printInfo(name, age):
    print("name",name)
    print("age",age)

#calling the required arguments
printInfo("Tom",10)
#calling the keyword arguments
printInfo(age=10, name="winne")

#lambda functions in python

sum = lambda num1, num2:num1+num2
#calling the lambda function
print("sum of two numbers",sum(2,3))


#Python modules
#importing a module
import random
#calling function inside the module
print(random.randrange(1,10))

#the random built in module
print(random.random())
print(random.randint(5,20))
print(random.choice(["head","tail"]))
#shuffle random
myshirtcolors = ["blue","red","black","yellow","green"]
random.shuffle(myshirtcolors)
print(myshirtcolors)
print(myshirtcolors)

random.seed(10)
print(random.random())


#python date time module
import time 

print(time.time()) #seconds past 1st jan 1970
print(time.localtime(time.time())) #get the multiple time values as a tuple
print(time.asctime(time.localtime(time.time())))

for i in range(0,10):
    print(i)
    time.sleep(1) #delay the program execution by tghe specified number of seconds


import datetime
print(datetime.datetime.now()) #return the current date time object

#creating custom datetime object
birthday = datetime.datetime(2022,7,20)
print(birthday)




import calendar

myCalendar = calendar.month(2022,7) #get calendar of a month
print(myCalendar)

myCalendar = calendar.prcal(2022)#calendar of the entire year
print(myCalendar)




import math

#finding the exponential of a number, then its absolute, then its log, the
#convert to the base of 10


number = 2e-7
print(math.log(math.fabs(number)))

number = math.pow(4,2) #power of the number
print(number)

number = math.floor(4.3) #round to smallest digit
print(number)

number = math.ceil(4.3) #round to the next digit
print(number)

number = math.fabs(-10) #return absolute value
print(number)

number = math.factorial(10) #return factorial
print(number)

number = math.modf(3.14) #return int and fractional part
print(number)



#calling the custom module created
import prime

answer = prime.checkIfPrime(7)
print(answer)


#decorators - a function which accepts another function, enhance it
#with a wrapper function and return the enhanced function back

def myDecorator(myFunc):
    def innerWrapper(): #wrapper function decorates the function received
        print("Before the Function Call")
        myFunc()
        print("After the function call")
    return innerWrapper

#defining a simple fn to pass into the decorator
def myFnToPassIntoDecorator():
    print("A simple function to pass into decorator")

#calling the decorator
myDecoratordemo = myDecorator(myFnToPassIntoDecorator)

# execute the decorator
myDecoratordemo()



##########################
#

#a simple function with a print statement
#which can accept at least one fn and can optionally return a fn

# a simple fn with a print statement
def greet(name):
    return "Hello{}".format(name)

#defining the higher order fn which can accept fn
def print_greetings(fn,param):
    print(fn(param))

#calling the higher order fn
print_greetings(greet,"Abhi")

#map() fn - a higher order fn which can accept a fn and also
#a list of iterable params. Each param will be applied to the function
#and result will be returned back as a map obj
#we can later convert this map obj into set/tuple

#defining a simple fn
def mymapfunction(a):
    return a*a

#passing a lambda fn as well as the iterables
x = map(lambda x:x*x, (1,2,3,4))
#x is a map obj, need to convert that into a set/tuple
print(tuple(x))

#filter function
def filterFn(x):
    if(x>=3):
        return x
y = filter(filterFn, (1,2,3,4,5,6)) # memory efficient compared to for loop
print(list(y))

y = filter(lambda x : x >= 3, (1,2,3,4,5,6))
print(list(y))

#reduce function


#class and regular function without the abstract class
class Lion:
    def give_food(self):
        print("Feeding a lion with raw meat")

class Panda:
    def feed_animal(self):
        print("Feeding a panda with bamboo") 

class Snake:
    def feed_snake(self):
        print("Feeding a snake with mice")

#Creating objects for animals we plan to feed
simba = Lion()
kungfupanda = Panda()
kingcobra = Snake()

#calling the feeding fn for each of them
simba.give_food()
kungfupanda.feed_animal()
kingcobra.feed_snake



#abstract class example

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def feed(self):
        pass
# class Lion inheriting abstract class Animal
class Lion(Animal):
    def feed(self):
        print("Feeding the Lion with raw meat")
class Panda(Animal):
    def feed(self):
        print("Feeding the panda with Bamboo")
class Snake(Animal):
    def feed(self):
        print("feeding mice")
    def feed_snake(self):
        print("Feeding a snake with mice")

simba = Lion()
simba.feed()
panda = Panda()
cobra = Snake()
panda.feed()
cobra.feed()

#instead of calling method repeatedly like the above,
#we can have a for loop for the list of classes
zoo_class_list = [Lion(), Panda(), Snake()]

for animal in zoo_class_list:
    animal.feed()



class Panda(Animal):
    def diet(self):
        return["bamboo","Leaves"]
    def feed(self):
        print("")




###################################################################################

#File handling in python
# opening a file in the same directory in read mode
from fileinput import close


myfile = open("myfile.txt", "r")
# read the contents using read()
print(myfile.read())
print(myfile.read(10)) #read the first 10 characters
print(myfile.read(30)) #will read from where the last read was stopped
print(myfile.readline()) #will read a single line form the file

# reading the contents of the file line by line using a for loop
for line in myfile:
    print(line)
myfile.close()

myfile = open("myfile.txt", "r")
# read all the lines 
contentList = myfile.readlines()
print(contentList)

# close he cursor
myfile.close()

#opening the file cursor in append mode
#whatever we write will be appended to the end of file
myfile = open("myfile.txt", "a")
#write() etod is used to write text / data to a file
myfile.write("This is a new line\n")
myfile.close()

myfile = open("myfile.txt", "r")
for line in myfile:
    print(line)
myfile.close()

#opening the file cursor in write mode
#whatever we write will overwrite the file
myfile = open("myfile.txt", "w")
#write() method is used to write text / data to a file
myfile.write("This is a new line\n")
myfile.close()

#opening the file cursor in read mode
myfile = open("myfile.txt", "r")
print(f"The file pointer is now at {myfile.tell()}")
# contentList = myfile.readlines()
# print(contentList)
# print(myfile.readline())
# change the file pointer offset using seek
myfile.seek(29) #reading will start from 30
print(f"The file pointer is now at {myfile.tell()}")
contentList = myfile.readlines()
print(f"The file pointer is now at {myfile.tell()}")
print(contentList)
myfile.close()

#File Operations
#Renaming a file
import os
if os.path.exists("myfilenew.txt"):
    os.rename("myfilenew.txt", "myfile.txt")
    print("The file has been renamed")
else:
    print("The file doesn't exist")

#Deleting a file
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("The file has been removed")
else:
    print("The file doesn't exist")

#Folder Manipulations in Python
import os
#creating a new directory
# os.mkdir("mydir")
#print the current working directory
print(os.getcwd())
#change the current working directory
os.chdir("mydir")
print(os.getcwd())
#delete the directory
os.chdir("..") #go back to the previous directory
print(os.getcwd())
os.rmdir("mydir")
#get the list of files
result  = os.listdir(os.getcwd())
print(result)

#run an external python file (fileoutputsave.py)
#save its results as txt file

import subprocess
with open("myfile.txt", "wb") as f:
    subprocess.check_call(["python", "fileoutputsave.py"], stdout=f)

#Python Exceptional Handling Basics

try:
    div = 4 // 0
except Exception as e:
    print("Attempting to divide by zero")
    print(f"{type(e).__name__} occered. More details below") #get the exception name
    print(e) #print the entire details of the exception
else:
    print(f"Division Completed and result is : {div}")
finally:
    print("This is code of finally clause")

#Nested try except statements in Python

try:
    f = open("somefile.txt")
    try :
        f.write("Hello world")
    except:
        print("some write error occered")
    finally:
        f.close()
except:
    print("The file cannot be opened")

#MSSQL Database Connection in Python
#importing pyodbc module
import pyodbc

#create a connection string
myConString = 'Driver={SQL Server};Server=DESKTOP-517KMB6\SQLEXPRESS;Database=employee_db;Trusted_Connection=yes;'
#create a connection with the connection string
myconn = pyodbc.connect(myConString)
try: 
    #get the cursor object
    mycursor = myconn.cursor()

    #using cursor, we can execute SQL commands
    mycursor.execute('SELECT * FROM EmployeeMaster WHERE Salary = 3000')

    for row in mycursor:
        print(row)
except Exception as e:
    print(f"{type(e).__name__}")

myconn.commit()
myconn.close()

#Creating a table in the database
myconn = pyodbc.connect(myConString)

try:
    mycursor = myconn.cursor()
    mycursor.execute('''CREATE TABLE EmployeeMaster3(
        Id INT IDENTITY PRIMARY KEY,
        EmployeeCode VARCHAR(10),
        EmployeeName VARCHAR(25),
        DepartmentCode VARCHAR(10),
        LocationCode VARCHAR(10),
        Salary INT
    );''')
except Exception as e:
    print("Cannot create the table because : ")
    print(f"{type(e).__name__} occured.")
    print(e)

myconn.commit()
myconn.close()

print("Statement after the query")

import pyodbc

#create a connection string
myConString = 'Driver={SQL Server};Server=DESKTOP-517KMB6\SQLEXPRESS;Database=employee_db;Trusted_Connection=yes;'
#create a connection with the connection string
myconn = pyodbc.connect(myConString)
try: 
    #get the cursor object
    mycursor = myconn.cursor()

    #using cursor, we can execute SQL commands
    mycursor.execute('SELECT * FROM EmployeeMaster')

    # for row in mycursor.fetchall():
    #     print(row)

    #to get the data as a dictionary
    employees = [{'empcode': row[1]}, {'empname': row[2]}for row in mycursor.fetchall()]
    print(employees)
except Exception as e:
    print(f"{type(e).__name__}")

myconn.commit()
myconn.close()
"""

#insert values into the database
import pyodbc

#create a connection string
myConString = 'Driver={SQL Server};Server=DESKTOP-517KMB6\SQLEXPRESS;Database=employee_db;Trusted_Connection=yes;'
#create a connection with the connection string
myconn = pyodbc.connect(myConString)
try: 
    #get the cursor object
    mycursor = myconn.cursor()

    #using cursor, we can execute SQL commands
#   mycursor.execute('''INSERT INTO EmployeeMaster VALUES
# ('E0088', 'Arjun', 'IT', 'TVM', 9000)''')

    # mycursor.execute("INSERT INTO EmployeeMaster VALUES (?, ?, ?, ?, ?)",('E0099', 'Ajun', 'IT', 'TVM', 12000))

    mycursor.execute("SELECT * FROM EmployeeMaster")

    # for i in mycursor:
    #     print(i)
    #to get the data as a dictionary
    employees = [{'empcode': row[1], 'empname': row[2], 'empdept': row[3], 'emploc': row[4], 'empsal': row[5]} for row in mycursor.fetchall()]
    print(employees)
except Exception as e:
    print(f"{type(e).__name__}")
    print(e)

myconn.commit()
myconn.close()

