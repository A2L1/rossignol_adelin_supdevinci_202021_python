def compare(string1,string2):
    if len(string1) > len(string2):
        print(string1)
    elif len(string1) < len(string2):
        print(string2)
    else:
        print(string1)
        print(string2)

string1 = str(input("Chaîne 1 : "))
string2 = str(input("Chaîne 2 : "))

compare(string1,string2)