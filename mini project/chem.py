from tkinter import *
from PIL import Image,ImageTk
import mainpage
class CHEM:
    
    def __init__(self):

        root = Tk()


        root.geometry("1600x900")



        canvas1 = Canvas( root, width = 1600,
                    height = 900)

        canvas1.pack(fill = "both", expand = True)

        img= (Image.open("chemical.jpg"))

    
        resized_image= img.resize((1600,900), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)



        canvas1.create_image( 0, 0, image = new_image,
                    anchor = "nw")


        def atul():
            root.destroy()
            s="ATUL.NS.csv"
            firster =mainpage.code(s)
        
        def basf():
            root.destroy()
            s="BASF.BO.csv"
            firster =mainpage.code(s)
        def guja():
            root.destroy()
            s="GUJALKALI.NS.csv"
            firster =mainpage.code(s)
        def pidi():
            root.destroy()
            s="PIDILITIND.NS.csv"
            firster =mainpage.code(s)
        def tata():
            root.destroy()
            s="TATACHEM.NS.csv"
            firster =mainpage.code(s)




        l=label=Label(root,text="CHEMICAL INDUSTRIES",font= ('Helvetica 60'))
        button1 = Button( root,text=  "Atul Ltd", font= ('Helvetica 30'),command=atul)
        button2 = Button( root, text= "BASF India Limited ", font= ('Helvetica 30'),command=basf)
        button3 = Button( root, text= "Gujarat Alkalies and Chemicals Limited", font= ('Helvetica 30'),command=guja)
        button4 = Button( root, text= "Pidilite Industries Limited", font= ('Helvetica 30'),command=pidi)
        button5 = Button( root, text= "Tata Chemicals Limited", font= ('Helvetica 30'),command=tata)
        button1_canvas = canvas1.create_window( 300, 200,
                                        anchor = "center",
                                        window = button1)

        button2_canvas = canvas1.create_window( 400, 300,
                                        anchor = "center",
                                            window = button2)
        button3_canvas = canvas1.create_window( 500, 400,
                                        anchor = "center",
                                        window = button3)
        button4_canvas = canvas1.create_window( 600, 500,
                                        anchor = "center",
                                        window = button4)
        button5_canvas = canvas1.create_window( 700, 600,
                                        anchor = "center",
                                        window = button5)
        l_canvas=canvas1.create_window(700,0,anchor='n',window=l)


# Execute tkinter
        root.mainloop()
