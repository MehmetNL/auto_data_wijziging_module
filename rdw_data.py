import requests

base_url = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"
kenteken = "P300BB"
params = {"kenteken": kenteken}

try:
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Controleer of het verzoek is gelukt
    gegevens = response.json()

except requests.exceptions.RequestException as e:
    print(f"Fout bij het ophalen van gegevens: {e}")

print(gegevens)















