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


column_names = ['name','age','email','gender','address']



tree=ttk.Treeview(root,columns=column_names)

search_label=tk.Label(text="Search").grid(row=0,column=0,sticky = "W",padx=10)
search=tk.Entry(width=30)
search.grid(row=1,column=0,sticky="w",pady=10,padx=10)

tree.heading('#0', text='ID')
tree.heading('name',text="name")
tree.heading('age',text="age")
tree.heading('email',text="email")
tree.heading('gender',text="gender")
tree.heading('address',text="address")

for data in datas:
    tree.insert("",tk.END,text=data[0],values=(data[1],data[2],data[3],data[4],data[5]))


tree.grid(row=3,column=0,columnspan=2,pady=10,padx=10)
root.mainloop()


        

