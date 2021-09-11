from tkinter import *

def display():
    if x.get() == 1:
        print("you agree")
    else:
        print("you don't agree")

window = Tk()

x = IntVar() #Can be BooleanVar, StringVar, etc. according to the onvalue and offvalue

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display)

check_button.pack()

window.mainloop()