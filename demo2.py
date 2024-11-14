import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.geometry("300x250")
root.title("Reorderable Listbox")

# Create a Listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10)
listbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Sample data to display
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"]

# Populate the Listbox with data
for item in items:
    listbox.insert(tk.END, item)

# Declare start_index as a global variable
start_index = None

# Store the initial position when the item is clicked
def on_click(event):
    global start_index
    start_index = listbox.nearest(event.y)  # Gets the item index under the mouse cursor

# Move the item to a new position while dragging
def on_drag(event):
    global start_index
    current_index = listbox.nearest(event.y)
    if current_index != start_index:  # If the cursor is over a different item
        # Swap the items at start_index and current_index
        listbox.insert(current_index, listbox.get(start_index))
        listbox.delete(start_index + (1 if current_index < start_index else 0))
        start_index = current_index  # Update start index to current position

# Bind events to handle dragging
listbox.bind("<Button-1>", on_click)    # Mouse button press to start drag
listbox.bind("<B1-Motion>", on_drag)    # Mouse drag event

# Start the Tkinter main loop
root.mainloop()
