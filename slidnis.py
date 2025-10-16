import tkinter as tk
from tkinter import messagebox

# Galvenais logs
root = tk.Tk()
root.title("Slider Piemērs")
root.geometry("300x150")

# Funkcija, kas parāda slīdņa vērtību
def paradit_vertibu():
    vertiba = slidnis.get()
    messagebox.showinfo("Izvēlētā vērtība", f"Slīdņa vērtība ir: {vertiba}")

# Etiķete
tk.Label(root, text="Izvēlieties vērtību (0-100):").pack(pady=10)

# Slider (Scale) izveide
slidnis = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
slidnis.pack(pady=5, padx=20, fill='x')

# Poga apstiprināšanai
tk.Button(root, text="Apstiprināt", command=paradit_vertibu).pack(pady=10)

root.mainloop()
