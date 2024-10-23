import mysql.connector
import tkinter as tk
import tkinter.messagebox as msg

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cocu1"
)

mycursor=mydb.cursor()

def insert_data():
    try:
        username=entry.get()
        age=entry2.get()
        sql="INSERT INTO member_list(name,age) VALUES (%s,%s)"
        val=(username,age,)
        mycursor.execute(sql,val)
        mydb.commit()
        msg.showinfo("Success","Data inserted successfully")
    except Exception as e:
        msg.showerror("Error",str(e))


# input1=input("please insert you username:")

# input2=input("please insert you age:")

# insert_data(input1,input2)

root=tk.Tk()
root.geometry("500x500")
tk.Label(root,text="Please insert your username").grid(row=0,column=0)

entry=tk.Entry(root)
entry.grid(row=1,column=0)
tk.Label(root,text="Age").grid(row=2,column=0)
entry2=tk.Entry(root)
entry2.grid(row=3,column=0)

Button=tk.Button(root,text="Insert",command=lambda:insert_data())

Button.grid(row=4,column=0)

root.mainloop()


