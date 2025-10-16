import tkinter as tk
logs = tk.Tk()
logs.geometry('200x150')

def paradit_ievadi():
    # ievade.get() iegūst informāciju no lauka ievades vērtību
    teksts.config(text="Tu ievadīji: " + ievade.get())


tk.Label(logs, text="Ieavadi kautko!").pack()

#Izveido ievades lauku
ievade = tk.Entry(logs)
ievade.pack()

poga = tk.Button(logs, text="parādīt tekstu",
                 command=paradit_ievadi
                 )
poga.pack()



tk.Label(logs, text="Ieavadi Kautko!").pack()

teksts = tk.Label(logs, text="")
teksts.pack()
logs.mainloop()