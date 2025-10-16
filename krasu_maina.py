import tkinter as tk
logs = tk.Tk()
logs.geometry('500x500')

def krasas_maina():
    krasa = krasas_ievade.get()

    logs.config(bg=krasa)

tk.Label(logs, text='Ieavadi krāsu(angļu valodā)').pack(pady=10)

krasas_ievade = tk.Entry(logs)
krasas_ievade.pack(pady=10)

poga = tk.Button(logs, text='Nomaini krāsu!',
                 command=krasas_maina
                 )
poga.pack()
logs.mainloop()

