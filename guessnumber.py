import tkinter as tk
import random
from tkinter import messagebox


def generate_number():
    number=str(random.randint(1,999999999))
    return number


def guess():
    entrynumber=[entry.get() for entry in entries]
    checkstatus=[]
    for i,entryval in enumerate(entrynumber):
        if entryval==split[i]:
            checkstatus.append(True)
        elif entryval in split:
            checkstatus.append("Partial")
        else:
            checkstatus.append(False)
    
    checkresult(checkstatus)

def checkresult(checkstatus):
    if all(checkstatus):
        messagebox.showinfo("Congratulations","You guessed the number!")
        for i,status in enumerate(checkstatus):
            tk.Label(root,text=split[i],bg="green").grid(row=1,column=i,sticky="nsew",padx=10)
    else:
        messagebox.showinfo("Sorry","You did not guess the number. Try again!")
        for i,status in enumerate(checkstatus):
            if status==True:
                tk.Label(root,text=split[i],bg="green").grid(row=1,column=i,sticky="nsew",padx=10)
            elif status=="Partial":
                tk.Label(root,text=split[i],bg="yellow").grid(row=1,column=i,sticky="nsew",padx=10)
            else:
                tk.Label(root,text=split[i],bg="red").grid(row=1,column=i,sticky="nsew",padx=10)


random_number=generate_number()

split=list(random_number)


root=tk.Tk()
root.geometry("500x200")

entries=[]
for i,digit in enumerate(split):
    # print(enumerate(split))
    entry = tk.Entry(root, width=5)
    entry.grid(row=0,column=i,sticky="nsew",padx=10)
    entries.append(entry)
    
# print(entries)
button=tk.Button(root,text="Guess",command=lambda:guess()).grid(row=2,column=0,sticky="n",padx=20,pady=10,columnspan=len(split))

root.mainloop()