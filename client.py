import socket
from tkinter import*
from threading import Thread

port = 4912

def polzvtl():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.56.1", port))
    chat = True

    while chat:
        data = client.recv(1024)
        print(data.decode("utf-8"))
        client.send(input("Отправить::").encode("utf-8"))

        if not data:
            client.close()
            print("Server closed")



def gui_client():
    gui = Tk()
    Thread(target=polzvtl).start()
    gui.geometry("1200x900")
    gui["bg"] = "gray6"
    gui.title("You connected to {}")

    LabelFrame(gui, text = "Отправлять от сюда", highlightthickness=0, bg = "gray15", width = 1200, height = 400,).place(relx = 0, rely = 0.77)
    pole_vvoda = Entry(gui, bg = "gray80", relief = "solid", width = 140)
    pole_vvoda.place(relx = 0.15, rely = 0.95)

    gui.mainloop()