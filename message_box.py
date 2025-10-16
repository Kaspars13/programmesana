import tkinter as tk
from tkinter import messagebox


# Definē galveno logu
root = tk.Tk()

# loga virsraksts 
root.title("Loga virsraksts")
# Loga izmēri (widthxheight)
root.geometry('400x300')


messagebox.showwarning("warning","This is a Warning") 

messagebox.showerror("errorWindow","oops!!!Error") 

# Palaiž programmu
root.mainloop()