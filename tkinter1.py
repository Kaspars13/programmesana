import tkinter as tk
logs = tk.Tk()

#Loga virsaksts
logs.title("Pirmais logs")
#Loga krāsa
logs.config(bg='#AD27F5')
#Loga izmērs un kreisā augšējā stūra koordinātes
logs.geometry("300x300+1100+100")
#Mazākais loga izmērs
logs.minsize(100, 100)
#Lielākais loga izmērs
logs.maxsize(1000, 1000)
#Tiesības mainīt loga izmēru (platums, augstums), True var mainīt, Flase nevar mainīt
logs.resizable(True, True)

#Logā izveido label jeb etiķeti
teksts_1 = tk.Label(logs, text='''Labie darbi!'
'Dari vienmēr labu!''',
                    bg='green', #fona krāsa
                    fg='white', #rakstzīmju krāsa
                    #fonts, izmērs, treknraksts
                    font=('Arial',10, 'bold'),
                    #izmērs pikseļos
                    padx=20,
                    pady=20,
                    #loga izmērs
                    width=13,
                    height=3,
                    #Teksta novietojums etiķetē/label
                    anchor='ne',    
                    #Lauka telpiskums
                    relief=tk.RAISED,
                    bd=10,
                    #Teksta līdzinājums
                    justify=tk.CENTER
                    )

def ziemas_teksts():
    print("Ziemā snieg")

poga1 = tk.Button(logs, text='Ziema',
                  command=ziemas_teksts
                  )

def teksta_lauks1():
    tekstsLoga1 = tk.Label(logs, text='Spoži spīd saule!')
    tekstsLoga1.pack()

poga2 = tk.Button(logs, text='Vasara',
                  command=teksta_lauks1
                  )

poga3 = tk.Button(logs, text='Funkcija lambda',
                  command=lambda:tk.Label(logs, text='Īsāks koda pieraksts').pack()
                  )

exit_button = tk.Button(
    logs,
    text = 'Exit',
    command=lambda: logs.quit()
)

teksts_1.pack()
poga1.pack()
poga2.pack()
poga3.pack()
exit_button.pack()
logs.mainloop()