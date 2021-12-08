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
    Idproduit = StringVar()
    Produitname = StringVar()
    Quantite =IntVar()
    Prix = DoubleVar()

    def affichestockcaissier():
        win = Toplevel(widow)
        win.geometry("1100x900")
        win.title("Afficher Stock")

        title = Label(win , text = "Stock Caisse")
        title.place(x = 200 , y = 5)
        bakerimg = PhotoImage(file = '/Users/mathanaruban/Desktop/Cour/ProgrammationInterface/project_tkinter/projet_interface/bread.gif')
       

        def pommebutton():
            Idproduit.set("Fruit et Légumes")
            Produitname.set("Pommes")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def bananebutton():
            Idproduit.set("Fruit et Légumes")
            Produitname.set("Banane")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def manguebutton():
            Idproduit.set("Fruit et Légumes")
            Produitname.set("Mangue")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def orangebutton():
            Idproduit.set("Fruit et Légumes")
            Produitname.set("Oranges")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)

        def ananasbutton():
            Idproduit.set("Fruit et Légumes")
            Produitname.set("Ananas")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def saladebutton():
            Idproduit.set("Fruit et Légumes")
            Produitname.set("Pommes")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)

        def haricotbutton():
            Idproduit.set("Fruit et Légumes")
            Produitname.set("Haricot")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)

        def poivronsbutton():
            Idproduit.set("Fruit et Légumes")
            Produitname.set("Poivrons")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)    

        def pimentbutton():
            Idproduit.set("Fruit et Légumes")
            Produitname.set("Piment")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def tomatebutton():
            Idproduit.set("Fruit et Légumes")
            Produitname.set("Tomates")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def fruitbutton():
            Idproduit.set("Fruit et Légumes")
            Quantite.set(1000)
           

            affiche ="Catégories : "+Idproduit.get()+"\nQuantités de produit:"+str(Quantite.get())
            entryZDT.config(text = affiche)

        fruitetlegumes = Button(win , text = "Fruit\n et \nLégumes",height = 5 , command = fruitbutton)
        fruitetlegumes.place(x =10 , y = 50,width=100,height=100 )
        pomme = Button(win , text = "Pomme" , height = 5,command = pommebutton)
        pomme.place(x = 140 , y = 50,width=90,height=90)
        banane = Button(win , text = "Banane", height = 5,command = bananebutton)
        banane.place(x = 230 , y = 50,width=90,height=90)
        mangue = Button(win , text = "Mangue", height = 5, command = manguebutton)
        mangue.place( x = 320 , y = 50,width=90,height=90)
        orange = Button(win , text = "Orange", height = 5, command = orangebutton)
        orange.place(x = 410 , y = 50,width=90,height=90)
        ananas = Button(win , text = "Ananas", height = 5, command = ananasbutton)
        ananas.place( x = 500 , y = 50,width=90,height=90)
        salade = Button(win , text = "Salade ", height = 5, command= saladebutton)
        salade.place(x = 590, y = 50,width=90,height=90)
        haricot = Button(win, text = "Haricot ", height = 5, command = haricotbutton)
        haricot.place(x = 680 , y = 50,width=90,height=90)
        poivrons = Button(win, text = "Poivrons ", height = 5,command = poivronsbutton)
        poivrons.place(x = 770 , y = 50,width=90,height=90)
        piment = Button(win, text = "Piment", height = 5, command = pimentbutton)
        piment.place(x = 860 , y = 50,width=90,height=90)
        tomate = Button(win , text = "Tomates", height = 5, command = tomatebutton)
        tomate.place(x = 950, y = 50,width=90,height=90)

        
        def boulangeriebutton():
            Idproduit.set("Boulangerie")
            Quantite.set(1000)


            affiche ="Catégories : "+Idproduit.get()+"\nQuantités :"+str(Quantite.get())
            entryZDT.config(text = affiche)

        def baguettebutton():
            Idproduit.set("Boulangerie")
            Produitname.set("Baguettes")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)

        def traditionbutton():
            Idproduit.set("Boulangerie")
            Produitname.set("Tradition")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)

        def painbutton(): 
            Idproduit.set("Boulangerie")
            Produitname.set("Pain au Noix")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)

        def croissantbutton():
            Idproduit.set("Boulangerie")
            Produitname.set("Croissant")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)

        def briochebutton():
            Idproduit.set("Boulangerie")
            Produitname.set("Brioche")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)

        def gateaubutton():
            Idproduit.set("Boulangerie")
            Produitname.set("Gateau")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)

        def levuresbutton():
            Idproduit.set("Boulangerie")
            Produitname.set("Levures")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def boissonbutton():
            Idproduit.set("Boulangerie")
            Produitname.set("Boisson")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def tartebutton():
            Idproduit.set("Boulangerie")
            Produitname.set("Tarte")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def sandwichbutton():
            Idproduit.set("Boulangerie")
            Produitname.set("Sandwich")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)

        boulangerie = Button(win ,text = "Boulangerie",height = 4, command = boulangeriebutton)
        boulangerie.place(x = 10 , y = 150,width=100,height=100)
        baguette = Button(win , text ="Baguette", height = 5,command = baguettebutton)
        baguette.place(x = 140 , y = 150,width=90,height=90)
        tradition = Button(win, text = "Tradition", height = 5,command = traditionbutton)
        tradition.place(x = 230, y = 150,width=90,height=90)
        pain = Button ( win , text = "Pain \nau noix", height = 5,command = painbutton)
        pain.place(x= 320 , y = 150,width=90,height=90)
        croissant = Button (win , text = "Croissant", height = 5,command = croissantbutton)
        croissant.place(x = 410 , y = 150,width=90,height=90)
        brioche = Button(win , text= "Brioche", height = 5,command = briochebutton)
        brioche.place(x = 500 , y = 150,width=90,height=90)
        gateau = Button(win , text = "Gateau" , height = 5,command = gateaubutton)
        gateau.place(x = 590, y  = 150,width=90,height=90)
        levures = Button(win , text = "Levures" , height = 5,command = levuresbutton)
        levures.place(x = 680 , y = 150,width=90,height=90)
        boisson = Button(win , text = "Boisson" , height = 5,command = boissonbutton)
        boisson.place(x = 770 , y = 150,width=90,height=90)
        tarte = Button(win ,text ="Tartes" , height = 5,command = tartebutton)
        tarte.place(x = 860 , y = 150,width=90,height=90)
        sandwich= Button(win , text = "Sandwich", height = 5,command = sandwichbutton)
        sandwich.place(x = 950 , y = 150,width=90,height=90)

        def meatandfishbutton():
            Idproduit.set("Boucherie et Poissonerie")
            Quantite.set(1000)
            

            affiche ="Catégories : "+Idproduit.get()+"\nQuantités de produit :"+str(Quantite.get())
            entryZDT.config(text = affiche)

        def boeufbutton():
            Idproduit.set("Boucherie et Poissonerie")
            Produitname.set("Boeuf/Vache")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)

        def pouletbutton():
            Idproduit.set("Boucherie et Poissonerie")
            Produitname.set("Poulet")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)

        def moutonbutton():
            Idproduit.set("Boucherie et Poissonerie")
            Produitname.set("Mouton")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def cochonbutton():
            Idproduit.set("Boucherie et Poissonerie")
            Produitname.set("Cochon")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)

        def crabebutton():
            Idproduit.set("Boucherie et Poissonerie")
            Produitname.set("Crabes")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def saumonbutton(): 
            Idproduit.set("Boucherie et Poissonerie")
            Produitname.set("Saumon")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        def truitebutton():
            Idproduit.set("Boucherie et Poissonerie")
            Produitname.set("Truite")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        def sardinebutton():
            Idproduit.set("Boucherie et Poissonerie")
            Produitname.set("Sardine")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        def crevettesbutton():
            Idproduit.set("Boucherie et Poissonerie")
            Produitname.set("Boeuf/Vache")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        def lapinbutton():
            Idproduit.set("Boucherie et Poissonerie")
            Produitname.set("Lapin")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)


        meatandfish = Button(win , text = "Boucherie\n et \nPoissonerie", height = 5, command = meatandfishbutton)
        meatandfish.place(x = 10 , y = 250,width=100,height=100)
        boeuf = Button(win , text = "Boeuf \nVache", height = 5,command = boeufbutton)
        boeuf.place(x = 140 , y = 250,width=90,height=90)
        poulet = Button(win , text = "Poulet", height = 5, command = pouletbutton)
        poulet.place(x = 230 ,y = 250,width=90,height=90)
        mouton = Button(win, text = "Mouton",height = 5, command = moutonbutton)
        mouton.place(x = 320 , y = 250,width=90,height=90)
        cochon = Button(win, text = "Cochon", height = 5,command = cochonbutton)
        cochon.place(x = 410, y = 250,width=90,height=90)
        crabe = Button(win,text = "Crabe", height = 5,command = crabebutton)
        crabe.place(x = 500, y = 250,width=90,height=90)
        saumon = Button(win, text = "Saumon", height = 5,command = saumonbutton)
        saumon.place(x = 590 , y = 250,width=90,height=90)
        truite = Button(win ,text = "Truite", height = 5,command = truitebutton)
        truite.place(x = 680, y= 250 ,width=90,height=90)
        sardine = Button(win, text = "Sardine", height = 5,command = sardinebutton)
        sardine.place(x = 770, y = 250,width=90,height=90)
        crevettes = Button(win, text = "Crevettes",height = 5,command = crevettesbutton)
        crevettes.place(x = 860, y =250,width=90,height=90)
        lapin = Button(win , text = "Lapin" , height = 5,command = lapinbutton)
        lapin.place(x = 950 , y = 250,width=90,height=90)

        def entretienbutton():
            Idproduit.set("Produit d'Entretien")
            Quantite.set(1000)
 
            affiche ="Catégories : "+Idproduit.get()+"\nQuantités de produit :"+str(Quantite.get())
            entryZDT.config(text = affiche)
        
        def balaibutton():
            Idproduit.set("Produit d'Entretien")
            Produitname.set("Balai")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def javelbutton():
            Idproduit.set("Produit d'Entretien")
            Produitname.set("Javel")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def soudebutton():
            Idproduit.set("Produit d'Entretien")
            Produitname.set("Soude")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def lessivebutton():
            Idproduit.set("Produit d'Entretien")
            Produitname.set("Lessive")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def epongebutton():
            Idproduit.set("Produit d'Entretien")
            Produitname.set("Eponge")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def vaisellebutton():
            Idproduit.set("Produit d'Entretien")
            Produitname.set("Vaiselle")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def chiffonbutton():
            Idproduit.set("Produit d'Entretien")
            Produitname.set("Chiffon")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)

        def gantbutton():
            Idproduit.set("Produit d'Entretien")
            Produitname.set("Gant")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def sceaubutton():
            Idproduit.set("Produit d'Entretien")
            Produitname.set("Sceau")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)
        
        def poubellebutton():
            Idproduit.set("Produit d'Entretien")
            Produitname.set("Sac Poubelle")
            Quantite.set(100)
            Prix.set(10.0)
            affiche ="Catégories : "+Idproduit.get()+"\nProduit : "+Produitname.get()+"\nQuantités :"+str(Quantite.get())+"\nPrix: "+str(Prix.get())+"$"
            entryZDT.config(text = affiche)

        produitentretien = Button(win , text = "Produit\nd'entretien",height = 5,command = entretienbutton)
        produitentretien.place(x = 10 , y = 350,width=100,height=100)
        balai = Button(win, text = "Balai", height = 5, command = balaibutton)
        balai.place(x = 140,y=350,width=90,height=90)
        javel= Button(win , text = "Javel", height = 5,command = javelbutton)
        javel.place(x = 230, y = 350,width=90,height=90)
        soude = Button(win , text = "Soude", height = 5,command = soudebutton)
        soude.place(x = 320 , y = 350,width=90,height=90)
        lessive = Button(win , text = "Lessive", height = 5,command = lessivebutton)
        lessive.place(x = 410 , y = 350,width=90,height=90)
        eponge = Button(win ,text = "Eponge", height = 5,command =epongebutton)
        eponge.place(x = 500 , y = 350,width=90,height=90)
        vaiselle = Button(win , text = "Vaiselle", height = 5,command = vaisellebutton)
        vaiselle.place(x = 590 , y = 350,width=90,height=90)
        chiffon = Button(win , text = "Chiffon", height = 5,command = chiffonbutton)
        chiffon.place(x = 680 , y = 350,width=90,height=90)
        gant = Button(win, text = "Gant" , height =5,command = gantbutton)
        gant.place(x = 770 , y = 350,width=90,height=90)
        sceau = Button(win , text = "Sceau", height = 5,command = sceaubutton)
        sceau.place(x = 860 , y = 350,width=90,height=90)
        poubelle = Button(win ,text = "Poubelle", height =5,command = poubellebutton)
        poubelle.place(x = 950 ,y = 350,width=90,height=90)

        labelinfo = Label(win, font =("Comic sans ms",17,"italic"),text = "Informations : ")
        labelinfo.place (x = 400 , y = 500)
        entryZDT = Label(win,font=("Comic sans ms",14,"italic"),relief = GROOVE)
        entryZDT.place(x=450, y = 550,width = 400,height = 100)

        quittbutton1 = Button(win, text = "Quitter",command = lambda root=win:fenQuit(root))
        quittbutton1.place(x = 850, y = 700 )

    def ticketdecaissebutton():
        win = Toplevel(widow)
        win.geometry("500x700")
        win.title("Ticket de Caisse")



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