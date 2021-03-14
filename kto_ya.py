from tkinter import *
import server
import client
import threading
from PIL import Image, ImageTk

def vibor(nickname):
    who_im = Tk()
    who_im.title("Выбор дальнейшего использования")
    who_im["bg"] = "gray22"
    who_im.geometry("900x800")

    matrisa = Canvas(who_im, width = 800, height = 350, bg = "gray22", highlightthickness=0)

    img = Image.open("images/matrisa_tabletka.jpg")
    image = ImageTk.PhotoImage(img)
    matrisa.create_image(300, 200, image = image)
    matrisa.place(relx = 0.17, rely = 0.17)

    message = f'''Здравствуйте {nickname}, cтановясь сервером, вы тоже сможете общаться с пользователями,
                  но перед этим вам нужно будет дождаться подключения собеседников
                   и сообщить им свой IPv4 адресс для подключения.
                Сервер будет поддерживать чат и немного дополнительно нагружать вашу систему.
                Для создания сервера не требуется указывать какие-либо данные.'''

    info = Label(who_im, text = message, bg = "gray22", font = ("Times New Roman", "16"),fg='orange red')
    info.place(relx = 0.025, rely = 0.01)
    LabelFrame(text="Сервер", font=("Times New Roman", "21"), height=200, width=350, bg="gray22").place(
        relx=0.08, rely=0.67)

    Button(who_im,command =  lambda: threading.Thread(target = server.gui_server).start(), text = "Создать свой\n сервер",
font = ("Times New Roman", "20"), width = 15,bg = "orange red", fg = "black").place(relx = 0.15, rely = 0.75)

    client_frame = LabelFrame(text = "Клиент",font = ("Times New Roman", "21"), height = 300, width = 350, bg = "gray22").place(relx = 0.6, rely = 0.61)
    Label(client_frame, text = "Пожалуйста заполните\n необходимые\n"
                              " для подключения данные", bg = "gray22",font = ("Times New Roman", "14"),fg="black").place(relx = 0.68,rely = 0.65)

    Label(client_frame, text = "IPv4 адресс\n сервера :", bg = "gray22", font = ("Times New Roman", "14"),fg="black").place(relx = 0.62,rely = 0.75)
    Text(client_frame, relief = "solid", bg="burlywood4", width = 25, height = 1).place(relx = 0.74,rely = 0.77)


    Button(who_im, command = lambda: threading.Thread(target = client.gui_client).start(), text="Войти на сервер\nкак клиент",
font=("Times New Roman", "20"), width = 15,bg="orange red", fg="black").place(relx=0.67, rely=0.85)

    who_im.mainloop()