import mysql.connector
import tkinter as tk
from tkinter import messagebox,ttk


root=tk.Tk()
root.title("Demo2")
root.geometry("200x200")
# button1=tk.Button(text="Left",height=15,width=30).grid(row=0,column=0,sticky="w",)
# button1=tk.Button(text="Center",height=15,width=30).grid(row=0,column=1)
# button2=tk.Button(text="Right",height=15,width=30).grid(row=0,column=2,sticky="e")
# tk.Button(text="1",height=2,width=5).grid(row=0,column=0,sticky="e")
# tk.Button(text="2",height=2,width=5).grid(row=1,column=1,sticky="e")
# tk.Button(text="3",height=2,width=5).grid(row=2,column=2,sticky="e")
# tk.Button(text="4",height=2,width=5).grid(row=3,column=3,sticky="e")
# tk.Button(text="5",height=2,width=5).grid(row=4,column=4,sticky="e")
# tk.Button(text="6",height=2,width=5).grid(row=5,column=5,sticky="e")
# tk.Button(text="7",height=2,width=5).grid(row=6,column=6,sticky="e")
# tk.Button(text="8",height=2,width=5).grid(row=7,column=7,sticky="e")
# tk.Button(text="9",height=2,width=5).grid(row=8,column=8,sticky="e")
# tk.Button(text="10",height=2,width=5).grid(row=9,column=9,sticky="e")

tk.Button(text=1,height=2,width=15).grid(row=0,column=0,columnspan=5)


tk.Button(text=2,height=2,width=5).grid(row=1,column=0,columnspan=2)
tk.Button(text=2,height=2,width=5).grid(row=1,column=3,columnspan=2)


tk.Button(text=3,height=2,width=5).grid(row=2,column=0)
tk.Button(text=3,height=2,width=5).grid(row=2,column=1)
tk.Button(text=3,height=2,width=5).grid(row=2,column=3)
tk.Button(text=3,height=2,width=5).grid(row=2,column=4)


tk.mainloop()


