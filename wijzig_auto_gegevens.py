import sqlite3
from versie_def import versie_info
versie_info()
db = sqlite3.connect("auto_data.db")
cursor = db.cursor()


class Database:
    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name)
        self.cursor = self.db.cursor()

    @staticmethod
    def sluit_verbinding():
        db.commit()
        db.close()


class wijzig_auto_gegevens(Database):
    def controleer_kenteken(self):
        cursor.execute("SELECT COUNT(*) FROM auto_voorraad WHERE Kenteken = ?", (self,))
        result = cursor.fetchone()
        count = result[0] #[0] moet tupel omgezet worden in list, zodat vergelijk gemaakt kan worden
        if count > 0:
            exit(f"Kenteken {self} bestaat al in uw auto voorraad, u kunt dit niet wijzigen!")


    kenteken = input("Vul hier uw kenteken die u wilt wijzigen: ").upper()
    cursor.execute("SELECT * FROM auto_voorraad WHERE Kenteken = ?", (kenteken,))
    info_auto = cursor.fetchall()
    if len(info_auto) == 0:
        print("Kenteken niet gevonden")
    else:
        for i in info_auto:
            print(f"Wijziging\n1: Kenteken {i[0]}\n2: Merk {i[1]}\n3: Model {i[2]}\n4: Kleur {i[3]}\n5: Bouwjaar {i[4]}\n6: Catalogus Waarde {i[5]}\n7: Brandstof {i[6]}\n8: Aantal Zitplaatsen {i[7]}\n9: Land Code {i[8]}")

        keuze = int(input("Maak een keuze wijzigen: "))
        if keuze == 1:
            nieuwe_kenteken = input(f"Uw oude kenteken is {i[0]} vul uw nieuwe kenteken: ").upper()
            controleer_kenteken(nieuwe_kenteken)
            cursor.execute("UPDATE auto_voorraad SET Kenteken = ? WHERE Kenteken = ?",(nieuwe_kenteken,kenteken))
            print(f"Kenteken is gewijzigd! nieuwe kenteken is {nieuwe_kenteken}")
            Database.sluit_verbinding()
        elif keuze == 2:
            nieuwe_merk = input(f"Huidge merk: {i[1]}, nieuwe merk:   ").capitalize()
            cursor.execute("UPDATE auto_voorraad SET Merk = ? WHERE Merk = ?",(nieuwe_merk,i[1]))
            print(f"Uw merk is gewijzigd, nieuwe merk is: {nieuwe_merk} ")
            Database.sluit_verbinding()
        elif keuze == 3:
            nieuwe_model = input(f"Huidge model: {i[2]}, nieuwe model : ").capitalize()
            cursor.execute("UPDATE auto_voorraad SET Model = ? WHERE Model = ?",(nieuwe_model,i[2]))
            print(f"Uw model is gewijzigd, nieuwe model is: {nieuwe_model}")
            Database.sluit_verbinding()
        elif keuze == 4:
            nieuwe_kleur = input(f"Huidge kleur: {i[3]}, nieuwe kleur: ").capitalize()
            cursor.execute("UPDATE auto_voorraad SET Kleur = ? WHERE Kleur = ?",(nieuwe_kleur,i[3]))
            print(f"Uw kleur is gewijzigd, nieuwe kleur is: {nieuwe_kleur}")
            Database.sluit_verbinding()
        elif keuze == 5:
            nieuwe_bouwjaar = input(f"Huidige bouwjaar: {i[4]}, nieuwe bouwjaar: ")
            cursor.execute("UPDATE auto_voorraad SET Bouwjaar = ? WHERE Bouwjaar = ?",(nieuwe_bouwjaar,i[4]))
            print(f"Uw bouwjaar is gewijzigd, nieuwe bouwjaar is: {nieuwe_bouwjaar}")
            Database.sluit_verbinding()
        elif keuze == 6:
            nieuwe_cat_waarden = input(f"Huidige catalogus waarde: {i[5]}, nieuwe catalagus waarden:  ")
            cursor.execute("UPDATE auto_voorraad SET Nieuw_prijs = ? WHERE Nieuw_prijs = ?",(nieuwe_cat_waarden,i[5]))
            print(f"Uw catalogus prijs is gewijzigd, nieuwe prijs is: {nieuwe_cat_waarden}")
            Database.sluit_verbinding()
        elif keuze == 7:
            nieuwe_brandstof = input(f"Huidige brandstof is: {i[6]}, nieuwe brandstof: ").capitalize()
            list_brandstof = ["Benzine","Diesel","LPG","Elektriche","Cng"]
            if nieuwe_brandstof in list_brandstof:
               cursor.execute("UPDATE auto_voorraad SET Brandstof = ? WHERE Brandstof = ? ", (nieuwe_brandstof, i[6]))
               print(f"Uw brandstof is gewijzigd, nieuwe brandstof is: {nieuwe_brandstof}")
               Database.sluit_verbinding()
            else:
                exit("Geen geldige brandstog ingevoerd!")
        elif keuze == 8:
            nieuwe_aantal_zitplaatsen = input(f"Huidige zitplaatsen: {i[7]}, nieuwe zitplaatsen: ")
            cursor.execute("UPDATE auto_voorraad SET aantal_zitplaatsen = ? WHERE aantal_zitplaatsen = ?",(nieuwe_aantal_zitplaatsen,i[7]))
            print(f"Uw aantal zitplaatsen is gewijzigd, nieuwe zitplaatsen is: {nieuwe_aantal_zitplaatsen}")
            Database.sluit_verbinding()
        elif keuze == 9:
            nieuwe_landcode = input(f"Huidige landcode: {i[8]}, nieuwe landcode is: ").upper()
            cursor.execute("UPDATE auto_voorraad SET Registratie_land = ? WHERE Registratie_land = ?",(nieuwe_landcode,i[8]))
            print(f"Uw landcode is gewijzigd, nieuwe landcode is: {nieuwe_landcode}")
            Database.sluit_verbinding()
        else:
            print("Ongeldige keuze!")
