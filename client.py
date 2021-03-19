import socket
from tkinter import*
from threading import Thread
import numpy as np
from tkinter import messagebox as mess

port = 4911
client_data = []
clients_nickname = []
otstupi = np.arange(0.03, 0.68, 0.04)
otstupi.tolist()

def gui_client():
    gui = Tk()
    gui.geometry("1200x900")
    gui["bg"] = "gray6"

    def polzvtl():
        global client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("192.168.56.1", port))
        chat = True
        info_about_you = f"К нам присоеденился новый участник {clients_nickname[-1]}"

        while chat:
            data = client.recv(1024)
            data_from_server = data.decode("utf-8")
            client_data.append(data_from_server)
            index = len(client_data)
            for i in range(index):
                if index == 1:
                    client.send(info_about_you.encode("utf-8"))
                Label(gui, text=data_from_server, bg="gray6", fg="yellow").place(relx=0.02, rely=(
                            0.02 + otstupi[index]))

    gui.title("You is client and connected to {}")

    LabelFrame(gui, text = "Отправлять от сюда", highlightthickness=0, bg = "gray15", width = 1200, height = 400,).place(relx = 0, rely = 0.77)
    pole_vvoda = Entry(gui, bg = "gray80", relief = "solid", width = 140)
    pole_vvoda.place(relx = 0.15, rely = 0.95)

    def add_users_nicknames():
        info = open("data/data_files.txt", encoding="utf-8")
        line = info.readlines()
        nickname = line[0][11:-1]
        return nickname

    client_nickname = add_users_nicknames()
    clients_nickname.append(client_nickname)

    info_of_server = (f"Сервер запущен на ip: 192.168.56.1, порту:{port}")
    Label(gui, text = info_of_server,bg = "gray6", fg = "orange red").place(relx = 0.01, rely =0.02 )


    LabelFrame(gui, text = "Отправлять от сюда", font = ("Times New Roman", "16"), highlightthickness=0,
               bg = "gray15", width = 1200, height = 200,).place(relx = 0, rely = 0.77)
    pole_vvoda = Text(gui, wrap = "word", bg = "snow", relief = "solid", width = 75, height = 2, font = ("Times New Roman", "16"))
    pole_vvoda.place(relx = 0.03, rely = 0.85)

    def send_ur_messages_to_you():
        line = pole_vvoda.get("1.0", END)
        clients_message = f"{client_nickname} :: {line}"
        client.send(clients_message.encode("utf-8"))
        pole_vvoda.delete("1.0", END)

    Button(gui, command = send_ur_messages_to_you,text="Отправить", bg="orange red",
           width=30, height=6).place(relx=0.76, rely=0.82)

    Thread(target=polzvtl).start()

    gui.mainloop()