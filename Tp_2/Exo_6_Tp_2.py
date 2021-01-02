arret = "o"
liste = []

while arret == "o":
    string = str(input("Chaîne de caractères : "))
    string = string.upper()
    liste.append(string)
    
    arret = str(input("Voulez-vous continuez la saisie ? (o/n) :"))
    arret = arret.lower()

for element in liste:
    print(element)