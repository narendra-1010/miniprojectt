from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
class Main_Page:
    def __init__(self, root, ls):
        self.root = root
        self.ls = ls
        # Creating the first frame.



        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])
        
        # Creating the first frame.
        
        self.frame1 = Frame(self.frame, bg='#ffffff')
        self.frame1.place(x=ls[0]//14*2, y=ls[1]//4, width=ls[0]//12*9, height=ls[1]//4*2)

        # Taking All pics in the variable.
        self.photo_auto = PhotoImage(file=r"Images/auto.png")
        self.photo_chemical = PhotoImage(file=r"Images/chem.png")
        self.photo_agro = PhotoImage(file=r"Images/agro.png")
        self.photo_BFSI = PhotoImage(file=r"Images/banking.png")
        #self.photo_ = PhotoImage(file=r"Images/autoo.png")


        # Resizing the Images as per requirement.
        self.photo_auto = self.photo_auto.subsample(8, 8)
        self.photo_chemical = self.photo_chemical.subsample(8, 8)
        self.photo_agro = self.photo_agro.subsample(8, 8)
        self.photo_BFSI = self.photo_BFSI.subsample(8, 8)
        def at():
            import auto
            self.root.destroy()
            firster =auto.automobile()

        def chemical():
            import chem
            self.root.destroy()
            firster =chem.CHEM()
        def agr():
            import agro
            self.root.destroy()
            firster =agro.agri()
        def bfsi():
            import banking
            self.root.destroy()
            firster =banking.bank()
            

        # Title for Register/Login.
        self.title1 = Label(self.frame1, text='SECTORS', font=('Algerian', 25, 'bold'), bg='#ffffff').pack(side=TOP)

        # Creating two buttons.
        self.auto_btn = Button(self.frame1, text='automobile', bd=0, bg='#ffffff', image=self.photo_auto,
                                   compound=TOP, command=at) \
            .place(width=ls[0] // 14, height=ls[1] // 3, x=(ls[0]//12)*3-ls[0]//10*2, y=(ls[1] // 3)-ls[1]//4)

        self.chemical_btn = Button(self.frame1, text="chemical", bd=0, bg='#ffffff', image=self.photo_chemical,
                                  compound=TOP, command=chemical) \
            .place(width=ls[0] // 14, height=ls[1] // 3, x=(ls[0]//12 * 5)-ls[0]//10*2, y=(ls[1] // 3)-ls[1]//4)

        self.AGRO_btn = Button(self.frame1, text="agro", bd=0, bg='#ffffff', image=self.photo_agro,
                                   compound=TOP, command=agr) \
            .place(width=ls[0] // 14, height=ls[1] // 3, x=(ls[0]//12* 7)-ls[0]//10*2, y=(ls[1] // 3)-ls[1]//4)
        
        self.BFSI_btn = Button(self.frame1, text="BFSI", bd=0, bg='#ffffff', image=self.photo_BFSI,
                                  compound=TOP, command=bfsi) \
            .place(width=ls[0] // 14, height=ls[1] // 3, x=(ls[0]//12 * 9)-ls[0]//10*2, y=(ls[1] // 3)-ls[1]//4)
        
