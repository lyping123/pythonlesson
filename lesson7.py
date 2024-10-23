# try catch exception handling


# print(x)


# try:
#   print(x)
#   print("success")
# except:
#   print("An exception occurred")


# x=1
# y="2"



# try:
#   x=1
#   y="2"
#   print(x)
#   print(x+y)
# except NameError as e:
#   print(e)
# except Exception as e:
#   print(e)
  
# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")
  
  
# try:
#   a=1
#   print(a)
  
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")
  
# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")
  

# for i in range(1,100):
  
#   if i > 11:
#     raise Exception("Sorry, no numbers above 11")



array=[1,3,4,6,7,-1,9,2]

for i in array:
  
  if i < 0:
    raise ValueError("Negative numbers are not allowed")
    


# x = "hello"

# if not type(x) is int:
#   raise TypeError("Only integers are allowed")




