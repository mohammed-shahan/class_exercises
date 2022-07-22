"""

#define a simple class with a constructor that can accept two variables
class Employee:
    #defining a global variable(data member)
    empCount = 0

    #defining a constructor
    #that can accept two values name and salary
    #save those values into self (self is an instance of the class)
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1 #increment the emp count when a new obj is created.

     #define a simple member function
    def displayEmpCount(self):
        print("Total no of employees:",Employee.empCount)
    def displayEmployeeDetails(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

#create an object of employee class
employee1 = Employee("Tom",2000)
employee1.displayEmpCount()
employee1.displayEmployeeDetails()

employee2 = Employee("Jerry",3000)
employee2.displayEmpCount()
employee2.displayEmployeeDetails()

print("Total employee count ",Employee.empCount)

"""

###################################
#demonstrating Class Inheritance
#Defining teh Base class
class Rocket:
    # Defining the constructor
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def launch(self):
        return "%s has reached %s" % (self.name, self.distance)

class MarsRover(Rocket):
    def __init__(self, name, distance, maker):
        #calling the base class constructor
        Rocket.__init__(self, name, distance)
        self.maker = maker
        
    
    def printMaker(self):
        return "%s launched by %s" % (self.name, self.maker)

#create object (instance) for main class Rocket
x = Rocket("small rocket","till stratosphere")
y = MarsRover("mars rover","till mars","ISRO")

print(x.launch())
print(y.launch())
print(y.printMaker())


#Encapsulation
