import sqlite3
from versie_def import versie_info
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
    Kenteken = input("Kenteken: ").upper()
    count = controleer_kenteken(Kenteken)
    if count > 0:
        print("Kenteken {} bestaat al in uw auto voorraad".format(Kenteken))
        return
    Merk = input("Merk: ").capitalize()
    Model = input("Model: ").capitalize()
    Kleur = input("Kleur: ").capitalize()
    Bouwjaar = input("Bouwjaar: ")
    Nieuw_prijs = input("Nieuwprijs: ")
    Brandstof = input("Brandstof: ").capitalize()
    aantal_zitplaats = input("Aantal zitplaats: ")
    Registratie_land = input("Registratie Land: ").upper()
    data_invoegen_db(Kenteken, Merk, Model, Kleur, Bouwjaar, Nieuw_prijs, Brandstof, aantal_zitplaats,Registratie_land)
    print("Voertuig {} is toegevoegd".format(Kenteken))
    sluit_verbinding()


nieuwe_auto_toevoegen()