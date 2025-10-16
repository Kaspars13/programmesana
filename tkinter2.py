import tkinter as tk
logs = tk.Tk()

logs.title("Mans logs")
logs.geometry("500x200")

teksts_1 = tk.Label(logs, text='Mācāmies Python OOP',
                    fg='green',
                    font=('Arial', 10, 'bold'),
                    )

def samainit_tekstu():
    teksts_1.config(text='Teksts tika samainīts!',
                    fg='red',
                    ) # Funkcija nomaina veco tekstu uz jauno.

poga1 = tk.Button(logs, text='Samainīt tekstu',
                  command=samainit_tekstu
                  )

teksts_1.pack()
poga1.pack()
logs.mainloop()