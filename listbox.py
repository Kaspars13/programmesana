import tkinter as tk
from tkinter import messagebox

# Galvenais logs
root = tk.Tk()
root.title("Listbox Piemērs")
root.geometry("300x250")

# Funkcija, kas parāda atlasīto elementu
def paradit_izveli():
    try:
        # Iegūstam atlasītā elementa indeksu
        atlasitais_indekss = saraksts.curselection()[0]
        # Iegūstam pašu elementu pēc indeksa
        izveleta_pilseta = saraksts.get(atlasitais_indekss)
        messagebox.showinfo("Jūsu izvēle", f"Jūs izvēlējāties: {izveleta_pilseta}")
    except IndexError:
        # Kļūdas apstrāde, ja nekas nav izvēlēts
        messagebox.showwarning("Kļūda", "Lūdzu, izvēlieties pilsētu no saraksta!")

# Etiķete
tk.Label(root, text="Izvēlieties pilsētu:").pack(pady=5)

# Listbox izveide
saraksts = tk.Listbox(root, height=5) # Augstums - redzamo rindu skaits
saraksts.pack(pady=5)

# Elementu pievienošana sarakstam
pilsetas = ["Rīga", "Liepāja", "Ventspils", "Daugavpils", "Jelgava"]
for pilseta in pilsetas:
    saraksts.insert(tk.END, pilseta) # tk.END nozīmē pievienot beigās

# Poga apstiprināšanai
tk.Button(root, text="Apstiprināt", command=paradit_izveli).pack(pady=20)

root.mainloop()
