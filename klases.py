# class Cars:
#     make = "Audi"
# my_car = Cars

# print(my_car.make)

# class Cars:
    
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.atrums = 0

#     def info(self):
#         print(f'Auto: {self.make} {self.model} {self.year}')

#     def paatrinat(self, pieagums):
#         self.atrums += pieagums
#         print(f'Notiek atruma palielinasana. Jaunais atrums ir {self.atrums}')

#     def bremzet(self, samazinajums):
#         self.atrums -= samazinajums
#         if self.atrums < 0:
#             print('Nevare braukt atpakal gaita ar bremzesanu')
#         else:
#             print(f'Notiek atruma samazinasana. Jaunais atrums {self.atrums}')


# my_car = Cars("Audi", "A4", 2008)
# my_car.info()
# my_car.paatrinat(50)
# my_car.bremzet(60)

# class Persona:
#     def __init__(self, vards, uzvards):
#         self.vards = vards
#         self.uzvards = uzvards
#     def pilns_vards(self):
#         return self.vards + " " + self.uzvards

# vards1 = Persona('Kaspars', 'Sokolovs')
# print(vards1.pilns_vards())
        

# class Rinkis:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def laukums(self):
#         S = 3.14 * self.radius ** 2
#         return f"Riņķa laukums ir {S}"
    
#     def rinka_linija(self):
#         C = 2 * 3.14 * self.radius
#         return f"Riņķa līnijas garums ir {C}"
    
# radius1 = Rinkis(3)
# print(radius1.laukums())
# print(radius1.rinka_linija())


# class Persona:
#     def __init__(self, vards, valsts, dz_gads):
#         self.vards = vards
#         self.valsts = valsts
#         self.dz_gads = dz_gads

#     def vecums(self):
#        return 2025 - self.dz_gads
    
# persona1 = Persona("Jānis", "Latvija", 2000)
# print(persona1.vecums())
from datetime import date

class Persona:
    def __init__(self, vards, valsts, dz_datums):
        self.vards = vards
        self.valsts = valsts
        self.dz_datums = dz_datums

    def vecums(self):
        return date.today().year - self.dz_datums.year
    
persona1 = Persona("Jānis", "Latvija", date(2000,1,1))
print(persona1.vards, persona1.vecums(), 'gadi')