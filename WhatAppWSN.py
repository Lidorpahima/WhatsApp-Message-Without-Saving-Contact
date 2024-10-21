from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ // This is the main window
window = tk.Tk()
window.title("WhatsApp Without Saving Number")
window.geometry("500x200")
window.resizable(False, False)
window.iconbitmap('.\icon.ico')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
background_image_path = r".\Background.png"


background_image = Image.open(background_image_path)
background_photo = ImageTk.PhotoImage(background_image)

background_label = Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def calculate():
    try:
        Number = p1.get()
        if len(Number) != 10 or not Number.isdigit():
            result_label.config(text="Please enter a valid number")
            return

        # Format the number to include +972 for Israeli numbers
        Number = "+972" + Number[1:10]
        URL = "https://wa.me/" + Number

        result_label.config(text=f"Your link is: {URL}")

        # Option to automatically open the link in a browser
        webbrowser.open(URL)
    except ValueError:
        result_label.config(text="Please enter valid numbers")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
title_label = Label(window, text="NOT Needed To Add Check Digit", font=("Arial", 10, "bold"), fg="red")
title_label.place(x=150, y=10)

lblp1 = Label(window, text="Enter Number :")
lblp1.place(x=150, y=50)

p1 = Entry(window, width=20)
p1.place(x=250, y=50)

b = Button(window, text="Generate Link", width=30, height=2, command=calculate)
b.place(x=150, y=85)

## Result label to show the generated link
result_label = Label(window, text="", font=("Arial", 14))
result_label.place(x=75, y=150)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Adding Copy and Paste functionality using keyboard shortcuts and right-click menu

def copy():
    window.clipboard_clear()
    try:
        window.clipboard_append(p1.selection_get())
    except tk.TclError:
        pass  # No selection

def cut():
    copy()
    try:
        p1.delete("sel.first", "sel.last")
    except tk.TclError:
        pass  # No selection

def paste():
    try:
        p1.insert(tk.INSERT, window.clipboard_get())
    except tk.TclError:
        pass  # Clipboard is empty or contains non-text data

# Create right-click menu
right_click_menu = Menu(window, tearoff=0)
right_click_menu.add_command(label="Cut", command=cut)
right_click_menu.add_command(label="Copy", command=copy)
right_click_menu.add_command(label="Paste", command=paste)

def show_right_click_menu(event):
    right_click_menu.tk_popup(event.x_root, event.y_root)

# Bind right-click to show menu
p1.bind("<Button-3>", show_right_click_menu)

# Bind keyboard shortcuts -SOON-
p1.bind("<Control-c>", lambda event: copy())
p1.bind("<Control-v>", lambda event: paste())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.mainloop()
