x,y = int(input("Valeur de x : ")),int(input("Valeur de y : "))


for i in range (1, x+1, 1):
    ligne= ""
    for j in range (1, y+1, 1):
        ligne = ligne +" "+str(i*j)
    print(ligne)