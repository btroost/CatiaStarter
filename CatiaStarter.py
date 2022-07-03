#CatiaStarter
import tkinter as tk
import os
import subprocess
#import xml.dom.minidom
import xml.etree.ElementTree as ET

#######################################################################
# description
######################################################################

#  Variables
OS="mac"        # choose mac or win
if OS=="mac":
    Settingsdir = "/Users/berttroost/develop/GitHub/CatiaStarter/"
    Workingdir = "/Users/berttroost/develop/GitHub/CatiaStarter/"
if OS =="win":
    Settingsdir = "/Users/berttroost/develop/GitHub/CatiaStarter/"
    Workingdir = "/Users/berttroost/develop/GitHub/CatiaStarter/"

#import os
#os.path.join('app', 'subdir', 'dir', 'filename.foo')
#'app/subdir/dir/filename.foo'

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

    root = ET.parse(Settingsdir + 'licenserole.xml').getroot()
    for program in root.findall("./licenseroles/role"):
        LicenseRole.append(program.get('name'))
    Settings.append(LicenseRole)
    return Settings



def GUI(settings):
    window=tk.Tk()
    window.title(" Catia Starter ")
    window.geometry("600x400")

    # Usage Scope
    newlabel = tk.Label(text = " Select your Usagescope ")
    newlabel.grid(column=0,row=0)
    #    dropdown1=tk.OptionMenu(window,tk.IntVar(),"Papendrecht","Hoogerheide","Helmond","Filton")
    dropdown1=tk.OptionMenu(window,tk.IntVar(),settings[0][0],settings[0][1],settings[0][2])
    dropdown1.grid(column = 1, row=0)

    # Program
    newlabel = tk.Label(text = " Select your Program ")
    newlabel.grid(column=0,row=1)
    dropdown=tk.OptionMenu(window,tk.IntVar(),settings[1][0],settings[1][1])
    dropdown.grid(column = 1, row=1)

    # LicenseRole
    newlabel = tk.Label(text = " Select your LicenseRole ")
    newlabel.grid(column=0,row=2)
    dropdown=tk.OptionMenu(window,tk.IntVar(),settings[2][0],settings[2][1])
    dropdown.grid(column = 1, row=2)

    # Button Start Catia
    mybutton = tk.Button(window, text = "Start Catia")
    mybutton.grid(column=1,row=3)
    mybutton.bind("<Button-1>",start)

    # Button Check licenses
    mybutton = tk.Button(window, text = "Check License")
    mybutton.grid(column=0,row=4)
    mybutton.bind("<Button-1>",CheckLicense)

    window.mainloop()


def CheckLicense(event):
    # 1) check license
    # 2) copy licensefile
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

def start(event):
    print(" Start Catia")

    program = "Airbus"

    #Get variables to start Catia
    root = ET.parse(Settingsdir + 'programs.xml').getroot()
    for program in root.findall("./programs/program[@name='"+program+"']"):
        for variable in program.findall("./variables/variable"):
#            print(variable.find('name').text)
            print(variable.find('value').text)

        # set environment Variables
        my_env = os.environ.copy()
        for variable in program.findall("./envvariables/variable"):
            my_env[variable.find('name').text] = variable.find('value').text
#            print("test")

    #my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
#    my_env["testvar"] = "MyTestVarValues"
##    my_command = "export > tstenv.txt"
#    my_command = "c:\data\apps\testenv.cmd"
#    subprocess.Popen(my_command, env=my_env)

    #os.environ['SOMEVAR'] = 'SOMEVAL'
    #you might use my_env.get("PATH", '') instead of my_env["PATH"] in case PATH somehow not defined in the original environment, but other than that it looks fine.

    #Start-Process  -WorkingDirectory "C:\Program Files\Dassault Systemes\B30\win_b64\code\bin" -ArgumentList "-nowindow"  #-nowindow  -ArgumentList "/c dir `"%systemdrive%\program files`""
    #os.system(""C:\Program Files\Dassault Systemes\B30\win_b64\code\bin\CATSTART.exe"")
    # "-nowindow"  #-nowindow  -ArgumentList "/c dir `"%systemdrive%\program files`""

    #file = "C:/Program Files/Dassault Systemes/B30/win_b64/code/bin/CATSTART.exe"
    #subprocess.call([file])

###    result = subprocess.Popen(["C:\Program Files\Dassault Systemes\DS License Server\win_b64\\code\\bin\\DSLicSrv.exe", "-admin", "-i", "c:\data\\apps\startup\dslsinput.txt", "-o", "c:\data\\apps\startup\dslsoutputpy.txt"])
 ###  result = subprocess.Popen(["C:\Program Files\Dassault Systemes\DS License Server\win_b64\\code\\bin\\DSLicSrv.exe", "-admin", "-i", "c:\data\\apps\startup\dslsinput.txt", "-o", "c:\data\\apps\startup\dslsoutputpy.txt"], env=my_env)

#    print (result)

#*************Start ProGRAM *********************************
# get settingsdata
settings=getsettingsdata()
#for row in settings:
#    print(row)
#Create Graphical User Interface
GUI(settings)
