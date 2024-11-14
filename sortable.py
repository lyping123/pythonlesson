import mysql.connector
import tkinter as tk
import tkinter.messagebox as ms
from tkinter import ttk 


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "cocu1"
)


mycursor = mydb.cursor()

def submit():
    try:
        insert= "insert into `member_list` (`name`, `age`, `email`, `gender`, `address`) values (%s, %s, %s, %s, %s)"
        mycursor.execute(insert,(entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get()))
        mydb.commit()
        
        ms.showinfo("Success","Record inserted successfully into memberlist table")
    except mysql.connector.Error as error:
        ms.showerror("Error","Failed to insert record into memberlist table".format(error))
        

def fetch_data():
    if entry.get() == '':
        query='SELECT * FROM `member_list`'
        mycursor.execute()
    else:
        query='SELECT * FROM `member_list` WHERE `name` LIKE %s OR `age` LIKE %s OR `email` LIKE %s OR `gender` LIKE %s OR `address` LIKE %s'
        queryvalue=(entry.get(),entry.get(),entry.get(),entry.get(),entry.get())
        mycursor.execute(query,queryvalue)
    mycursor.fetchall()
    tree.delete(*tree.get_children())
    for i in mycursor:
        tree.insert("", "end", values=i)


        
root = tk.Tk()
root.geometry("500x500")

        
tk.Label(root, text="Username").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Age").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Email").pack()

entry3 = tk.Entry(root)
entry3.pack()


tk.Label(root, text="Gender").pack()

entry4 = tk.Entry(root)
entry4.pack()


tk.Label(root, text="Address").pack()

entry5 = tk.Entry(root)
entry5.pack()


tk.Button(root, text="submit",command=submit).pack()
columns_name = ("id","Name", "Age", "Email", "Gender", "Address")         
        
tree = ttk.Treeview(root,column=columns_name, show="headings")        
tree.heading("#0", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Email", text="Email")
tree.heading("Gender", text="Gender")
tree.heading("Address", text="Address")

tree.pack()

entry=tk.Entry(root)
tk.Label(root,text="search").pack()
entry.bind('<KeyRelease>',lambda: fetch_data)
entry.pack()
fetch_data()

root.mainloop()