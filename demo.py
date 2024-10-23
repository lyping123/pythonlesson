import mysql.connector
import tkinter as tk
import tkinter.messagebox as ms


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
        ms.showerror("Error","Failed to insert record into memberlist table {}".format(error))
        
        
root = tk.Tk(className="weisheng")

tk.Label(root, text="Username").pack()

entry1 = tk.Entry()
entry1.pack()


tk.Label(root, text="Age").pack()

entry2 = tk.Entry()
entry2.pack()


tk.Label(root, text="Email").pack()

entry3 = tk.Entry()
entry3.pack()


tk.Label(root, text="Gender").pack()

entry4 = tk.Entry()
entry4.pack()


tk.Label(root, text="Address").pack()

entry5 = tk.Entry()
entry5.pack()


tk.Button(root, text="submit",command=submit).pack()




root.mainloop()