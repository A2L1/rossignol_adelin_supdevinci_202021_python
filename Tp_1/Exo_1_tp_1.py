liste = "Valeurs :"

for i in range (2000, 3200, 1):
    if i%7 == 0 and not (i%5 == 0):
        liste = liste + str(i) + ","

print(liste)
