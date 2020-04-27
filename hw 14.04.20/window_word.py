from tkinter import *
from random import choice

def check_translation():
    if entry.get()==dct[word]:
        label3.config(text='угадали')
    else:
        label3.config(text='не угадали')

with open('C:\\Users\\iriska\\my_project\\my_python\\hw14.04.20\\enrus.txt','r') as f:
    r = f.readlines()
data = [x.strip() for x in r]
a = data[0::2]
b = data[1::2]
dct = (dict(zip(a,b)))
word = choice(a)

root = Tk()
root.title('назови перевод')

frame = Frame(root)
frame.pack()
label1 = Label(frame,text='случайное слово:\n'+word)
label1.pack()
label2 = Label(frame,text = 'укажите перевод слова:')
label2.pack()
entry = Entry(frame)
entry.pack()
label3 = Label(frame)
label3.pack()

button1 =  Button(frame, text='готово', command=check_translation)
button1.pack()
button2 =  Button(frame, text='выход', command=exit)
button2.pack()
root.mainloop()
