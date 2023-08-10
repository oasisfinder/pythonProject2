from tkinter import *
import tkinter.messagebox

root = Tk()
label = Label(root, text='기여운거 볼래?')
label.pack()

b1 = Button(root, text='웅', width = 10)
b1.pack(side=LEFT)

b2 = Button(root, text='아니', width = 10)
b2.pack(side=LEFT)


def btn_click(event):
    tkinter.messagebox.showinfo("바보","바보야 속았지")

def btn_click2(event):
    tkinter.messagebox.showinfo("바보","바보야 왜안봐")

b1.bind('<Button-1>', btn_click)
b2.bind('<Button-1>', btn_click2)


root.mainloop()
