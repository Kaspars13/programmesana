import csv

# dati = [
#     ['Vards', 'Klase', 'Gads'],
#     ['Juris', '12.c' , 2007],
#     ['Anna', '12.c', 2008],
# ]

# with open('dati_rakst.csv', 'w', newline='') as r:
#     rakstitajs = csv.writer(r, delimiter= '|')
#     rakstitajs.writerows(dati)




vards = input("Ieavdi skolēna vārdu: ")
uzvards = input('Ievadi skolēna uzvārdu: ')
gads = input('Ievadi skolēna dzimšanas gadu: ')

with open('dati_rakst.csv', 'w', newline='') as fails:
    rakstitajs = csv.writer(fails)
    rakstitajs.writerow([vards,uzvards,gads])