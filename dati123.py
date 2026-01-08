import json
#3
# with open('draugi.json', 'r', encoding='utf8') as fails:
#     data = json.load(fails)

# print(data[0]["Vecums"])


#4
# dati = {"nosaukums" : "Mana skola", "klase" : 12, "priekšmeti" : ["matemātika", "latviešu valoda"]}

# with open('mana_skola.json', 'w', encoding='utf8') as fails:
#     json.dump(dati, fails)

# with open('mana_skola.json', 'r', encoding='utf8') as fails:
#     data = json.load(fails)

# print(data["priekšmeti"])

#5
# with open('atzimes.json', 'r', encoding='utf8') as fails:
#     data = json.load(fails)

# vid_atzime_janis = sum(data[0]["atzīmes"]) / 3
# print(f"Jāņa vidējā atzīme ir {vid_atzime_janis}")

# vid_atzime_anna = sum(data[1]["atzīmes"]) / 3
# print(f"Annas vidējā atzīme ir {vid_atzime_anna}")

#6

# with open('titanic.json', 'r', encoding='utf8') as fails:
#     data = json.load(fails)

# print(len(data))

#7

# with open('titanic.json', 'r', encoding='utf8') as fails:
#     data = json.load(fails)

# izdzivoja = 0

# for pasazieris in data:
#     if pasazieris["Survived"] == 1:
#         izdzivoja += 1
# print(f"Izdzīvoja {izdzivoja} cilvēki")
