def verification(password):
#P@ul675,toto,JEsuiSM@1ade,1234567890111213
    """ Fonction vérifiant la validité d'un mot de passe

    >>>verification(P@ul675)
    True
    >>>verification(toto)
    False
    >>>verification(JEsuiSM@1ade)
    True
    >>>verification(1234567890111213)
    False
    """
    minuscule=majuscule=special=chiffre=False
    if 6 <= len(password) <= 12:
    #Vérifie si la longueur du mot de passe est valide
        for caractere in password:
            #Vérifie la validité de chaque caractère
            if caractere.islower():
                minuscule = True
            elif caractere.isupper():
                majuscule = True
            elif 20 <= int(ord(caractere)) <= 47 or 58 <= int(ord(caractere)) <= 64 or 123 <= int(ord(caractere)) <= 126:
                special = True
            elif 0 <= int(caractere) <= 9:
                chiffre = True

    if minuscule==majuscule==special==chiffre==True:
        return  minuscule==majuscule==special==chiffre
        #Return True si le mot de passe est valide sinon false

string = str(input("Ensemble des mots de passe : "))
#Permet de saisir la chaine de mot de passe exemple : P@ul675,toto,JEsuiSM@1ade,1234567890111213
liste = string.split(",")
print(liste)
password = []
#Transfome la chaine de caractère en liste de mot de passe
for element in liste:
    if verification(element):
        #Vérifie chaque mot de passe dans la liste
        password.append(element)

print(password)
#Affiche une liste ds mots de passe valides 