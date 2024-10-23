
import re


a = 80
b = 50

# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")


# if a > b: print("a is greater than b")

import random

a = random.randint(1, 1000)
b = random.randint(1, 1000)

# print("A") if a > b else print("B")

# total=a-b if a>b else b-a
# print(total)


# a = 700
# b = 600
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")
  
  

# i = 10

# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1


# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")
  
# for x in range(6):
#   print(x)


# for x in range(2, 6):
#   print(x)


number=[1,2,3,4,5,6,7,8,9]


# for x in range(0, 100, 5):
#   print(x)
  

# def my_function(fname):
#   print(fname + " Refsnes")
  

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# findall
# search
# split
# sub

# txt="hi, i am peter nice to meet you, i age 13 year old"


txt = "13231231241asd312323"

x = re.findall("[0-9]", txt)
print(x)



