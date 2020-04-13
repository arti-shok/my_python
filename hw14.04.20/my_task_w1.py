from tkinter import *
from json import *

with open('C:\\Users\\iriska\\my_project\\my_python\\hw14.04.20\\to_do.json','r') as f:
    r = f.read()
data = loads(r)

def set_task():
    data.append({'category':entry2.get(),'name':entry1.get(),'time':entry3.get()})
    with open('C:\\Users\\iriska\\my_project\\my_python\\hw14.04.20\\to_do.json','w') as f:
        f.write(dumps(data))


def show_tasks():
    for i in data:
        print(f"категория: {i['category']}, имя: {i['name']}, срок исполнения: {i['time']}")

root = Tk()
root.title('менеджер приложений')

frame = Frame(root)
frame.pack()
label1= Label(frame,text='задача:',)
label1.grid(row=0, column=0)
entry1 = Entry(frame)
entry1.grid(row=0, column=1)

label2= Label(frame,text='категория:',)
label2.grid(row=1, column=0)
entry2 = Entry(frame)
entry2.grid(row=1, column=1)

label3= Label(frame,text='время:',)
label3.grid(row=2, column=0)
entry3 = Entry(frame)
entry3.grid(row=2, column=1)

button1 = Button(frame,text='заказать', command=set_task)
button1.grid(row=3, column=1)
button2 = Button(frame,text='список задач', command=show_tasks)
button2.grid(row=4, column=1)
button3 = Button(frame,text='выход', command=exit)
button3.grid(row=5, column=1)

root.mainloop()
