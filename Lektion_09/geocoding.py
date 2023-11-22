import requests

def geocode(adresse):
    url = "https://nominatim.openstreetmap.org/search"

    query_parameter = {
        "q": adresse,
        "format": "json"
    }

    header = {
        "User-Agent": "FHNW Webbrowser V1.1 Sina"
    }

    r = requests.get(url, params = query_parameter, headers=header)

    if r.status_code == 200:
        data = r.json()
        return data
    else: 
        print(f"Fehler!!")

resultat = geocode("Hofackerstrasse 30, 4132 Muttenz, Schweiz")
print(resultat)