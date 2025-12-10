edienkarte = []
for i in range(3):
    edienkarte.append(input("Ieavdi Ēdienu: "))
print(edienkarte)

with open("edienkarte.txt", "w") as fails:
    fails.writelines(edienkarte)
    print("Saturs tika pievienots.")