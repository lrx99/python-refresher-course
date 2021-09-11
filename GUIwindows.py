#widgets = GUI elements: buttons, textboxes, labels, images
#windows = serves as a container to hold or contain these widgets
#label = an area widget that holds text and/or an image in a window

from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("1000x1000") #width x height
window.title("Calvin's window")

#changing the icon of the window
icon = PhotoImage(file="C:\\Users\\LRXCalvin\\Downloads\\lock screen.png")# jpeg file does not work with tkinter Photoimage
window.iconphoto(True, icon)

#changing the background color of the window
window.config(background='#5cfcff')

#placing a label in the window
label = Label(window,
              text="Hello world",
              bg='black',
              font=('Ariel', 40, 'bold'),
              fg='red',
              relief=RAISED,
              bd=10)
"""           image=icon,
              compound="bottom")"""
#label.place(x=0, y=0) #where the text going to placed at on the window x, y coordinates
label.pack() #both .place and .pack can put the label on the window

#Label(the_container(aka master), text)
#font('font name', size, bold/italic, etc.)
#fg: is the word color, can be hex to be specific or color name to be generic
#bg: short-form for background
#relief: border style
#bd: border size
#padx, pady: spacing out the word x and y axis
#compound: placement of the photo in the label("bottom"/"top")

#placing a button on window

def click ():
    print("Thanks for liking this page!")

button = Button(window,
                text= "like",
                command=click,
                font=("Comic sans",40),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE)

#activeforeground, activebackground: when click what color does it show when its pressed
#state: to allow the user to use the button anot

button.pack()

#entry widget: textbox that accepts s single line of user inputs

def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)#After the user types in, the user cannot edit it anymore

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END) # entry.delete(cursor at the character before the last character, cursor at the last character)

entry = Entry(window,
              font=("Arial", 40),
              show="*")#Will show * when user enters any character
#We can edit the widgets using widget_name.config(text="", font="", etc.)

submit_button = Button(window,
                text="Submit",
                font=("Arial",25),
                command=submit)

delete_button = Button(window,
                       text="Delete",
                       font=("Arial",25),
                       command=delete)

backspace_button = Button(window,
                       text="Backspace",
                       font=("Arial",25),
                       command=backspace)


submit_button.pack(side=RIGHT)
delete_button.pack(side=RIGHT)
backspace_button.pack(side=RIGHT)
entry.pack(side=RIGHT)


window.mainloop() #place a window on screen and listen for events