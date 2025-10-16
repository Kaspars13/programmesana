import tkinter as tk
from tkinter import messagebox

# Galvenais logs
root = tk.Tk()
root.title("Radio Pogas Piemērs")
root.geometry("300x200")

# Mainīgais, kas glabās izvēlēto vērtību
izvele = tk.StringVar(value="Latviešu") # Noklusējuma vērtība

# Funkcija, kas parāda izvēli
def paradit_izveli():
    messagebox.showinfo("Jūsu izvēle", f"Jūs izvēlējāties: {izvele.get()}")

# Etiķete (Label)
tk.Label(root, text="Izvēlieties valodu:").pack(pady=5)

# Radio pogu izveide
tk.Radiobutton(root, text="Latviešu", variable=izvele, value="Latviešu").pack(anchor='w')
tk.Radiobutton(root, text="Angļu", variable=izvele, value="Angļu").pack(anchor='w')
tk.Radiobutton(root, text="Vācu", variable=izvele, value="Vācu").pack(anchor='w')

# Poga apstiprināšanai
tk.Button(root, text="Apstiprināt", command=paradit_izveli).pack(pady=20)

root.mainloop()
