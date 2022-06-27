#CatiaStarter
import tkinter as tk
import os
import subprocess


def start(event):
    print(" Start Catia")
    #os.system(r"C:\Data\xxx2XMLnew\otr.bat")

    #a = subprocess.check_output("batch_1.bat")
    #print a

window=tk.Tk()
window.title(" Catia Starter ")
window.geometry("600x400")

# Usage Scope
newlabel = tk.Label(text = " Select your Usagescope ")
newlabel.grid(column=0,row=0)
dropdown1=tk.OptionMenu(window,tk.IntVar(),"Papendrecht","Hoogerheide","Helmond","Filton")
dropdown1.grid(column = 1, row=0)

# Program
newlabel = tk.Label(text = " Select your Program ")
newlabel.grid(column=0,row=1)
dropdown=tk.OptionMenu(window,tk.IntVar(),"Airbus","JSF","Gulfstream","Eviation")
dropdown.grid(column = 1, row=1)

# LicenseRole
newlabel = tk.Label(text = " Select your LicenseRole ")
newlabel.grid(column=0,row=2)
dropdown=tk.OptionMenu(window,tk.IntVar(),"Basic Design","Advanced Design","Composite Design","Machining")
dropdown.grid(column = 1, row=2)

#Start Catia
mybutton = tk.Button(window, text = "Start Catia")
mybutton.grid(column=1,row=3)
mybutton.bind("<Button-1>",start)


window.mainloop()


print("test")
