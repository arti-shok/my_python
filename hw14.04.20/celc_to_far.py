from tkinter import *

def converter():
    try:
        label2.config(text=str(int(entry.get())*9/5+32))
    except:
        label2.config(text='ошибка ввода')

root = Tk()
root.title('конвертер градусов')

frame = Frame(root)
label1 = Label(frame,text='температура в цельсиях:')
label1.pack()
frame.pack()
entry = Entry(frame)
entry.pack()
label2 = Label(frame)
label2.pack()

button1 =  Button(frame, text='конвертировать!', command=converter)
button1.pack()
button2 =  Button(frame, text='выход', command=exit)
button2.pack()
root.mainloop()