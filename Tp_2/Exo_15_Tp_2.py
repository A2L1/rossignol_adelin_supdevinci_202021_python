tete = 35
patte = 94

for i in range (0,tete+1,1):
    if (i*2) + ((tete-i)*4) == 94:
        print("Il y a "+ str(tete-i) + " lapins et " + str(i) + " poules.")