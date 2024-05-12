import requests

base_url = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"
base_url_brandstof = "https://opendata.rdw.nl/resource/8ys7-d773.json"
kenteken = input("Vul uw kenteken in: ")
params = {"kenteken": kenteken.upper()}

try:
    response = requests.get(base_url, params=params)
    response_brandstof_api = requests.get(base_url_brandstof, params=params)
    response.raise_for_status()  # Controleer of het verzoek is gelukt
    if response.raise_for_status() != 200:
        raise ValueError("Er kan geen verbinding gemaakt worden met de server")
    response_brandstof_api.raise_for_status()
    gegevens = response.json()
    gegevens_2 = response_brandstof_api.json()

    merk.api = gegevens[0].get("merk")
    model = gegevens[0].get("handelsbenaming")
    kleur = gegevens[0].get("eerste_kleur")
    bouwjaar = gegevens[0].get("datum_eerste_toelating_dt")
    catalogus_prijs = int(gegevens[0].get("catalogusprijs"))
    brandstof = gegevens_2[0].get("brandstof_omschrijving")
    aantal_zitplaatsen = gegevens[0].get("aantal_zitplaatsen")

    print(f"Merk: {merk}")
    print(f"Model: {model}")
    print(f"Kleur: {kleur}")
    bouwjaar_format = f"{bouwjaar[:4]}"
    print(f"Bouwjaar: {bouwjaar_format}")
    print(f"Catalogus Prijs: EURO:{catalogus_prijs}")
    if brandstof == None:
        brandstof = input("Brandstof niet gevonden, Vul hier uw brandstof type in: ")
    print(f"Brandstof: {brandstof}")
    print(f"Aantal zitplaatsen: {aantal_zitplaatsen}")

except requests.exceptions.RequestException as e:
    print(f"Fout bij het ophalen van gegevens: {e}")
