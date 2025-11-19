# 1.uzdevums
# atzimes = {
#     "Jānis" : 10,
#     "Andris" : 6,
#     "Anna" : 7,
#     "Juris" : 9,
#     "Kristaps" : 4,
# }
# vards = atzimes.keys()
# print(vards)

# atzime = atzimes.values()
# print(atzime)

# print(atzimes["Andris"])

# atzimes.update({"Kārlis" : 9})
# print(atzimes)

# atzimes.pop("Jānis")
# print(atzimes)

# if "Mārtiņš" in atzimes:
#     print("Jā, Mārtīņš ir vārdnīcā.")
# else:
#     print("Nē, Mārtiņš nav vārdnīcā.")

# 2.uzdevums

# auglu_krasas = {'ābols' : 'sarkans', 'banāns' : 'dzeltens', 'apelsīns' : 'oranžs'}

# auglu_krasas.update({'bumbiers' : 'zaļš'})
# print(auglu_krasas)

# auglu_krasas['ābols'] = "zaļš"
# print(auglu_krasas)

# print(auglu_krasas.values())

# if 'ābols' in auglu_krasas:
#     print(auglu_krasas['ābols'])
# else:
#     print("Šāda augļa nav")

# 3.uzdevums

# auto = {
#     'Audi' : 2010,
#     'BMW' : 1998,
#     'Mercedes' : 2007,
#     'Ford' : 1964,
#     'Nissan' : 2025,
# }

# for x, y in auto.items():
#     print(x, y)

# if 'Audi' in auto:
#     print("Jā, Audi ir vārdnīcā")
# else:
#     print("Audi, nav vārdnīcā.")

# for marka, gads in auto.items():
#     if gads < 2010:
#         print(marka)

# 4.uzdevums

# auto = {
#     "marka" : "Audi",
#     "modelis" : "A4",
# }

# Jāpabeidz ir vēl šis

# 5.uzdevums

personas = {
    "persona1" : {
        "vārds" : "Anna",
        "vecums" : 28,
        "pilsēta" : "Rīga"
    },
    "persona2" : {
        "vārds" : "Jānis",
        "vecums" : 34,
        "pilsēta" : "Liepāja",
    },
    "persona3" : {
        "vārds" : "Ilze",
        "vecums" : 25,
        "pilsēta" : "Jelgava",
    }
}

for x, y in personas.items():
    print(x)

    for z in y:
        print(z + ':',y[z] )
