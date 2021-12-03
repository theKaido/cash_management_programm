from tkinter import *


widow = Tk()
widow.title("Authentication")
widow.geometry("600x400")

#labeltitre = Label(text = "Connection",relief=GROOVE)
#labeltitre.place( x = 270, y = 50)

def fenQuit(widow):
    widow.destroy()

def connect():
    win = Toplevel(widow)
    win.geometry("400x400")
    win.title("Fenetre de Connection")
    quitbutton1 = Button(win, text = "Quitter",command = lambda root=win:fenQuit(root))
    quitbutton1.place(x = 80, y = 260 )

def managerinterface():
    win = Toplevel(widow)
    win.geometry("400x400")
    win.title("Interface Manager")
    labelmanager = Label(win,text = "Interface Manager :")
    labelmanager.place(x = 100,y = 10)

    ajoutcaissebutton= Button(win, text = "Ajout de caisier",height = 3)
    ajoutcaissebutton.place(x = 40 , y = 50)

    affichercaisier = Button(win,text = "Afficher Caisier",height = 3)
    affichercaisier.place(x = 210 , y = 50)

    supprimercaisier = Button(win,text = "Suprrimer Caisier",height = 3)
    supprimercaisier.place(x = 40 , y = 140)

    suivievente = Button(win,text = "Suivie de Vente",height = 3)
    suivievente.place( x = 210 , y = 140)

    modecaisse = Button(win,text="Mode Caisse",height = 3)
    modecaisse.place( x = 40 , y = 230)

    quitbutton = Button(win,text = "Quitter",command = lambda root = win:fenQuit(root))
    quitbutton.place(x = 270, y = 350)


labelid = Label(text = "Login:",)
labelid.place(x = 100 , y = 100)
user = StringVar()
user.set("ID")
saisieUser = Entry(widow,textvariable = user)
saisieUser.place(x = 180,y = 100)

labelpwd = Label(text = "Password:")
labelpwd.place(x = 100, y = 200)
password = StringVar()
password.set('**************')
saisiePwd = Entry(widow,textvariable = password)
saisiePwd.place(x = 180, y = 200)

labelconnect = Button(text = "Connection",relief = RAISED,command = connect)#On va ensuite modifier ce label en bouton pour afficher une fenetre de connection
labelconnect.place( x = 150 , y = 300)
quitbutton1 = Button(widow, text = "Quitter",command = lambda root=widow:fenQuit(root))
quitbutton1.place(x = 260, y = 300 )


buttonessaie = Button(text = "ManagerInterface",relief = RAISED,command = managerinterface)
buttonessaie.place(x=300 , y = 350)
widow.mainloop()