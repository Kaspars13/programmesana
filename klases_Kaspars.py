# 1.uzdevums
# class Darbinieks:
#     def __init__(self, vards, amats):
#         self.vards = vards
#         self.amats = amats

# jauns_darbinieks = Darbinieks("Anna", "Projekta vadītājs")

# 2.uzdevums
# class Darbinieks:
#     def __init__(self, vards, amats):
#         self.vards = vards
#         self.amats = amats

#     def radit_profilu(self):
#         print(f"Darbinieks: {self.vards}, Amats: {self.amats}")

# jauns_darbinieks = Darbinieks("Anna", "Projekta vadītājs")
# jauns_darbinieks.radit_profilu()


# 3.uzdevums
# class Darbinieks:
#     def __init__(self, vards, amats,):
#         self.vards = vards
#         self.amats = amats
#         self.alga = 3000

#     def paaugstinat_algu(self, summa):
#         jauna_alga = self.alga + summa
#         print(f" Algu paaugstināja par {summa} EUR, tagad junā alga ir {jauna_alga} EUR")

#     def radit_profilu(self):
#         print(f"Darbinieks: {self.vards}, Amats: {self.amats}, Sākotnējā alga: {self.alga} EUR")

# jauns_darbinieks = Darbinieks("Anna", "Projekta vadītājs")
# jauns_darbinieks.paaugstinat_algu(500)
# jauns_darbinieks.radit_profilu()

# 4.uzdevums
# class Darbinieks:
#     def __init__(self, vards, amats, alga=2000):
#         self.vards = vards
#         self.amats = amats
#         self.alga = alga

#     def paaugstinat_algu(self, summa):
#         jauna_alga = self.alga + summa
#         print(f" Algu paaugstināja par {summa} EUR, tagad junā alga ir {jauna_alga} EUR")

#     def radit_profilu(self):
#         print(f"Vārds: {self.vards}, Amats: {self.amats}, Alga: {self.alga} EUR")

# vecs_darbinieks = Darbinieks("Jānis", "Analītiķis")
# vecs_darbinieks.radit_profilu()

# 5.uzdevums

# class Darbinieks:
#     def __init__(self, vards, amats, alga=2000):
#         self.vards = vards
#         self.amats = amats
#         self.alga = alga

#     def paaugstinat_algu(self, summa):
#         if summa <= 0:
#             print("Kļūda: Algas paaugstinājums nevar būtnegatīvs vai nulle!")
#         else:
#             jauna_alga = self.alga + summa
#             print(f" Algu paaugstināja par {summa} EUR, tagad junā alga ir {jauna_alga} EUR")
        

#     def radit_profilu(self):
#         print(f"Vārds: {self.vards}, Amats: {self.amats}, Alga: {self.alga} EUR")

# jauns_darbinieks = Darbinieks("Anna", "Projekta vadītājs", 3000)
# jauns_darbinieks.paaugstinat_algu(200)
# jauns_darbinieks.paaugstinat_algu(-100)