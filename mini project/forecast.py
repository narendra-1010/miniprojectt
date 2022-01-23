from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

class stocks:
    def __init__(self,train,valid,p):
        self.train=train
        self.valid=valid
        self.p=p
        window = Tk()

# setting the title
        window.title(self.p)

# dimensions of the main window
        window.geometry("1640x830")
        fig = Figure(figsize = (10, 10),
                    dpi = 100)
        plot1 = fig.add_subplot(111)
        plot1.plot(self.train['Close'])
        plot1.plot(self.valid[['Close','Predictions']])
    
        canvas = FigureCanvasTkAgg(fig,master = window)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas,window)
        toolbar.update()
        canvas.get_tk_widget().pack()
        window.mainloop()