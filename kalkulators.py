import tkinter as tk
logs = tk.Tk()
logs.geometry('500x500')
logs.title('Kalkulators')


def saskaitit():
    pirmais_teksts = pirma_ievade.get()
    otrais_teksts = otra_ievade.get()

    pirmais_skaitlis = int(pirmais_teksts)
    otrais_skaitlis = int(otrais_teksts)

    summa = pirmais_skaitlis + otrais_skaitlis
    
    rezultats.config(text=f"Summa: {summa}")

    





tk.Label(logs, text='Ieavadi pirmo skaitli').pack(pady=5)

pirma_ievade = tk.Entry(logs)
pirma_ievade.pack()


tk.Label(logs, text='Ieavdi otro skaitli').pack(pady=5)

otra_ievade = tk.Entry(logs)
otra_ievade.pack()

poga1 = tk.Button(logs, text='Saskaitīt',
                  command=saskaitit
                  ).pack()

rezultats = tk.Label(logs, text='Summa:')
rezultats.pack(pady=5)



logs.mainloop()