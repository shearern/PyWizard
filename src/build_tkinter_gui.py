
from Tkinter import *

if __name__ == '__main__':

    root = Tk()

    sizex = 325
    sizey = 600
    posx = 100
    posy = 100
    #                                 sizex, sizey, posx, powy
    root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

    task_frame = Frame(master=root, bg='#FFA233', height=200)
    task_frame.grid(row=0, ipadx=5, ipady=5, sticky=W, width=325)
    #task_frame.columnconfigure(0, weight=2)

    task = Label(master=task_frame, text="Task", bg='#33FF83')
    task.grid(row=0)

    log = Label(master=root, text="Log", bg='#339CFF')
    log.grid(row=1)

    root.mainloop()
