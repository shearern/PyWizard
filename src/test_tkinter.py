
from Tkinter import *
#from PIL import ImageTk, Image

images = list()

def data():
    global images
    for i in range(50):
        images.append(PhotoImage(file=r"Task.gif"))

        Label(frame, text=i).grid(row=i, column=0)
        Label(frame, text="my text" + str(i)).grid(row=i, column=1)
        Label(frame, image = images[-1]).grid(row=i, column=2)

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=200, height=200)

def resize_root(event):
    global config_num
    global canvas
    global root

    print dir(root.wm_geometry())
    print root.winfo_width(), root.winfo_height()

    canvas.configure(scrollregion=canvas.bbox("all"), width=root.winfo_width()-35, height=root.winfo_height() - 35)

if __name__ == '__main__':
    root = Tk()
    sizex = 800
    sizey = 600
    posx = 100
    posy = 100
    root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

    myframe = Frame(root, relief=GROOVE, width=50, height=100, bd=1)
    myframe.place(x=10, y=10)

    canvas = Canvas(myframe)
    frame = Frame(canvas)
    myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right", fill="y")
    canvas.pack(side="left")
    canvas.create_window((0, 0), window=frame, anchor='nw')
    frame.bind("<Configure>", myfunction)
    data()

    root.bind("<Configure>", resize_root)

    root.mainloop()