import requests
import json

requete = requests.get('https://restcountries.eu/rest/v2/region/europe')
events=requete.json()
for i in range (0,len(events)):
    print(str(events[i]['demonym']) + " : " + str(events[i]['population']))
