from tkinter import *


widow = Tk()
widow.title("Authentication")
widow.geometry("600x400")

#labeltitre = Label(text = "Connection",relief=GROOVE)
#labeltitre.place( x = 270, y = 50)
 
def delentryaffiche():
    iden.delete(0,'end')

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


    def affichestockcaissier():
        win = Toplevel(widow)
        win.geometry("1100x800")
        win.title("Afficher Stock")

        title = Label(win , text = "Stock Caisse")
        title.place(x = 200 , y = 5)

        fruitetlegumes = Button(win , text = "Fruit\n et \nLégumes",height = 5)
        fruitetlegumes.place(x =10 , y = 50 )
        pomme = Button(win , text = "Pomme" , height = 5)
        pomme.place(x = 140 , y = 50)
        banane = Button(win , text = "Banane", height = 5)
        banane.place(x = 220 , y = 50)
        mangue = Button(win , text = "Mangue", height = 5)
        mangue.place( x = 300 , y = 50)
        orange = Button(win , text = "Orange", height = 5)
        orange.place(x = 380 , y = 50)
        ananas = Button(win , text = "Ananas", height = 5)
        ananas.place( x = 460 , y = 50)
        salade = Button(win , text = "Salade ", height = 5)
        salade.place(x = 540 , y = 50)
        haricot = Button(win, text = "Haricot ", height = 5)
        haricot.place(x = 620 , y = 50)
        poivrons = Button(win, text = "Poivrons ", height = 5)
        poivrons.place(x = 700 , y = 50)
        piment = Button(win, text = "Piment", height = 5)
        piment.place(x = 780 , y = 50)
        tomate = Button(win , text = "Tomates", height = 5)
        tomate.place(x = 860, y = 50)

        boulangerie = Button(win , text = "Boulangerie" , height = 5)
        boulangerie.place(x = 10 , y = 150)
        baguette = Button(win , text ="Baguette", height = 5)
        baguette.place(x = 140 , y = 150)
        tradition = Button(win, text = "Tradition", height = 5)
        tradition.place(x = 220, y = 150)
        pain = Button ( win , text = "Pain \nau noix", height = 5)
        pain.place(x= 300 , y = 150)
        croissant = Button (win , text = "Croissant", height = 5)
        croissant.place(x = 380 , y = 150)
        brioche = Button(win , text= "Brioche", height = 5)
        brioche.place(x = 460 , y = 150)
        gateau = Button(win , text = "Gateau" , height = 5)
        gateau.place(x = 540, y  = 150)
        levures = Button(win , text = "Levures" , height = 5)
        levures.place(x = 620 , y = 150)
        boisson = Button(win , text = "Boisson" , height = 5)
        boisson.place(x = 700 , y = 150)
        tarte = Button(win ,text ="Tartes" , height = 5)
        tarte.place(x = 780 , y = 150)
        sandwich= Button(win , text = "Sandwich", height = 5)
        sandwich.place(x = 850 , y = 150)

        meatandfish = Button(win , text = "Boucherie\n et \nPoissonerie", height = 5)
        meatandfish.place(x = 10 , y = 250)
        boeuf = Button(win , text = "Boeuf \nVache", height = 5)
        boeuf.place(x = 140 , y = 250)
        poulet = Button(win , text = "Poulet", height = 5)
        poulet.place(x = 210 ,y = 250)
        mouton = Button(win, text = "Mouton",height = 5)
        mouton.place(x = 280 , y = 250)
        cochon = Button(win, text = "Cochon", height = 5)
        cochon.place(x = 360, y = 250)
        crabe = Button(win,text = "Crabe", height = 5)
        crabe.place(x = 440, y = 250)
        saumon = Button(win, text = "Saumon", height = 5)
        saumon.place(x = 510 , y = 250)
        truite = Button(win ,text = "Truite", height = 5)
        truite.place(x = 580, y= 250 )
        sardine = Button(win, text = "Sardine", height = 5)
        sardine.place(x = 640, y = 250)
        crevettes = Button(win, text = "Crevettes",height = 5)
        crevettes.place(x = 710, y =250)
        lapin = Button(win , text = "Lapin" , height = 5)
        lapin.place(x = 790 , y = 250)

        produitentretien = Button(win , text = "Produit\nd'entretien",height = 5)
        produitentretien.place(x = 10 , y = 350)
        balai = Button(win, text = "Balai", height = 5)
        balai.place(x = 140,y=350)
        javel= Button(win , text = "Javel", height = 5)
        javel.place(x = 200, y = 350)
        soude = Button(win , text = "Soude", height = 5)
        soude.place(x = 260 , y = 350)
        lessive = Button(win , text = "Lessive", height = 5)
        lessive.place(x = 320 , y = 350)
        eponge = Button(win ,text = "Eponge", height = 5)
        eponge.place(x = 400 , y = 350)
        vaiselle = Button(win , text = "Vaiselle", height = 5)
        vaiselle.place(x = 480 , y = 350)
        chiffon = Button(win , text = "Chiffon", height = 5)
        chiffon.place(x = 560 , y = 350)
        gant = Button(win, text = "Gant" , height =5)
        gant.place(x = 640 , y = 350)
        sceau = Button(win , text = "Sceau", height = 5)
        sceau.place(x = 700 , y = 350)
        poubelle = Button(win ,text = "Poubelle", height =5)
        poubelle.place(x = 770 ,y = 350)


    labelcaissier = Label(win, text= "Interface Caissier :")
    labelcaissier.place(x=100, y = 10)

    afficherstock = Button(win, text = "Afficher Stock",height = 3, command = affichestockcaissier)
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

        def saveaddcaissier():
            save = ID.get()+"\n"+Nom.get()+"\n"+Prenom.get()+"\n"+Dateofbirth.get()+"\n"+Adresse.get()+"\n"+Codepostal.get()+"\n"+Login.get()+"\n"+Password.get()+"\n\n\n"
            fichier = open("data.txt", "w")
            fichier.write(save)
            fichier.close()

        def erasecase():
            iden.delete(0,'end')
            name.delete(0,'end')
            prenom.delete(0,'end')
            dateofbirth.delete(0,'end')
            adresse.delete(0,'end')
            codepostal.delete(0,'end')
            login.delete(0,'end')
            password.delete(0,'end')


        savebutton = Button(win , text ="Enregistrer",command = saveaddcaissier)
        savebutton.place(x = 50 , y = 550)

        cleanbutton = Button(win ,text ="Effacer",command = erasecase)
        cleanbutton.place(x = 150 , y = 550)

        quitbutton = Button(win, text = "Quitter", command = lambda root = win:fenQuit(root))
        quitbutton.place(x = 500, y = 550)

    def affichercaissier():
        win = Toplevel(widow)
        win.geometry("250x250")
        win.title("Fenetre d'affichage caisse")
   
        ID = StringVar()
        ID.set("Saisir Identifiant")
        iden = Entry(win , textvariable = ID,width = "13")
        iden.place( x = 100,y = 50)
        labelid = Label(win,text = "Identifiant :")
        labelid.place(x = 20 , y = 50)

        afficherbutton = Button(win , text = "Afficher \nle caissier \n saisie",height = 4)
        afficherbutton.place(x = 20 , y = 100)

        affichertout = Button(win , text = "Afficher\n tout\n les caissiers",height = 4)
        affichertout.place (x = 120, y = 100)

    
        vidersaisie = Button(win ,text ="Effacer",command = delentryaffiche)
        vidersaisie.place(x = 20 , y = 200)

        quitbutton = Button(win, text = "Quitter", command = lambda root = win:fenQuit(root))
        quitbutton.place(x = 150, y = 200)

    def supprcaisier():
        win = Toplevel(widow)
        win.geometry("250x250")
        win.title("Fenetre d'affichage caisse")
   
        ID = StringVar()
        ID.set("Saisir Identifiant")
        iden = Entry(win , textvariable = ID,width = "13")
        iden.place( x = 100,y = 50)
        labelid = Label(win,text = "Identifiant :")
        labelid.place(x = 20 , y = 50)

        supprbutton = Button(win , text = "Supprimer \nle caissier \n saisie",height = 4)
        supprbutton.place(x = 20 , y = 100)

        vidersaisie = Button(win ,text ="Effacer",command = delentryaffiche)
        vidersaisie.place(x = 20 , y = 200)

        quitbutton = Button(win, text = "Quitter", command = lambda root = win:fenQuit(root))
        quitbutton.place(x = 150, y = 200)

    labelmanager = Label(win,text = "Interface Manager :")
    labelmanager.place(x = 100,y = 10)

    ajoutcaissebutton= Button(win, text = "Ajout de Caissier",height = 3, command = ajoutcaissier)
    ajoutcaissebutton.place(x = 40 , y = 50)

    affichercaisierbutton = Button(win,text = "Afficher Caissier",height = 3,command = affichercaissier)
    affichercaisierbutton.place(x = 210 , y = 50)

    supprimercaisier = Button(win,text = "Suprrimer Caissier",height = 3,command = supprcaisier)
    supprimercaisier.place(x = 40 , y = 140)

    suivievente = Button(win,text = "Suivie de Vente",height = 3)
    suivievente.place( x = 210 , y = 140)

    modecaisse = Button(win,text="Mode Caisse",height = 3,command = caisierinterface)
    modecaisse.place( x = 40 , y = 230)

    quitbutton = Button(win,text = "Quitter",command = lambda root = win:fenQuit(root))
    quitbutton.place(x = 270, y = 350)


labelid = Label(text = "Login :",)
labelid.place(x = 100 , y = 100)
user = StringVar()
user.set("ID")
saisieUser = Entry(widow,textvariable = user)
saisieUser.place(x = 180,y = 100)

labelpwd = Label(text = "Password :")
labelpwd.place(x = 100, y = 200)
password = StringVar()
saisiePwd = Entry(widow,show='*',textvariable=password)
saisiePwd.place(x = 180, y = 200)

butonconnect = Button(text = "Connection",relief = RAISED,command = connect)
butonconnect.place( x = 150 , y = 300)

quitbutton1 = Button(widow, text = "Quitter",command = lambda root=widow:fenQuit(root))
quitbutton1.place(x = 260, y = 300 )





widow.mainloop()