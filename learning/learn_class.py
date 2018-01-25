# File Name learn_class.py
# Demo for Python class concepts
# link : https://www.tutorialspoint.com/python3/python_classes_objects.htm
#!usr/bin/python3

from utility import *
import operator

printDes("Example of class: Developer")

class Developer:
    "Developer class to hold information of developer"
    skills = {}
    # Constructor
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        count = Developer.skills.get(skill)
        if count != None:
            Developer.skills[skill] = count + 1
        else:
            Developer.skills[skill] = 1

    # End __init__
    # Destructor
    def __del__(self):
        print("Removing developer: ", self.name)
        count = Developer.skills.get(self.skill)
        if count != None and count == 1:
            print("Last developer with skill %s, removing entry " % self.skill)
            del Developer.skills[self.skill]
        else:
            print("Remove developer with skill %s" % self.skill)
            Developer.skills[self.skill] = count - 1

        class_name = self.__class__.__name__
        print (class_name, "destroyed")
    # End
    def showSkill(self):
        print("The developer %s has skill => " % self.name, self.skill)
        print("The number of developer under same skill => ", Developer.skills[self.skill])
    # End showSkill
# End Developer

# Class: Employee: Base class
class Employee:
    "Class Employee: Base class for employee of org"
    # Class-vars
    dept = {}
    count = 0
    # Class/Static methods
    # Add dept
    @classmethod
    def addDept(cls,deptVal):
        try:
            existing = cls.dept[deptVal]
            cls.dept[deptVal] = existing + 1
        except:
            cls.dept[deptVal] = 1
    # End addDept
    # Show Dept Stat
    @staticmethod
    def showDeptStat():
        for key, count in Employee.dept.items():
            print("Dept: %s and number of employee: %d" % (key,count))
    # End showDeptStat
    # Constructor
    def __init__(self,name, dept, salary, role):
        self.name = name
        self.dept = dept
        self.salary = salary
        self.role = role
        self.type = "Employee"
        Employee.addDept(dept)
        Employee.count += 1
    # End __init__
    # Destructor
    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, "destroyed")
    # End __del__
    # __str__
    def __str__(self):
        class_name = self.__class__.__name__
        formatStr = "" + class_name.__str__() + ": name: %s, Dept: %s, Role: %s, Type: %s, Sal: %s"
        return formatStr % (self.name, self.dept, self.role, self.type, self.salary)
    # end __str__

# End Employee

# Class Engineer
class Engineer(Employee):
    # Constructor
    def __init__(self,name, dept, salary, jobType):
        super(Engineer, self).__init__(name,dept,salary,role= "Engineer")
        self.jobType = jobType
        self.technologies = []
    # End __init__
    # Basic Method Override
    def __str__(self):
        strVal = super(Engineer, self).__str__()
        return strVal + ", JobType: " + self.jobType.__str__()

    ## Methods
    # addTechnologies
    def addTech(self, tech):
        self.technologies.append(tech)
    # End addTechnologies
# End Engineer

# Class Vector
class Vector:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # end __init__
    # operator overloading
    # __str__
    def __str__(self):
        return "V:[{0},{1}]".format(self.x, self.y)
    # end __str__
    # __add__
    def __add__(self, other):
        return  Vector(self.x + other.x, self.y + other.y)
    # end add
    # __eq__
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    # end __eq__
    # __lt__
    def __lt__(self, other):
        return ((self.x < other.x) and (self.y < other.y))
    # end __lt__
    # other useful operator __sub__(x - y), __mul__(x * y), __pow__(x ** y),
    # __truediv__(x / y), __floordiv__(x // y), __mod__(x % y),
    # __lshift__(x << y), __rshift__(x >> y)
    # __and__(x & y), __or__(x | y), __xor__(x ^ y), __invert__(~x)
    # __cmp__ is depricated in python3
# end Vector

# Data Hiding: name python variable with _ prefix. It will become private member
# Class: Student
class Student:
    #_marks = 0
    def __init__(self,marks):
        self.__marks = marks
    # End: __init__
    # Getter/Setter: marks
    def getMarks(self):
        return self.__marks
    def setMarks(self,mrks):
        self.__marks = mrks
    # End: Getter/Setter: marks
# End: Laba


# Functional Methods
def useDeveloper():
    printDes("Simple Class Structure")
    dev1 = Developer("Laba", "Indentity managment")
    dev2 = Developer("Bhoba", "iOS")
    dev3 = Developer("Lele", "iOS")
    dev4 = Developer("Bunip", "automation testing")
    dev5 = Developer("Pungi", "None")

    devArray = [dev1, dev2, dev3, dev4]

    #1.
    print("Accessing showSkill method: dev2.showSkill()")
    dev2.showSkill()

    #2.
    print("Getting value of skill of an object get attribute")
    if hasattr(dev2, "skill"):
        print("getattr(dev2, \"name\") = ", getattr(dev2, "name"))

    #3.
    print("Set new attribute with value")
    setattr(dev1, "hasGas", True)
    print("%s" % dev1.name," => getattr(dev1, \"hasGas\") = ", getattr(dev1, "hasGas", None))
    print("%s" % dev2.name," => getattr(dev2, \"hasGas\") = ", getattr(dev2, "hasGas", None))
    print("Deleting attribute: delattr(dev1, \"hasGas\")")
    delattr(dev1, "hasGas")
    print("%s" % dev1.name," => getattr(dev1, \"hasGas\") = ", getattr(dev1, "hasGas", None))


    #4.
    print("Applying built-in func on class ")
    print(" NAME(Developer.__name__): ", Developer.__name__)
    print("DOC(Developer.__doc__): ", Developer.__doc__)
    print("DICT(Developer.__dict__): ", Developer.__dict__)
    print("MODULE(Developer.__module__): ", Developer.__module__)
    print("BASE(Developer.__bases__): ", Developer.__bases__)

    #5.
    print("Deleting object")
    del dev5
    print("DIR: ", Developer.__dict__)

    #6.
    print('Type Checking')
    print("dev4 is ", type(dev4))
    print("dev4 is instance of ", type(dev4) is Developer)



# End useDeveloper
useDeveloper()

# useEmployee: Testing employee and its subclasses
def useEmployee():
    printDes("Inheritence")
    emp1 = Employee("Kutta","Sales", "10L", "Sales exe")
    eng1 = Engineer("Laba", "Enterprise Service", "12L", "Support Dev")
    print("emp1 = ", emp1)
    print("eng1 = ", eng1)

    Employee.showDeptStat()
# End useEmployee
useEmployee()

# Operator overloading
def operatorOverloading():
    printDes("Operator overloading")
    v1 = Vector(5,10)
    v2 = Vector(2,7)
    v3 = Vector(7, 17)
    print(v1, " + ", v2, " = ", (v1 + v2))
    vadd = v1 + v2
    print(vadd, " == ", v3, " = ", vadd == v3)

    listVector = [v1, v3, v2]
    tmp = list(listVector)
    tmp.sort()

    print(strList(listVector), ".sort() => ", strList(tmp))
# end operatorOverloading
operatorOverloading()

# Data Hiding Eample
def dataHidingExample():
    printDes("Data Hiding")
    student = Student(15)
    try:
        print(" trying student.__marks = ", student.__marks)
    except AttributeError as excp:
        print("Expected AttributeError exception received: ", excp)
    # End: try
    print("Getting value through getter: student.getMarks() = ", student.getMarks())
    student.setMarks(25)
    print("Setting Value: student.setMarks(25) => student.getMarks() = ", student.getMarks())

    # Getting private value: obj._ClassName__pvtvar
    print("Backdoor to get private value: student._Student.__marks = ", student._Student__marks)
# End: dataHidingExample()
dataHidingExample()

printEnd()
