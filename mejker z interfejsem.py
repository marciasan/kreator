from tkinter import *
import random

def zwrot():
    print("\n\n")
    for i in range(0,8):
        lines = open('Baza.txt').read().splitlines(2)
        myline =random.choice(lines)
        
        label = Label(text = myline, bg = "pink")
        label.pack()

root = Tk()
root.title("Zapraszam do wspólnej zabawy!")
root.config(bg = "pink")

#Przycisk
bt_1 = Button(text = "Kliknij tu by wygenerować...", relief = GROOVE, bg = "#ff0099", command = zwrot)
photo = PhotoImage(file="zenus.png")
bt_1.config(image = photo, compound = TOP)
bt_1.pack()


root.mainloop()

