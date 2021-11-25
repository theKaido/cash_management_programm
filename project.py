from tkinter import *


widow = Tk()
widow.title("Authentication")
widow.geometry("600x400")

labeltitre = Label(text = "Connection",relief=GROOVE)
labeltitre.place( x = 270, y = 50)


labelid = Label(text = "User:",)
labelid.place(x = 100 , y = 100)
user = StringVar()
user.set("ID")
saisieUser = Entry(widow,textvariable = user,bd = '5')
saisieUser.place(x = 180,y = 100)

labelpwd = Label(text = "Password:")
labelpwd.place(x = 100, y = 200)
password = StringVar()
password.set('**************')
saisiePwd = Entry(widow,textvariable = password,bd = '5')
saisiePwd.place(x = 180, y = 200)


widow.mainloop()