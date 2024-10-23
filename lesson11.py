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


def select_data(qry):
    try:
        tree.delete(*tree.get_children())
        mycursor.execute(qry)
        rows=mycursor.fetchall()
        
        for data in rows:
            tree.insert("",tk.END,text=data[0],values=(data[1],data[2],data[3],data[4],data[5]))
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to select data from table: {error}")


def search_data(search_text=None):
    if search_text!=None:
        query=f"SELECT * FROM member_list WHERE name LIKE '%{search_text}%' OR age LIKE '%{search_text}%' OR email LIKE '%{search_text}%' OR gender LIKE '%{search_text}%' OR address LIKE '%{search_text}%'"
        return select_data(query)
    else:
        query="SELECT * FROM member_list"
        return select_data(query)
    
def delete_data(event):
    selected_item = tree.focus()
    if selected_item:
        confirmed=messagebox.askyesno("Confirmation","Are You sure you wan to delete this record?")
        if confirmed:
            text=tree.item(selected_item,"text")
            primary_key_values=text
            # print(primary_key_values)
            qry="DELETE FROM member_list WHERE id=%s"
            val=(primary_key_values,)
            mycursor.execute(qry,val)
            mydb.commit()
            messagebox.showinfo("Success","Record deleted successfully")
            search_data()
        

root=tk.Tk()
root.geometry("400x400")


column_names = ['name','age','email','gender','address']


tree=ttk.Treeview(root,columns=column_names)

search_label=tk.Label(text="Search").grid(row=0,column=0,sticky = "W",padx=10)
search=tk.Entry(width=30)
search.grid(row=1,column=0,sticky="w",pady=10,padx=10)

search.bind("<KeyRelease>",lambda e:search_data(search.get()))

tree.heading('#0', text='ID')
tree.heading('name',text="name")
tree.heading('age',text="age")
tree.heading('email',text="email")
tree.heading('gender',text="gender")
tree.heading('address',text="address")

tree.bind("<Double-1>",delete_data)

search_data()
tree.grid(row=3,column=0,columnspan=2,pady=10,padx=10)

root.mainloop()
