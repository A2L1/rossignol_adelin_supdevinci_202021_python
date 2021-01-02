def search(element,liste):
    if element in liste:
        print(liste.index(str(element)))

liste = ["P1ul675","toto","JEsuiSM1ade",'1234567890111213',"test"]
liste = sorted(liste)
search('test',liste)
    
