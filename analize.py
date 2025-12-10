import csv

#2.uzdevums

# with open('dati.csv', encoding='utf-8') as f:
#     lasitajs = csv.DictReader(f)
#     for rinda in lasitajs:
#         print(rinda['Skolena_ID'], rinda['Vards'], rinda['Kurss'], rinda['Punktu_Skaits'])


#3.uzdevums


#3.1 uzd
# with open('dati.csv', encoding='utf-8') as f:
#     lasitajs = csv.DictReader(f)
#     for rinda in lasitajs:
#         if int(rinda['Punktu_Skaits']) > 80:
#             print(f"Skolēni ar vairāk par 80 punktiem ir {rinda['Vards']} ({rinda['Punktu_Skaits']})")

#3.2 uzd

# fizika = []
# matematika = []
# programmesana = []

# with open('dati.csv', encoding='utf-8') as f:
#     lasitajs = csv.DictReader(f)
#     for rinda in lasitajs:
#         if rinda['Kurss'] == 'Fizika':
#             fizika.append(int(rinda['Punktu_Skaits']))
#         elif rinda['Kurss'] == 'Matematika':
#             matematika.append(int(rinda['Punktu_Skaits']))
#         elif rinda['Kurss'] == 'Programmesana':
#             programmesana.append(int(rinda['Punktu_Skaits']))
#         else:
#             print(f"Nestrada")
#     vid_fiz = sum(fizika) / len(fizika)
#     vid_mat = sum(matematika) / len(matematika)
#     vid_prog = sum(programmesana) / len(programmesana)
#     if vid_fiz < vid_mat:
#         print(f"Zemākais punktus skaits ir: Fizika")
#     elif vid_mat < vid_fiz:
#         print(f"Zemākais punktus skaits ir: Matemātikā")
#     elif vid_prog < vid_fiz:
#         print(f"Zemākais punktus skaits ir: Programmēšanā")
#     elif vid_fiz < vid_prog:
#         print(f"Zemākais punktus skaits ir: Fizika")
#     elif vid_prog < matematika:
#         print(f"Zemākais punktus skaits ir: Programmēšanā")
#     elif vid_mat <vid_prog:
#         print(f"Zemākais punktus skaits ir: Matemātikā")
# Es zinu, ka varēja izdarīt šo te visu īsāku, bet man šodien galva nestrād, lai to izdomātu.

#3.3

# nepietiekams_rezultats = 50

# with open('dati.csv', encoding='utf-8') as f:
#     lasitajs = csv.DictReader(f)
#     for rinda in lasitajs:
#         if rinda['Kurss'] == 'Fizika' and int(rinda['Punktu_Skaits']) < nepietiekams_rezultats:
#             print(f"Nepietiekami rezultāti Fizikas kursā: {rinda['Vards']} (ID:{rinda['Skolena_ID']})")
