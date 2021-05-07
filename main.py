#import the 'tkinter module
import string
from tkinter import*
root = Tk() # Blank window
root.geometry("1000x800")
#adding a background colour
root.config(bg='yellow')
#Can't change the size and shape of the window
root.resizable(width=False, height=False) #The set size cannot be changed
#Title for the window
root.title("Celsius to Fahrenheit Convertor!")
#The label frames
label_celfah = LabelFrame(root, text = "Celsius to Fahrenheit", fg="purple", font = ("Helvetica", 10)) # The labels must be purple when enabled
label_fahcel = LabelFrame (root, text = "Fahrenheit to Celsius", fg="purple", font = ("Helvetica", 10))
label_celfah.place(x=150, y=50, width=300, height=200)
label_fahcel.place(x=550, y=50, width=300, height=200)

#Creating the textbox widgets
fah_cel = Entry (label_fahcel, state = "disabled")
fah_cel.place (x=50, y=50, width=180, height = 30)
cel_fah = Entry (label_celfah, state = "disabled")
cel_fah.place(x=50, y=50, width=180)

#The output displaying widget
display_output = Entry (root, width=20, font = ("Helvetica", 20))
display_output.configure(bg='lime')


#functions: Showing the work that the buttons do
def button_clear ():
#clearing the textboxes and the label field
    cel_fah.delete(0, END)
    fah_cel.delete(0, END)
    display_output.delete(0, END)
#If the clear button is pressed without an answer on the entry field, all the fields must be disabled
    cel_fah.configure(state = 'disable')
    fah_cel.configure(state = 'disable')
    display_output.configure(state ='disable')

def button_celfah ():
    cel_fah.configure(state = 'normal')
    fah_cel.configure(state = 'disabled')

def button_fahcel ():
    fah_cel.configure(state = 'normal')
    cel_fah.configure(state = 'disabled')


def button_conv_celfah ():
    temp = float(cel_fah.get()) #Getting the value from the entry box
    fahrenheit = (temp*9/5)+32 #Converting celcius to Fahrenheit button
    display_output.insert(0, fahrenheit)


def button_conv_fahcel ():
    temp = float(fah_cel.get()); #Getting the values from the entry box
    celcius = (temp-32)*5/9 #Converting Fahrenheit to celcius
    display_output.insert(0, celcius)

#The button exits the program
def button_exit ():
    #EXITING
    import sys
    sys.exit()

# Creating, positioning and commanding the buttons
button_celfah = Button(root,  borderwidth=10, font=("Consolas 10 bold"),text="Activate-Celcius to Fahrenheit", bg="green", fg="white", width=27, command=button_celfah)
button_fahcel = Button(root, text="Activate-Fahrenheit to Celcius", borderwidth=10, font=("Consolas 10 bold"), bg="green", fg="white", width=27, command=button_fahcel)
button_exit = Button(root, text="Exit", borderwidth=10, font=("Consolas 10 bold"), bg="green", fg="white", width=10, command=button_exit)
button_clear = Button (root, borderwidth=10, font=("Consolas 10 bold"),text="Clear", bg="green", fg="white", width=10, command=button_clear)
button_conv_celfah = Button (root, borderwidth=10, font=("Consolas 10 bold"),text="Conversion1", bg="green", fg="white", width=10, command = button_conv_celfah)
button_conv_fahcel = Button (root, borderwidth=10, font=("Consolas 10 bold"),text="Conversion2", bg="green", fg="white", width=10, command = button_conv_fahcel)


button_celfah.place (x=170, y=300)
button_fahcel.place( x=570, y=300)
button_clear.place (x=170, y = 500)
button_conv_celfah.place(x=170, y= 400)
button_conv_fahcel.place(x=565, y=400)
button_exit.place(x=170, y=600)
display_output.place(x=550, y=550)

root.mainloop()
