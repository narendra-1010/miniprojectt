# Import module
from tkinter import *
from PIL import Image,ImageTk
import StartingFile
root = Tk()

# Adjust size
root.geometry("1640x830")

# Add image file
#bg = PhotoImage(file = "bull.png")

# Create Canvas
canvas1 = Canvas( root, width = 1640,
				height = 830)

canvas1.pack(fill = "both", expand = True)

img= (Image.open("bull.jpg"))

#Resize the Image using resize method
resized_image= img.resize((1640,830), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)



# Display image
canvas1.create_image( 0, 0, image = new_image,
					anchor = "nw")


def st():
    root.destroy()
    firster = StartingFile.start()
    
# Create Buttons
l=label=Label(root,text="Stock Market Forecast Application",font= ('Helvetica 30'))
button1 = Button( root,text= "Sectors", font= ('Helvetica 30'),command=st)
button2 = Button( root, text= "WATCH-LIST", font= ('Helvetica 30'))

# Display Buttons
button1_canvas = canvas1.create_window( 300, 400,
									anchor = "center",
									window = button1)

button2_canvas = canvas1.create_window( 800, 400,
									anchor = "center",
                                        window = button2)
l_canvas=canvas1.create_window(700,0,anchor='n',window=l)


# Execute tkinter
root.mainloop()
