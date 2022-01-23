from tkinter import *
from tkinter import ttk


import HomePage
class start:
    def __init__(self):
    # Getting the screensize in list.
            ls = list([1640, 830])
       #print(ls)
        # Creating a fixed window.
            root = Tk()
        # Creating a bit icon.
            root.iconbitmap('icon.ico')

        # Title and Screen Setting.
            root.title("Stock Market forecast")  # Sets-up the title of the window.
            root.geometry(f"{ls[0]}x{ls[1]}+0+0")  # Width Height Left-padding Top-padding.

            root.configure(bg='blue')  # Setting the background.

        # Starting the first window.
            firster = HomePage.Main_Page(root, ls)

        # Starting a main window.
            root.mainloop()
