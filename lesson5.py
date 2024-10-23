class MyClass:
  x=10
  y=100

# print(MyClass)

# p1 = MyClass()


print(p1.x+p1.y)


# class Person:
#   def __init__(self, name, age):
#     self.personname = name
#     self.personage = age
  
#   # personname="harray"

p1 = Person("peter ", 21)

print(p1.personname)
print(p1.personage)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"My name is {self.name}, i am now {self.age} year old"
#     # return self.age

p1 = Person("John", 36)

print(p1)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(person):
#     print("Hello my name is " + person.name)
  

p1 = Person("John", 36)
p1.myage()


#parent class
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2024)
x.welcome()


# y=Person("peter","parker")
# y.printname()


