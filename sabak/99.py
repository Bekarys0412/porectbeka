import tkinter as tk
from tkinter import ttk


class point:
    def _init_(self,x,y):
     self.x = x
     self.y = y



def _str_(self):
    return f"Point {self.x} {self.y}"

def show_day():
    print(combo.get(), combo_int.get())
    if combo_int.get() == '5':
        print('well')


def set_day():
   combo.set('Friday')



weekDays=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sanday")
list_int=[1,2,3,4,5]

win = tk.Tk()
win.geometry(f"300x400+800+150")
win.title('мое первое графическо приложение')

combo=ttk.Combobox(win,values=weekDays)
combo_int=ttk.Combobox(win,values=list_int)
combo_point=ttk.Combobox(win,values = [point(2,5),point(1,1)])
ttk.Button(win,text='show_day',command=show_day).pack()
ttk.Button(win,text='set_day',command=set_day).pack()
combo.current(1)
combo.current(4)
combo.pack()
combo_int.pack()
combo_point.pack()

win.mainloop()
