arret = "o"
liste = []

while arret == "o":
    string = str(input("Chaîne de caractères : "))
    information = tuple(string.split())

    liste.append(information)
    
    arret = str(input("Voulez-vous continuez la saisie ? (o/n) :"))
    arret = arret.lower()

print(sorted(liste))
