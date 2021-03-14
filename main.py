from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk
import registr


def main():
    create_okno()

def create_okno():
    okno = Tk()
    okno.title("Сервер-Клиент.beta")
    okno.geometry("{}x{}".format(1200,900))
    okno["bg"] = "gray22"
    canva = Canvas(okno, width = 1000, height = 800, bg = "gray22", highlightthickness=0)

    def quite():
        okno.destroy()
        registr.sled_okno()

    img = Image.open("images/durov3.jpg")
    image = ImageTk.PhotoImage(img)
    canva.create_image(550, 550, image = image)

    canva.pack()
    info = '''                Здравствуйте, вас приветстувует приложение
              "клиент-сервер" воплощающее чат с кем-либо.
              Чтобы начать перпеписку, вам потребуется пройти
              легкую регистрацию. Затем нужно будет
              отправить данную программу необходимому
              собеседнику и вы сможете общаться.
    '''
    canva.create_text(500, 165, text = info, fill = "indian red",
                     font = ("Times New Roman", "27"))

    btn_start = Button(okno, width = 15, height = 2, text = "Зарегистрироваться", font = ("Times New Roman", "20"),
    command = quite, bg = "orange red", fg = "black")


    btn_start.place(x = 300, y = 10)
    btn_start.pack()


    okno.mainloop()
main()
