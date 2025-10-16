import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Krāsu mikseris")
root.geometry("500x500")
root.config(bg="#FFFFFF")

def rgb_to_hex(sarkans,zals,zils):
    return f"#{sarkans:02x}{zals:02x}{zils:02x}"

def mainit_krasu():
    sarkans = slidnis_sarkans.get()
    zals = slidnis_zals.get()
    zils = slidnis_zils.get()

    hex_krasas = rgb_to_hex(sarkans,zals,zils)
    root.config(bg=hex_krasas)
    messagebox.showinfo("Aktuālās krasās", f"Sarkans: {sarkans}, Zaļš: {zals}, Zils: {zils}")



tk.Label(root, text="Sarkans").pack()
slidnis_sarkans = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
slidnis_sarkans.pack(fill='x')
tk.Label(root, text="Zaļš").pack()
slidnis_zals = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
slidnis_zals.pack(fill='x')
tk.Label(root, text="Zils").pack()
slidnis_zils = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
slidnis_zils.pack(fill='x')


tk.Button(root, text="Apstiprināt", command=mainit_krasu).pack(pady=20)


root.mainloop()