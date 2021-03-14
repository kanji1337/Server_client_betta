import socket
from tkinter import*
from threading import Thread
import numpy as np

port = 4912
client_data = []

def polzvtl():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.56.1", port))
    chat = True

    while chat:
        data = client.recv(1024)
        data_from_server = data.decode("utf-8")
        client_data.append(data_from_server)

        if not data:
            client.close()
            print("Server closed")

def gui_client():
    gui = Tk()

    gui.geometry("1200x900")
    gui["bg"] = "gray6"
    gui.title("You is client and connected to {}")

    LabelFrame(gui, text = "Отправлять от сюда", highlightthickness=0, bg = "gray15", width = 1200, height = 400,).place(relx = 0, rely = 0.77)
    pole_vvoda = Entry(gui, bg = "gray80", relief = "solid", width = 140)
    pole_vvoda.place(relx = 0.15, rely = 0.95)

    def add_users_nicknames():
        info = open("data/data_files.txt", encoding="utf-8")
        line = info.readlines()
        nickname = line[0][11:-1]
        return nickname

    clients_nickname = add_users_nicknames()

    info_of_server = ("Сервер запущен на ip: 192.168.56.1, порту: {}".format(port))
    Label(gui, text = info_of_server,bg = "gray6", fg = "orange red").place(relx = 0.01, rely =0.02 )


    LabelFrame(gui, text = "Отправлять от сюда", font = ("Times New Roman", "16"), highlightthickness=0,
               bg = "gray15", width = 1200, height = 200,).place(relx = 0, rely = 0.77)
    pole_vvoda = Text(gui, wrap = "word", bg = "snow", relief = "solid", width = 75, height = 2, font = ("Times New Roman", "16"))
    pole_vvoda.place(relx = 0.03, rely = 0.85)

    def send_ur_messages_to_you():
        line = pole_vvoda.get("1.0", END)
        client_data.append(line)
        index_history = len(client_data)
        if index_history != 0:
            with open("data/history.txt", "tw", encoding= "utf-8") as file:
                file.write(f"{line}")
            client_message = client_data[-1]
            somebody_message = client_data[-2]
            clients_message = f"{clients_nickname} :: {client_message}\n{somebody_message}"
            Thread(target= send_mes, args =(index_history,clients_message,)).start()
        else:
            pole_vvoda.delete("1.0", END)

    def send_mes(int_of_send,message,):
        otstupi = np.arange(0.03, 0.73, 0.04)
        otstupi.tolist()
        for i in range(int_of_send):
            Label(gui, text = message, bg="gray6", fg="yellow").place(relx=0.02, rely=(0.005+otstupi[int_of_send]))
        client.send(message.encode("utf-8"))
        pole_vvoda.delete("1.0", END)

    Thread(target = send_ur_messages_to_you).start()

    Button(gui, command = send_ur_messages_to_you,text="Отправить", bg="orange red",
           width=30, height=6).place(relx=0.76, rely=0.82)

    Thread(target=polzvtl).start()

    gui.mainloop()