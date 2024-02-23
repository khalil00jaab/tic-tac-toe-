import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("TIC-TAC-TOE")

chiffres = list(range(1, 10))

mark = ''

count = 0
panneaux = ['placeholder'] + [''] * 9

window.mainloop()
