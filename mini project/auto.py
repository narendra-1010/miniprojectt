from tkinter import *
from PIL import Image,ImageTk
import mainpage
class automobile:
    
    def __init__(self):

        root = Tk()


        root.geometry("1600x900")



        canvas1 = Canvas( root, width = 1600,
                    height = 900)

        canvas1.pack(fill = "both", expand = True)

        img= (Image.open("car.jpg"))

    
        resized_image= img.resize((1600,900), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)



        canvas1.create_image( 0, 0, image = new_image,
                    anchor = "nw")


        def tvs():
            root.destroy()
            s="TVSMOTOR.NS.csv"
            firster =mainpage.code(s)
        
        def ttm():
            root.destroy()
            s="TTM.csv"
            firster =mainpage.code(s)
        def hero():
            root.destroy()
            s="HEROMOTOCO.NS.csv"
            firster =mainpage.code(s)
        def ashok():
            root.destroy()
            s="ASHOKLEY.NS.csv"
            firster =mainpage.code(s)
        def mahindra():
            root.destroy()
            s="M&M.NS.csv"
            firster =mainpage.code(s)




        l=label=Label(root,text="AUTOMOBILE INDUSTRIES",font= ('Helvetica 60'))
        button1 = Button( root,text=  "TVS  MOTORS  ", font= ('Helvetica 30'),command=tvs)
        button2 = Button( root, text= "TATA  MOTORS ", font= ('Helvetica 30'),command=ttm)
        button3 = Button( root, text= "HERO   MOTORS", font= ('Helvetica 30'),command=hero)
        button4 = Button( root, text= "ASHOK LEYLAND", font= ('Helvetica 30'),command=ashok)
        button5 = Button( root, text= "   MAHINDRA  ", font= ('Helvetica 30'),command=mahindra)
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

