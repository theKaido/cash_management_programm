from tkinter import *


widow = Tk()
widow.title("Authentication")
widow.geometry("600x400")

#labeltitre = Label(text = "Connection",relief=GROOVE)
#labeltitre.place( x = 270, y = 50)
def ajoutcaissier():
    win = Toplevel(widow)
    win.geometry("600x600")
    win.title("Ajout de Caisse")
    labeltitre = Label(win,text = "Remplir les champs de saisie :")
    labeltitre.place(x = 100 , y =10)

    ID = StringVar()
    ID.set("Saisir Identifiant")
    iden = Entry(win , textvariable = ID,width = "40")
    iden.place( x = 130,y = 50)
    labelid = Label(win,text = "Identifiant :")
    labelid.place(x = 20 , y = 50)

    Nom= StringVar()
    Nom.set("Saisir Nom")
    name = Entry(win, textvariable = Nom,width="40")
    name.place(x = 130,y = 100)
    labelnom = Label(win,text = "Nom :")
    labelnom.place(x = 20 , y = 100)
   
    Prenom = StringVar()
    Prenom.set("Saisir Prenom")
    prenom = Entry(win , textvariable = Prenom,width ="40")
    prenom.place(x = 130 , y =150)
    labelprenom = Label(win,text = "Prénom :")
    labelprenom.place(x = 20 , y = 150)

    Dateofbirth= StringVar()
    Dateofbirth.set("format demandé AAAA/MM/JJ")
    dateofbirth = Entry(win , textvariable = Dateofbirth,width = "40")
    dateofbirth.place(x = 130 , y = 200)
    labeldate = Label(win,text="Date of birth:")
    labeldate.place( x = 20, y = 200)

    Adresse = StringVar()
    Adresse.set("Saisir Adresse")
    adresse = Entry(win , textvariable = Adresse,width = "40")
    adresse.place(x = 130 , y = 250)
    labeladresse = Label(win , text = "Adresse :")
    labeladresse.place(x = 20 , y = 250)

    Codepostal = StringVar()
    Codepostal.set("Saisir Code postal")
    codepostal = Entry ( win , textvariable = Codepostal,width = "40")
    codepostal.place(x = 130 , y = 300)
    labelpostalcode = Label(win, text = "Code postal :")
    labelpostalcode.place(x = 20 , y =300)

    Login = StringVar()
    Login.set("Choisiser votre login")
    login= Entry(win,textvariable = Login,width = "40")
    login.place(x = 130 , y = 350)
    labellogin = Label(win, text = "Login :")
    labellogin.place(x = 20 , y = 350)

    Password = StringVar()
    Password.set("Entrez votre mot de passe")
    password = Entry(win , textvariable = Password,width = "40")
    password.place(x = 130 , y = 400)
    labelpassword = Label(win, text = "Password :")
    labelpassword.place(x = 20 , y = 400)

    savebutton = Button(win , text ="Enregistrer")
    savebutton.place(x = 50 , y = 550)

    cleanbutton = Button(win ,text ="Vider")
    cleanbutton.place(x = 150 , y = 550)

    quitbutton = Button(win, text = "Quitter", command = lambda root = win:fenQuit(root))
    quitbutton.place(x = 500, y = 550)

def affichercaissier():
    win = Toplevel(widow)
    win.geometry("400x400")
    win.title("Fenetre d'affichage caisse")
    quitbutton = Button(win, text = "Quitter", command = lambda root = win:fenQuit(root))
    quitbutton.place(x = 350, y = 390)


def fenQuit(widow):
    widow.destroy()

def connect():
    win = Toplevel(widow)
    win.geometry("400x400")
    win.title("Fenetre de Connection")

    buttonessaie = Button(win,text = "Manager Interface",relief = RAISED,height = 3, command = managerinterface)
    buttonessaie.place(x=40 , y = 120)

    buttonessaie2 = Button (win,text = "Caissier Interface",relief = RAISED,height=3, command = caisierinterface)
    buttonessaie2.place(x=210, y = 120)

    quitbutton1 = Button(win, text = "Quitter",command = lambda root=win:fenQuit(root))
    quitbutton1.place(x = 270, y = 350 )

def caisierinterface():
    win = Toplevel(widow)
    win.geometry("400x400") 
    win.title("Interface Caisier")

    labelcaissier = Label(win, text= "Interface Caissier :")
    labelcaissier.place(x=100, y = 10)

    afficherstock = Button(win, text = "Afficher Stock",height = 3)
    afficherstock.place(x=40 , y = 50)

    ticketdecaisse = Button(win , text = "Ticket de Caisse", height = 3)
    ticketdecaisse.place(x = 210 , y = 50)

    interfaceexportstat = Button(win, text="Interface Export\n Statistique", height = 3)
    interfaceexportstat.place(x = 40 , y =140)

    quitbutton = Button(win, text = "Quitter", command = lambda root = win:fenQuit(root))
    quitbutton.place(x = 270, y = 350)

def managerinterface():
    win = Toplevel(widow)
    win.geometry("400x400")
    win.title("Interface Manager")

    labelmanager = Label(win,text = "Interface Manager :")
    labelmanager.place(x = 100,y = 10)

    ajoutcaissebutton= Button(win, text = "Ajout de Caissier",height = 3, command = ajoutcaissier)
    ajoutcaissebutton.place(x = 40 , y = 50)

    affichercaisierbutton = Button(win,text = "Afficher Caissier",height = 3)
    affichercaisierbutton.place(x = 210 , y = 50)

    supprimercaisier = Button(win,text = "Suprrimer Caissier",height = 3)
    supprimercaisier.place(x = 40 , y = 140)

    suivievente = Button(win,text = "Suivie de Vente",height = 3)
    suivievente.place( x = 210 , y = 140)

    modecaisse = Button(win,text="Mode Caisse",height = 3,command = caisierinterface)
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

butonconnect = Button(text = "Connection",relief = RAISED,command = connect)#On va ensuite modifier ce label en bouton pour afficher une fenetre de connection
butonconnect.place( x = 150 , y = 300)

quitbutton1 = Button(widow, text = "Quitter",command = lambda root=widow:fenQuit(root))
quitbutton1.place(x = 260, y = 300 )





widow.mainloop()