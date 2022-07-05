#CatiaStarter
import tkinter as tk
from tkinter import ttk
import os
import subprocess
#import xml.dom.minidom
import xml.etree.ElementTree as ET

#######################################################################
# description
######################################################################



def getsettingsdata():
    print("getsettingsdata")

    Settings = []
    Usagescope = []
    Programs = []
    LicenseRole =[]

    root = ET.parse(Settingsdir + 'usagescope.xml').getroot()
    for scope in root.findall("./usagescopes/usagescope"):
        Usagescope.append(scope.get('name'))
    Settings.append(Usagescope)

    root = ET.parse(Settingsdir + 'programs.xml').getroot()
    for program in root.findall("./programs/program"):
        Programs.append(program.get('name'))
    Settings.append(Programs)
    program="insettingsdata"

    root = ET.parse(Settingsdir + 'licenserole.xml').getroot()
    for program in root.findall("./licenseroles/role"):
        LicenseRole.append(program.get('name'))
    Settings.append(LicenseRole)
    return Settings

def ddProgramAction(choice):
    choice = proglist.get()
    print(choice)

def ddUsageAction(choice):
    choice = usagelist.get()
    print(choice)

def ddLicenseAction(choice):
    choice = licenselist.get()
    print(choice)

def GUI(settings):
    global window
    program="tbd"

    window=tk.Tk()
    window.title(" Catia Starter ")
    window.geometry("600x400")

    # Usage Scope
    newlabel = tk.Label(text = " Select your Usagescope ")
    newlabel.grid(column=0,row=0)

    usagescope = []
    for usage in settings[0]:
        usagescope.append(usage)
    global usagelist
    usagelist = tk.StringVar()
    if len(usagescope) > 0 :
        usagelist.set(usagescope[0])
    dropdown = tk.OptionMenu(
        window,
        usagelist,
        *usagescope,
        command=ddUsageAction
    )
    dropdown.grid(column = 1, row=0)

    # Program
    newlabel = tk.Label(text = " Select your Program ")
    newlabel.grid(column=0,row=1)
    programs = []
    for progs in settings[1]:
        programs.append(progs)
    global proglist
    proglist = tk.StringVar()
    if len(programs) > 0 :
        proglist.set(programs[0])
    dropdown = tk.OptionMenu(
        window,
        proglist,
        *programs,
        command=ddProgramAction
    )
    dropdown.grid(column = 1, row=1)

    # LicenseRole
    newlabel = tk.Label(text = " Select your LicenseRole ")
    newlabel.grid(column=0,row=2)

    license = []
    for licrole in settings[2]:
        license.append(licrole)
    global licenselist
    licenselist = tk.StringVar()
    if len(license) > 0 :
        licenselist.set(license[0])
    dropdown = tk.OptionMenu(
        window,
        licenselist,
        *license,
        command=ddLicenseAction
    )
    dropdown.grid(column = 1, row=2)

    # Button Check licenses
    mybutton = tk.Button(window, text = "Check License")
    mybutton.grid(column=0,row=3)
    mybutton.bind("<Button-1>",CheckLicense)

    # Button Start Catia
    mybutton = tk.Button(window, text = "Start Catia")
    mybutton.grid(column=1,row=4)
    mybutton.bind("<Button-1>",Start)

    window.mainloop()

def CheckLicense(event):
    # 1) check license
    # 2) copy licensefile
    print("Check License")
    result = subprocess.Popen(["C:\Program Files\Dassault Systemes\DS License Server\win_b64\\code\\bin\\DSLicSrv.exe", "-admin", "-i", "c:\data\\apps\startup\dslsinput.txt", "-o", "c:\data\\apps\startup\dslsoutputpy.txt"])
    #result = subprocess.Popen([r"C:\Program Files\Dassault Systemes\DS License Server\win_b64\code\bin\DSLicSrv.exe", "-admin", "-i", r"c:\data\apps\startup\dslsinput.txt", "-o", r"c:\data\apps\startup\dslsoutputpy.txt"])

    arg1=r"C:\Program Files\Dassault Systemes\DS License Server\win_b64\code\bin\DSLicSrv.exe"
    arg2=r"c:\data\apps\startup\dslsinput.txt"
#    arg3=r"c:\data\apps\startup\dslsoutputpy.txt"
    myworkdir = my_env["TEMP"]
    #my_env.get("TEMP", '') in case temp does not exist..
    arg3=myworkdir + "\\dslsoutputpy.txt"
    result = subprocess.Popen([arg1, "-admin", "-i", arg2, "-o", arg3])
    print (result)

    f = open(arg3, "r")
    for x in f:
        print(x)

def Start(event):
#    print(" Start Catia")
    program=proglist.get()
#    print (program)

    #Get variables to start Catia
    envdir=""
    root = ET.parse(Settingsdir + 'programs.xml').getroot()
    for program in root.findall("./programs/program[@name='"+program+"']"):
        for variable in program.findall("./variables/variable"):
            if variable.find('name').text=="envdir":
                envdir = variable.find('value').text
            #print(variable.find('name').text)
            #print(variable.find('value').text)
        print(envdir)

        # set environment Variables
        my_env = os.environ.copy()
        for variable in program.findall("./envvariables/variable"):
            my_env[variable.find('name').text.upper()] = variable.find('value').text
            #print (variable.find('name').text.upper())

    StartCommand="C:\\Program Files\\Dassault Systemes\\B30\\win_b64\\code\\bin\\CATSTART.exe"
    Arg1="-nowindow"
    Arg2= envdir
    Arg3=""

    result = subprocess.Popen([StartCommand, Arg1, Arg2, Arg3], env=my_env)
    print(result)
    ##window.destroy()


#*************Start ProGRAM *********************************

#  Set Variables
OS="mac"        # choose mac or win
if OS=="mac":
    Settingsdir = "/Users/berttroost/develop/GitHub/CatiaStarter/"
    Workingdir = "/Users/berttroost/develop/GitHub/CatiaStarter/"
if OS =="win":
    Settingsdir = "C:\\data\\CatiaStarter\\"
    Workingdir = "C:\\data\\CatiaStarter\\"
Program = "none"

# Get settingsdata
settings=getsettingsdata()
# Create Graphical User Interface
GUI(settings)
