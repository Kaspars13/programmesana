import csv


# with open('skoleni.csv', 'a', newline='', encoding='utf-8') as f:
#     rakstitajs = csv.writer(f)
#     if f.tell() == 0:
#         rakstitajs.writerow(['Vārds', 'Uzvārds', 'Klase'])
#     rakstitajs.writerow([vards, uzvards, klase])


# dati = [
#     ['Name', 'Age', 'City'],
#     ['Alice', 25, 'New York'],
#     ['Bob', 30, 'Los Angeles'],
#     ['Charlie', 35, 'Chicago'],
# ]

# with open('test.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f, delimiter='|')
#     writer.writerows(dati)

with open('skoleni.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    if f.tell() == 0:
        writer.writerow(['Vārds', 'Uzvārds', 'Klase'])

    while True:
        vards = input("Vārds: ").capitalize()

        if vards == "":
            break

        uzvards = input("Uzvārds: ").capitalize()
        klase = input("Klase: ").upper()

        writer.writerow([vards, uzvards, klase])
a = []
b = []
c = []
with open('skoleni.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    ievade = int(input("1 vai 2: "))
    if ievade != 1 and ievade != 2:
        print("Ievadi pareizu skaitli!!")
    if ievade == 1:
        for rinda in reader:
            if 'A' in rinda['Klase']:
                a.append(rinda['Klase'])
                summa = int(sum(a))
            elif 'B' in rinda['Klase']:
                b.append(rinda['Klase'])
                print(b)
            elif 'C' in rinda['Klase']:
                c.append(rinda['Klase'])
                print(c)
