import requests

base_url = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"
kenteken = input("Vul uw kenteken in: ")
params = {"kenteken": kenteken.upper()}

try:
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Controleer of het verzoek is gelukt
    gegevens = response.json()

    merk.api = gegevens[0].get("merk")
    model = gegevens[0].get("handelsbenaming")
    kleur = gegevens[0].get("eerste_kleur")
    bouwjaar = gegevens[0].get("datum_tenaamstelling")
    catalogus_prijs = int(gegevens[0].get("catalogusprijs"))
    brandstof = gegevens[0].get("voertuigen_brandstof")
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
