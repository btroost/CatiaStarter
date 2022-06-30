#CatiaStarter
import tkinter as tk
import os
import subprocess

#######################################################################
# description
######################################################################


def start(event):
    print(" Start Catia")
    #Start-Process  -WorkingDirectory "C:\Program Files\Dassault Systemes\B30\win_b64\code\bin" -ArgumentList "-nowindow"  #-nowindow  -ArgumentList "/c dir `"%systemdrive%\program files`""
    #os.system(""C:\Program Files\Dassault Systemes\B30\win_b64\code\bin\CATSTART.exe"")
    # "-nowindow"  #-nowindow  -ArgumentList "/c dir `"%systemdrive%\program files`""

    #file = "C:/Program Files/Dassault Systemes/B30/win_b64/code/bin/CATSTART.exe"
    #subprocess.call([file])

    result = subprocess.Popen(["C:\Program Files\Dassault Systemes\DS License Server\win_b64\\code\\bin\\DSLicSrv.exe", "-admin", "-i", "c:\data\\apps\startup\dslsinput.txt", "-o", "c:\data\\apps\startup\dslsoutputpy.txt"])
    print (result)


def CheckLicense(event):
    print("Check License")
    result = subprocess.Popen(["C:\Program Files\Dassault Systemes\DS License Server\win_b64\\code\\bin\\DSLicSrv.exe", "-admin", "-i", "c:\data\\apps\startup\dslsinput.txt", "-o", "c:\data\\apps\startup\dslsoutputpy.txt"])
    #result = subprocess.Popen([r"C:\Program Files\Dassault Systemes\DS License Server\win_b64\code\bin\DSLicSrv.exe", "-admin", "-i", r"c:\data\apps\startup\dslsinput.txt", "-o", r"c:\data\apps\startup\dslsoutputpy.txt"])

    arg1=r"C:\Program Files\Dassault Systemes\DS License Server\win_b64\code\bin\DSLicSrv.exe"
    arg2=r"c:\data\apps\startup\dslsinput.txt"
    arg3=r"c:\data\apps\startup\dslsoutputpy.txt"
    #result = subprocess.Popen([arg1, "-admin", "-i", arg2, "-o", arg3])    print (result)

    f = open(arg3, "r")
    for x in f:
        print(x)


def GUI():
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

    #Check licenses
    mybutton = tk.Button(window, text = "Check License")
    mybutton.grid(column=0,row=4)
    mybutton.bind("<Button-1>",CheckLicense)


    window.mainloop()

#*************Start ProGRAM *********************************

GUI()
