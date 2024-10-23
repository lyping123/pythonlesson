import mysql.connector

# pip install mysql-connector-python

#servername=abcserver.com
#username=abcuser
#password=abc123




mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

mycursor=mydb.cursor()


# database=mycursor.execute("SHOW DATABASES")
# print(database)

# SHOW DATABASES
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO customers (name, address,gender,age,email) VALUES (%s,%s)"
# val = ("John", "Highway 21")
mycursor.execute(sql, ("John", "Highway 21"))
mydb.commit()

sql="SELECT * FROM customers WHERE address=%s"
mycursor.execute(sql,('highway 21',))

data=mycursor.fetchall()


# print(data)
for i in data:
  print(f"{i[0]} is locate at {i[1]}")
  
# update="UPDATE customers SET address=%s WHERE name=%s"
# mycursor.execute(update,('new address', 'John'))
# mydb.commit()


# delete="DELETE FROM customers WHERE name=%s"
# mycursor.execute(delete,('John',))
# mydb.commit()
# insert update delete







  



