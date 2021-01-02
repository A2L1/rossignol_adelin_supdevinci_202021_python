password = str(input("Mot de passe : "))

password = list(password)


minuscule=majuscule=special=chiffre=False

if 6 <= len(password) <= 12:
    for caractere in password:

        if caractere.islower():
            minuscule = True
        elif caractere.isupper():
            majuscule = True
        elif 20 <= int(ord(caractere)) <= 47 or 58 <= int(ord(caractere)) <= 64 or 123 <= int(ord(caractere)) <= 126:
            special = True
        elif 0 <= int(caractere) <= 9:
            chiffre = True

if minuscule==majuscule==special==chiffre:
    print("Mots de passe enregistré")
else:
    print("Saisie incorrecte")