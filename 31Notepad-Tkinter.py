#NOTEPAD
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

######################### FUNCTIONS ###################################

def newfile():
    global file
    root.title("Notepad")
    file=None
    TextArea.delete(1.0,END)
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Please visit notepad.com for more information")

#######################################################################


if __name__ == '__main__':
     #basic tkinter setup
     root=Tk()
     root.title("Notepad")
     root.wm_iconbitmap("4.ico")
     root.geometry("650x400")


     #add textarea
     TextArea=Text(root,font="lucida 13")
     file=None
     TextArea.pack(fill=BOTH,expand=True)

     #Lets create a menubar
     MenuBar = Menu(root)

######################### FILE MENU STARTS ####################################
FileMenu = Menu(MenuBar, tearoff=0)
# To open a new file
FileMenu.add_command(label="New", command=newfile)
# to open existing file
FileMenu.add_command(label="Open", command=openfile)
# to save current file
FileMenu.add_command(label="Save", command=savefile)
# to exit
FileMenu.add_command(label="Exit", command=quitApp)
MenuBar.add_cascade(label="File", menu=FileMenu)

######################### FILE MENU ENDS ####################################

######################### EDIT MENU STARTS ####################################
EditMenu=Menu(MenuBar,tearoff=0)
#to add cut , copy , paste
EditMenu.add_command(label="Cut",command=cut)
EditMenu.add_command(label="Copy",command=copy)
EditMenu.add_command(label="Paste",command=paste)
MenuBar.add_cascade(label="Edit",menu=EditMenu)
######################### EDIT MENU ENDS ####################################

######################### HELP MENU STARTS ####################################
HelpMenu=Menu(MenuBar,tearoff=0)
HelpMenu.add_command(label="About",command=about)
MenuBar.add_cascade(label="Help",menu=HelpMenu)
######################### HELP MENU ENDS ####################################

root.config(menu=MenuBar)

#SCROLLBAR
Scroll=Scrollbar(TextArea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()
