#rabiobuttons = similar to checkboxes but you can only pick 1 in the group

from tkinter import *

def cashier():
    if x.get()==0:
        print("You have picked the burger, that will be $5")
    elif x.get()==1:
        print("You have picked the fries, that will be $2")
    elif x.get()==2:
        print("You have picked the soda, that will be $1")
    else:
        print("huh?")

food = ["Burger", "Fries", "Soda"]

window = Tk()

x = IntVar()

for i in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[i],
                               variable=x,
                               value=i,
                               command=cashier,
                               indicatoron=0,#removing the cirular check box, and changing it to buttons instead
                               width=30)#width of the buttons

    radio_button.pack(anchor=W)

window.mainloop()