import socket
from tkinter import*
from threading import Thread
import numpy as np

port = 4912
server_addres = (socket.gethostbyname(socket.gethostname()), port)
users_sockets = []
big_data = []
your_history = []

def serv():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostname(), port))
    server.listen(5)
    chat = True
    while chat:
        user, addres = server.accept()                                      #Где user, это socket пользователя
        user.send(f"Ты присоединился из {addres} ".encode("utf-8"))
        users_sockets.append(user)
        while chat:
            data = user.recv(1024)
            data.decode("utf-8")
            big_data.append(data)

def gui_server():
    gui = Tk()
    gui.geometry("1200x900")
    gui["bg"] = "gray6"
    gui.title("Your server started")

    def add_users_nicknames():
        info = open("data/data_files.txt", encoding="utf-8")
        line = info.readlines()
        nickname = line[0][11:-1]
        return nickname

    user_nickname = add_users_nicknames()

    info_of_server = ("Сервер запущен на ip: {}, порту: {}".format(*server_addres))
    Label(gui, text = info_of_server,bg = "gray6", fg = "orange red").place(relx = 0.01, rely =0.02 )


    LabelFrame(gui, text = "Отправлять от сюда", font = ("Times New Roman", "16"), highlightthickness=0,
               bg = "gray15", width = 1200, height = 200,).place(relx = 0, rely = 0.77)
    pole_vvoda = Text(gui, wrap = "word", bg = "snow", relief = "solid", width = 75, height = 2, font = ("Times New Roman", "16"))
    pole_vvoda.place(relx = 0.03, rely = 0.85)

    message = StringVar()

    def send_ur_messages_to_you():
        line = pole_vvoda.get("1.0", END)
        your_history.append(line)
        index_history = len(your_history)
        if index_history != 0:
            with open("data/history.txt", "a", encoding= "utf-8") as file:
                file.write(f"{line}")
            with open("data/history.txt", "r", encoding="utf-8") as file:
                content = file.readlines()[-1]
            send_mes(index_history,content)
        else:
            pole_vvoda.delete("1.0", END)
            pole_vvoda.get("1.0", END)
            send_ur_messages_to_you()

    def send_mes(int_of_send,content):
        otstupi = np.arange(0.03, 0.73, 0.03)                           # создание массива numpy, т.к python list не умеет создавать float массивы
        otstupi.tolist()                                                # преобразование массива numpy в list python

        for int_of_send in range(int_of_send):                                   # HARD brain make it long time ради этой строчки созданы предыдущие 15
            Label(gui, textvariable = message, bg="gray6", fg="yellow").place(relx=0.02, rely=(0.01+otstupi[int_of_send]))                            # После получения строки, номер ее этерации через len(your_history) передается в функцию send_mes                                                                                                          #  номер этерации поступает в функцию и создается новый Label опущенный на 0.03 вниз при помощи вызова массива по индексу этерации, вот зачем такой странный цикл

        for user in users_sockets:                                      # каждому сокету массива отправляется сообщение
            user.send(message.encode("utf-8"))
        message.set(f"{user_nickname}::{content}")
        gui.update()
        pole_vvoda.delete("1.0", END)

    Thread(target=serv).start()
    Button(gui, command = lambda : Thread(target= send_ur_messages_to_you()).start(), text="Отправить", bg="orange red", width=30, height=6).place(relx=0.76, rely=0.82)


    gui.mainloop()







