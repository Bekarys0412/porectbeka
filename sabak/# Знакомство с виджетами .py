 # Знакомство с виджетами .Виджет label

import tkinter as tk

win = tk.Tk()
win.geometry(f"300x400+100+200")
win.title('free fair')

lable_1 = tk.Label(win, text='''Hello!
world!''',
                   bg='red',
                   fg='white',
                   font=('Arial',20,'bold'),
                    # padx=20,
                    # pady=20,
                   width=10,
                   height=10,
                   anchor='sw',
                   relief=tk.RAISED,
                   bd=10,
                   justify=tk.RIGHT
                   )
lable_1.pack()

win.mainloop()