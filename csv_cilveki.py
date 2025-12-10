import csv 

#1.uzdevums
# with open('cilveki.csv', encoding='utf-8') as f:
#     lasitajs = csv.DictReader(f)
#     for rinda in lasitajs:
#         print(rinda['vards'], rinda['uzvards'])

#2.uzdevums

# vecumi = []


# with open('cilveki.csv', encoding='utf-8') as f:
#     lasitajs = csv.DictReader(f)
#     for rinda in lasitajs:
#         vecumi.append(int(rinda['vecums']))
#     vid_vec = sum(vecumi) / len(vecumi)
#     print(f"Vidējais vecums ir {vid_vec}")

#3.uzdevums
# sievietes = []
# with open('cilveki.csv', encoding='utf-8') as f:
#     lasitajs = csv.DictReader(f)
#     for rinda in lasitajs:
#         if 's' in rinda['dzimums']:
#             sievietes.append(rinda['dzimums'])
#     print(sievietes)

with open('cilveki.csv', encoding='utf-8') as f:
    pass