import mysql.connector
import tkinter as tk
from tkinter import messagebox,ttk


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cocu1"
)

mycursor=mydb.cursor()


def select_data():
    try:
        query="SELECT * FROM member_list"
        mycursor.execute(query)
        rows=mycursor.fetchall()
        return rows
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to select data from table: {error}")


root=tk.Tk()
root.geometry("400x400")
datas=select_data()


column_names = ['id','name','age','email','gender','address']

tree=ttk.Treeview(root,columns=column_names)
tree.heading('#0', text='ID')
tree.heading('id', text='newID')
tree.heading('name',text="name")
tree.heading('age',text="age")
tree.heading('email',text="email")
tree.heading('gender',text="gender")
tree.heading('address',text="address")

for data in datas:
    tree.insert("",tk.END,text=data[0],values=(data))


tree.pack()
root.mainloop()


        

