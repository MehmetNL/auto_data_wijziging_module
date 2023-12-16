import sqlite3

import print_gegevens_auto
from versie_def import versie_info
import requests
versie_info()

db = sqlite3.connect("auto_data.db")
cursor = db.cursor()


def data_invoegen_db(Kenteken, Merk, Model, Kleur, Bouwjaar, Nieuw_prijs, Brandstof, aantal_zitplaats,Regisratie_land):
    cursor.execute("INSERT INTO auto_voorraad VALUES (?,?,?,?,?,?,?,?,?)", (
    Kenteken, Merk, Model, Kleur, Bouwjaar, Nieuw_prijs, Brandstof, aantal_zitplaats, Regisratie_land))
    db.commit()

def controleer_kenteken(Kenteken):
    cursor.execute("SELECT COUNT(*) FROM auto_voorraad WHERE Kenteken = ?", (Kenteken,))
    result = cursor.fetchone()
    count = result[0] #[0] moet tupel omgezet worden in list, zodat vergelijk gemaakt kan worden
    return count

def sluit_verbinding():
    db.commit()
    db.close()

def nieuwe_auto_toevoegen():
    base_url = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"
    kenteken = input("Vul uw kenteken in: ").upper()
    params = {"kenteken": kenteken}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Controleer of het verzoek is gelukt
        gegevens = response.json()

        merk_api = gegevens[0].get("merk")
        model_api = gegevens[0].get("handelsbenaming")
        kleur_api = gegevens[0].get("eerste_kleur")
        bouwjaar_api = gegevens[0].get("datum_tenaamstelling")
        catalogus_prijs_api = gegevens[0].get("catalogusprijs")
        brandstof_api = gegevens[0].get("voertuigen_brandstof")
        aantal_zitplaatsen_api = gegevens[0].get("aantal_zitplaatsen")







    except requests.exceptions.RequestException as e:
        print(f"Fout bij het ophalen van gegevens: {e}")



    try:
        count = controleer_kenteken(kenteken)
        if count > 0:
            print("Kenteken {} bestaat al in uw auto voorraad".format(kenteken))
            return
        Merk = merk_api.capitalize()
        Model = model_api.capitalize()
        Kleur = kleur_api.capitalize()
        if bouwjaar_api == None:
            bouwjaar_api = input("Bouwjaar niet gevonden, voer uw bouwjaar in: ")
        Bouwjaar = bouwjaar_api
        if catalogus_prijs_api == None:
            catalogus_prijs_api = input("Catalogusprijs niet gevonden, voer uw Catalogusprijs in:")
        Nieuw_prijs = catalogus_prijs_api
        if brandstof_api == None:
            brandstof_api = input("Brandstof niet gevonden, Vul hier uw brandstof type in: ")
            print(f"Brandstof: {brandstof_api}")
        Brandstof = brandstof_api.capitalize()
        aantal_zitplaats = aantal_zitplaatsen_api
        Registratie_land = input("Registratie Land: ").upper()
        data_invoegen_db(kenteken, Merk, Model, Kleur, Bouwjaar, Nieuw_prijs, Brandstof, aantal_zitplaats,Registratie_land)
        print("Voertuig {} is toegevoegd".format(kenteken))
        sluit_verbinding()
    except sqlite3.IntegrityError:
        print("Database error, kan geen gegevens opslaan")



nieuwe_auto_toevoegen()

