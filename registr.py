from tkinter import *
from tkinter import messagebox as mess
import kto_ya

def sled_okno():
    registr = Tk()
    registr.title("Регистрация")
    registr.geometry("{}x{}".format(450, 500))
    registr["bg"] = "gray22"

    def zakritie():
        registr.destroy()
        kto_ya.vibor(nickname)

    L1 = Label(registr, width = 30, height = 2, text = "Придумайте имя пользователя", font = ("times new roman", "14")
               , bg = "grey25")
    L1.place(relx = 0.18, rely = 0.15)

    username = StringVar()

    Username = Entry(registr, relief = "solid", textvariable=username, bg = "burlywood4", width = 30)
    Username.place(relx = 0.3, rely = 0.25)

    L2 = Label(registr, width = 30, height = 2, text = "Придумайте надежный пароль", font = ("times new roman", "14")
               , bg = "grey25")
    L2.place(relx = 0.18, rely = 0.35)
    password = StringVar()

    Password = Entry(registr, show = "*", relief = "solid", textvariable=password, bg ="burlywood4", width = 30)
    Password.place(relx = 0.3 , rely = 0.45)

    L3 = Label(registr, text = "Укажите вашу электронную почту", bg = "grey25",
               width = 30, height = 2, font = ("times new roman", "14"))
    L3.place(relx = 0.17 , rely = 0.55)

    email = StringVar()

    Email = Entry(registr, relief = "solid", textvariable=email, bg = "burlywood4", width = 30)
    Email.place(relx = 0.3, rely = 0.65)


    def data_get():
        username = Username.get()
        password = Password.get()
        email = Email.get()


        if username != "" and password != "" and email != "":
            data = open('data/data_files.txt', 'tw', encoding='utf-8')
            data.write("username : {} \npassword : {} \nemail: {}".format(username, password, email))
            data = open("data/data_files.txt", encoding="utf-8")
            global nickname
            nick = data.readlines()
            nickname = nick[0][11:-1]
            data.close()
            zakritie()

        else:
            mess.showerror(title = "Ошибка", message= "Пожалуйста, заполните все поля регистрации")


    Button(registr, command = data_get, width=30, height=2, text="Создать аккаунт",
                font=("times new roman", "18"), bg="orange red").place(relx=0.08, rely=0.78)

    registr.mainloop()


