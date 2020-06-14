from tkinter import *
from random import randrange as rnd, choice
import time
from math import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog as fd


# #создадим окошко программы
#
# root = Tk()
# root.geometry('1500x1000')
#
# #добавим строку ввода значений
#
# def insertCSV():
#     path_to_file = fd.askopenfilename()
#     return path_to_file

df = pd.read_csv('E:\CSV.csv',
                     parse_dates = ['Date'],
                     index_col= 'Date')

a = df.Close.plot()
a.show()

# e = Entry(width = 30)
# b = Button(text = 'добавить значение')
# b1 = Button(text = 'выстроить график')
# b2 = Button(text = 'импорт CSV', command = insertCSV)
#


#
# e.pack()
# b.pack()
# b1.pack()
# b2.pack()



# mainloop()
#
