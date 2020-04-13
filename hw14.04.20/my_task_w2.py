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
    text.delete(1.0, END)
    for i in data:
        text.insert(END, f"категория: {i['category']}, имя: {i['name']}, срок исполнения: {i['time']}\n") 

root = Tk()
root.title('менеджер приложений')

frame1 = Frame(root)
frame1.grid(row=0, column=0)
frame2 = Frame(root)
frame2.grid(row=0, column=1)

text = Text(frame2,width=60, height=9,wrap=WORD)
text.pack(side=LEFT)
scroll = Scrollbar(frame2,command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)


label1= Label(frame1,text='задача:',)
label1.grid(row=0, column=0)
entry1 = Entry(frame1)
entry1.grid(row=0, column=1)

label2= Label(frame1,text='категория:',)
label2.grid(row=1, column=0)
entry2 = Entry(frame1)
entry2.grid(row=1, column=1)

label3= Label(frame1,text='время:',)
label3.grid(row=2, column=0)
entry3 = Entry(frame1)
entry3.grid(row=2, column=1)

button1 = Button(frame1,text='заказать', command=set_task)
button1.grid(row=3, column=1)
button2 = Button(frame1,text='список задач', command=show_tasks)
button2.grid(row=4, column=1)
button3 = Button(frame1,text='выход', command=exit)
button3.grid(row=5, column=1)



root.mainloop()
