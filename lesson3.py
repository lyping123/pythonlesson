# python code for lists and dictionaries
thislist = ["apple", "banana", "cherry","orange","pineapple"]

# print(thislist[1])


thislist = ["apple", "banana", "cherry"]

# print(thislist[-1])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# print(thislist[2:5])



# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])


thislist = [2,3,5,9,7,3,1]

# thislist.sort()
# print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

# thislist.sort(reverse = True)
# print(thislist)



# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)



thislist = ["apple", "banana", "cherry"]

mylist = thislist.copy()
print(mylist)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# #dictionary
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# for x in thisdict.valuesx():
#   print(x)


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x in myfamily:
  print(myfamily[x]["year"])
  

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print( myfamily.items())
for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])


