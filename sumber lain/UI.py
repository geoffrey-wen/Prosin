import tkinter as tk
from tkinter import *
from tkinter.ttk import *

main_window = Tk()
main_window.title('Line 404')
main_window.geometry('1000x1000')

arrowright = PhotoImage(file = "right.png")

image1 = tk.Label(main_window, image = arrowright, compound = 'center')
image1.grid(column = 2 + 1, row=6)
image1.config(height=30, width=30)

main_window.mainloop()