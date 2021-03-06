import socket
from tkinter import*
from threading import Thread
import numpy as np
from tkinter import messagebox as mess
import time

port = 4911
server_addres = (socket.gethostbyname(socket.gethostname()), port)
users_sockets = []
clients_nicknames = []
server_data = []
dict_of_user = {}
otstupi = np.arange(0.03, 0.68, 0.04)  # создание массива numpy, т.к python arrange не умеет создавать float массивы
otstupi.tolist()                       # преобразование numpy массива к list
quick_clients_nicknames = []

def gui_server():
    gui = Tk()
    gui.geometry("1200x900")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostname(), port))

    #главная функция
    def serv():
        server.listen(5)
        chat = True
        while chat:

            list_of_users = LabelFrame(gui, text="Список пользователей онлайн", font=("Times New Roman", "16"),
                                       fg="orange red", bg="gray15",
                                       width=680, highlightthickness=0)
            list_of_users.place(relx=0.75, rely=0.02)
            your_id = Label(list_of_users, text=f"Никнейм: {server_nickname}", font=("Times New Roman", "12"), bg="gray15",
                            fg="yellow")
            your_id.pack(side=TOP)
            Is_you = Label(list_of_users, text="Это ты", font=("Times New Roman", "13"), bg="gray15", fg="orange red")
            Is_you.pack(side=TOP)

            user, addres = server.accept()                     # Где user, это socket пользователя
            user.send(f"Ты присоединился из {addres} ".encode("utf-8"))
            users_sockets.append(user)

            while chat:
                data = user.recv(1024)
                All_Data = data.decode("utf-8")
                server_data.append(All_Data)
                index = len(server_data)
                for i in range(index):
                    Label(gui, text=All_Data, bg="gray6", fg="yellow").place(relx=0.02, rely=(
                            0.02 + otstupi[index]))
                for user in users_sockets:
                    user.send(All_Data.encode("utf-8"))
                if All_Data.startswith("К нам присоединился новый участник"):
                    user_nickname = All_Data[35:-1]
                    for first_nickname in clients_nicknames:
                        if user_nickname != first_nickname:
                            clients_nicknames.append(user_nickname)
                    quick_clients_nicknames.append(user_nickname)
                    dict_of_user[user_nickname] = user
                if len(quick_clients_nicknames) > 0:
                    client_id = Label(list_of_users, text=f"Никнейм: {quick_clients_nicknames[-1]}", font=("Times New Roman", "12"),
                                      bg="gray15", fg="yellow")
                    send_clients = Button(list_of_users,command = private_send_mes, text="Отправить\nличное сообщение", font=("Times New Roman", "14"),
                           bg="gray15", fg="orange red")
                    client_id.pack(side=TOP)
                    send_clients.pack(side=TOP)
                    quick_clients_nicknames.pop()
                print(dict_of_user)

    Thread(target=serv).start()

    def on_closing():
        if mess.askokcancel("Закрыть", "Действительно закрыть, работа сервера будет приостановлена"):
            server.close()
            gui.destroy()

    gui["bg"] = "gray6"
    gui.title("Your server started")

    def add_users_nicknames():
        info = open("data/data_files.txt", encoding="utf-8")
        line = info.readlines()
        nickname = line[0][11:-1]
        return nickname

    server_nickname = add_users_nicknames()
    Label(gui, text= "Чтобы отправить приватное сообщение, требуется перед сообщением\n указать /PM:никнейм пользователя и отправить через список пользователей",
          bg = "gray6", fg = "orange red").place(relx = 0.3, rely =0.02)
    info_of_server = ("Сервер запущен на ip: {}, порту: {}".format(*server_addres))
    Label(gui, text = info_of_server,bg = "gray6", fg = "orange red").place(relx = 0.01, rely =0.02 )

    LabelFrame(gui, text = "Отправлять от сюда", font = ("Times New Roman", "16"), highlightthickness=0,
               bg = "gray15", width = 1200, height = 200,).place(relx = 0, rely = 0.77)
    pole_vvoda = Text(gui, wrap = "word", bg = "snow", relief = "solid", width = 75, height = 2, font = ("Times New Roman", "16"))
    pole_vvoda.place(relx = 0.03, rely = 0.85)

    def send_ur_messages_to_you():
        line = pole_vvoda.get("1.0", END)
        server_data.append(line)
        index_history = len(server_data)
        if index_history != 0:
            with open("data/history.txt", "w", encoding= "utf-8") as file:
                file.write(f"{line}")
            ur_time = time.localtime()
            accept_time = time.strftime("%H:%M:%S", ur_time)
            all_message = f"[{accept_time}]  {server_nickname} ::  {line}"
            Thread(target= send_mes, args =(index_history,all_message,)).start()
        else:
            pole_vvoda.delete("1.0", END)

    def send_mes(int_of_send,message,):
        for i in range(int_of_send):                                   # HARD brain make it long time ради этой строчки созданы предыдущие 15
            message_to_you = Label(gui, text = message, bg="gray6", fg="yellow").place(relx=0.02, rely=(0.02+otstupi[int_of_send]))     # После получения строки, номер ее этерации через len(server_data) передается в функцию send_mes
                                                                                                                                        # каждому сокету массива отправляется сообщение номер этерации поступает в функцию и создается новый Label опущенный на 0.03 вниз при помощи вызова массива по индексу этерации, вот зачем такой странный цикл
        for user in users_sockets:
            user.send(message.encode("utf-8"))

        pole_vvoda.delete("1.0", END)

    def private_send_mes():
        private_mes = pole_vvoda.get("1.0", END)
        for key in dict_of_user.keys():
            print(key)
            if f"/PM:{key}" in private_mes:
                private_socket = dict_of_user[key]
                private_socket.send(f"Личное сообщение от {private_mes[4:]}".encode("utf-8"))
        pole_vvoda.delete("1.0", END)

    Button(gui, command=send_ur_messages_to_you, text="Отправить", bg="orange red",
           width=30, height=6).place(relx=0.76, rely=0.82)

    gui.protocol("WM_DELETE_WINDOW", on_closing)
    gui.mainloop()





