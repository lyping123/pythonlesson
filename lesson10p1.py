import tkinter as tk

from tkinter import ttk,messagebox



root = tk.Tk()
root.title("Treeview in Tk")
treeview = ttk.Treeview()

# treeview.insert("", tk.END, text="Item 1")

# item = treeview.insert("", tk.END, text="Item 1")
# treeview.insert(item, tk.END, text="Subitem 1")


# subitem = treeview.insert(item, tk.END, text="Subitem 1")
# treeview.insert(subitem, tk.END, text="Another item")


# my_iid = "unique_id"
# treeview.insert("", tk.END, text="Item 1", iid=my_iid)

# treeview = ttk.Treeview(columns=("size", "lastmod"))
# treeview.heading("#0", text="File")
# treeview.heading("size", text="Size")
# treeview.heading("lastmod", text="Last modification")

item1 = treeview.insert("", tk.END, text="Item 1")
item2 = treeview.insert("", tk.END, text="Item 2")

# # treeview.move(item1, item2, tk.END)
# treeview.delete(item2)


item=treeview.insert(
    "",
    tk.END,
    text="README.txt",
    values=("850 bytes", "12:30")
)


# treeview.set(item, "lastmod", "19:30")

treeview.pack()

root.mainloop()