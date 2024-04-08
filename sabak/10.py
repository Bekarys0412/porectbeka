import tkinter as tk
from random import shuffle
from tkinter import _Anchor, _ButtonCommand, _Compound, _Cursor, _ImageSpec, _Relief, _ScreenUnits, _TakeFocusValue, Misc, Variable
from tkinter.font import _FontDescription

import tkinter.messagebox
from typing import Any
from typing_extensions import Literal

colors = ['#FFFFFF', '#0000FF', '#008200', '#FF0000', '#000084', '#840000', '#008284', '#840084','#000000']


class MyButton(tk.Button):


    def __init__(self, master, x, y, number=0, is_mine=False, *args, **kwargs):
        super().__init__(master, height=0, width=3, font="Calibri 15 bold",*args, **kwargs)
        self.x = x
        self.y = y
        self.__job = None
        self.number = number
        self.count_bomb = 0
        self.is_open = False