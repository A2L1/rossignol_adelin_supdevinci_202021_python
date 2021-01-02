import requests
import json

requete = requests.get('https://restcountries.eu/rest/v2/region/europe')
events=requete.json()
print(events[0]['region'])

for i in range (0,len(events)):
    print(str(events[i]['region']) + " : " + str(events[i]['subregion']))