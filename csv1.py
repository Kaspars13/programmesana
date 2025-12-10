import csv 


with open('students0.csv', encoding='utf-8') as f:
    lasitajs = csv.reader(f)
    for rinda in lasitajs:
        print(f"{rinda[0]} is in {rinda[1]}")