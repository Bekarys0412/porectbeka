import tkinter as tk
h= 500
w=600
win = tk.Tk()
win.title('gta 7')
win.geometry(f"{h}x{w}+200+100")
win.resizable(True,True)
label_1 = tk.Label(win, text= 'minecraft pe' ,
                   bg= 'green',
                   fg= 'grey',
                   font=('arial',25, 'bold'),
                   #padx= 15,
                   #pady=15,
                   width=40,
                   height=40,
                   anchor='center',
                   )
label_1.pack()
                           

win.mainloop()