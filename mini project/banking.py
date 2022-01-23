from tkinter import *
from PIL import Image,ImageTk
import mainpage
class bank:
    
    def __init__(self):

        root = Tk()


        root.geometry("1600x900")



        canvas1 = Canvas( root, width = 1600,
                    height = 900)

        canvas1.pack(fill = "both", expand = True)

        img= (Image.open("bank.jpg"))

    
        resized_image= img.resize((1600,900), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)



        canvas1.create_image( 0, 0, image = new_image,
                    anchor = "nw")


        def axis():
            root.destroy()
            s="AXISBANK.NS.csv"
            firster =mainpage.code(s)
        
        def hdfc():
            root.destroy()
            s="HDFCBANK.NS.csv"
            firster =mainpage.code(s)
        def icic():
            root.destroy()
            s="ICICBANK.NS(2).csv"
            firster =mainpage.code(s)
        def sbi():
            root.destroy()
            s="SBIN.NS.csv"
            firster =mainpage.code(s)
        def kotak():
            root.destroy()
            s="KOTAKBANK.NS.csv"
            firster =mainpage.code(s)




        l=label=Label(root,text="BFSI-Banking, Financial Services and Insurance",font= ('Helvetica 40'))
        button1 = Button( root,text=  "Axis Bank", font= ('Helvetica 30'),command=axis)
        button2 = Button( root, text= "HDFC Bank", font= ('Helvetica 30'),command=hdfc)
        button3 = Button( root, text= "ICIC BANK ", font= ('Helvetica 30'),command=icic)
        button4 = Button( root, text= "STATE BANK OF INDIA", font= ('Helvetica 30'),command=sbi)
        button5 = Button( root, text= "Kotak Mahindra Bank", font= ('Helvetica 30'),command=kotak)
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
