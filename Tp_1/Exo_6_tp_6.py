string = input("String : ")

liste = string.split(",")
liste.sort()
string = ",".join(liste)

print(string)