#import the 'tkinter module
from tkinter import*
root = Tk() # Blank window
root.geometry("550x350")
#adding a background colour
root.config(bg='Pink')
#create the title for the window
root.title("Temperature Convertor")

#creating textbox widgets (Convert from Celcius to Fahrenheit)
cel_fah = Text (root, width= 20, height = 5, bg = "white", font = ("Helvetica", 16))
cel_fah.grid(row = 3, column = 5, padx = 200, pady=100)

#creating textbox widgets (Convert from Fahrenheit to Celcius)
fah_cel = Text (root,width= 20, height = 5, bg = "white", font = ("Helvetica", 16))
fah_cel.grid (row = 3, column = 15, padx = 200, pady=100)


#Creating a Frame for the buttons
#button_frame = Frame (root)
#button_frame.pack()

#Creating the label
label_dis = Label (root,width= 20, height = 5, bg = "lime", font = ("Helvetica", 16))


#functions
def button_clear ():
#clearing the textboxes and the label field
    cel_fah.delete(0, END)
    fah_cel.delete(0, END)
    label_dis.delete(0, END)


def button_celfah ():
    celcius_val =  cel_fah.get(); #Getting the values from the textboxes
    fahrenheit = celcius_val*9/5+32 #Converting celcius to Fahrenheit button
    label_dis.insert(0, fahrenheit)
    label_dis.delete(0, END)


def button_fahcel ():
    fahrenheit_val = fah_cel().get(); #Getting the values from the textboxes
    celcius = (fahrenheit_val-32*5/9) #Converting Fahrenheit to celcius
    label_dis.insert(0, celcius)
    label_dis.delete(0, END)

def button_exit ():
#EXITING
    import sys
    sys.exit()
#exits the program

# Buttons
button_celfah = Button(root,  borderwidth=10, font=("Consolas 10 bold"),text="Activate-Celcius to Fahrenheit", bg="green", fg="white", width=30, command=button_celfah)
button_fahcel = Button(root, text="Activate-Fahrenheit to Celcius", borderwidth=10, font=("Consolas 10 bold"), bg="green", fg="white", width=30, command=button_fahcel)
button_exit = Button(root, text="Exit", borderwidth=10, font=("Consolas 10 bold"), bg="green", fg="white", width=10, command=button_exit)
button_clear = Button (root, borderwidth=10, font=("Consolas 10 bold"),text="Clear", bg="green", fg="white", width=10, command=button_clear)
button_conversion = Button (root, borderwidth=10, font=("Consolas 10 bold"),text="Conversion", bg="green", fg="white", width=10)
#display

#grid (row = 3, column = 5, padx = 200, pady=100)

button_celfah.grid(row = 4, column = 5)
button_fahcel.grid(row = 4, column = 15)
button_clear.place (x=600, y = 500)
button_conversion.place(x=600, y = 700)
#button_exit.place(x=100, y=70)
#label_dis.place(x=90, y=90)

root.mainloop()
