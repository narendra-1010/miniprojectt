from tkinter import *
from PIL import Image,ImageTk
import mainpage
class agri:
    
    def __init__(self):

        root = Tk()


        root.geometry("1600x900")



        canvas1 = Canvas( root, width = 1600,
                    height = 900)

        canvas1.pack(fill = "both", expand = True)

        img= (Image.open("agriculture.jpg"))

    
        resized_image= img.resize((1600,900), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)



        canvas1.create_image( 0, 0, image = new_image,
                    anchor = "nw")


        def bbtc():
            root.destroy()
            s="BBTC.NS.csv"
            firster =mainpage.code(s)
        
        def good():
            root.destroy()
            s="GOODRICKE.BO.csv"
            firster =mainpage.code(s)
        def jkagri():
            root.destroy()
            s="JKAGRI.BO.csv"
            firster =mainpage.code(s)
        def kscl():
            root.destroy()
            s="KSCL.NS.csv"
            firster =mainpage.code(s)
        def msl():
            root.destroy()
            s="MSL.BO.csv"
            firster =mainpage.code(s)




        l=label=Label(root,text="AGRO-BASED INDUSTRIES",font= ('Helvetica 60'))
        button1 = Button( root,text=  "Goodricke Group Limited", font= ('Helvetica 30'),command=good)
        button2 = Button( root, text= "Bombay Burmah Trading Corporation", font= ('Helvetica 30'),command=bbtc)
        button3 = Button( root, text= "JK Agri Genetics Limited ", font= ('Helvetica 30'),command=jkagri)
        button4 = Button( root, text= "Kaveri Seed Company ", font= ('Helvetica 30'),command=kscl)
        button5 = Button( root, text= "Mangalam Seeds   ", font= ('Helvetica 30'),command=msl)
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
