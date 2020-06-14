from tkinter import *
from random import randrange as rnd, choice
import time
from math import *

dx, dy = (+2, +2)


root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white') #                   |
canv.pack(fill=BOTH, expand=1) #                    | создаем область для отрисовки примитивов и область вывода
l = Label(bg = 'grey', fg = 'white', width = 40) #  | значений счётчика
l.pack()

colors = ['red', 'green', 'blue', 'orange']

def tick():
    global x, y, dx, dy
    x += dx
    y += dy
    if x + r > 800 or x - r <= 0:
        dx = -dx
    elif y + r > 600 or y - r <= 0:
        dy = -dy
    root.after(50, tick)
    canv.move(ball, dx, dy)

def new_ball(): # функция создания шарика в рандомном месте с рандомными размерами и цветом
    canv.delete(ALL)
    global x, y, r, ball
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    ball = canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width = 0)
    tick()

a = []
def click(event): # функция реакции на клик по шарику, добавляет к счётчику значениие
    distance = sqrt((event.x - x) ** 2 + (event.y - y) ** 2)
    if distance <= r:
        a.append(1)
        canv.delete(ball)
        new_ball()
    l['text'] = len(a)




canv.bind('<Button-1>', click)

abc = new_ball()



mainloop()
