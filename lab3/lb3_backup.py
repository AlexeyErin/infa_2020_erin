from tkinter import *
from random import randrange as rnd, choice
import time
from math import *

WIDTH = 800
HEIGHT = 600

root = Tk()
root.geometry(str(WIDTH) + 'x' + str(HEIGHT))

a = []

canv = Canvas(root, bg='white') #                   |
canv.pack(fill=BOTH, expand=1) #                    | создаем область для отрисовки примитивов и область вывода
l = Label(bg = 'grey', fg = 'white', width = 40) #  | значений счётчика
l.pack()

class my_ball():



    def new_ball(self):  # функция создания шарика в рандомном месте с рандомными размерами и цветом
        canv.delete(ALL)
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.dx, self.dy = (+2, +2)
        self.colors = ['red', 'green', 'blue', 'orange']
        canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r,
                                self.y + self.r, fill=choice(self.colors), width=0)
        my_ball.tick(self)
        l['text'] = len(a)
        root.after(10000, self.new_ball)

    def tick(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.r > 800 or self.x - self.r <= 0:
            self.dx = -self.dx
        elif self.y + self.r > 600 or self.y - self.r <= 0:
            self.dy = -self.dy
        root.after(50, self.tick)
        canv.move(my_ball
                  , self.dx, self.dy)

def click(event):
    distance = sqrt((event.x - bal.x) ** 2 + (event.y - bal.y) ** 2)
    if distance <= bal.r:
        a.append(1)
        bal.new_ball(bal.number)


canv.bind('<Button-1>', click)


bal = my_ball()
bal.new_ball()
bal23 = my_ball()
bal23.new_ball()


mainloop()
