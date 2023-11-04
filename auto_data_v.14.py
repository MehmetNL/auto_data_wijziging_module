# v1.4 kenteken controlle ingevoerd, bij toevpegen nieuwe auto
# ORM - Object Relational Mapper = Framework om vanuit code verbinding te leggen met DB en DB taken kan uitvoeren
# v1.5 Toevoeging resultaat in filter functie
# v1.6 Bijd bij deze versie alles is aangepast naar f strinf, ipv, format
import sqlite3
import time


versie = "v1.5"

########################### hierboven definitie ########
print(100 * "-")
print(50 * " ", f"Auto voorraadbeheer versie {versie}")
print(100 * "-")

db = sqlite3.connect("auto_data.db")
cursor = db.cursor()


class AutoVoorraadBeheer:
    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name)
        self.cursor = self.db.cursor()

    def data_invoegen_db(self, Kenteken, Merk, Model, Kleur, Bouwjaar, Nieuw_prijs, Brandstof, aantal_zitplaats,
                         Regisratie_land):
        self.cursor.execute("INSERT INTO auto_voorraad VALUES (?,?,?,?,?,?,?,?,?)", (
            Kenteken, Merk, Model, Kleur, Bouwjaar, Nieuw_prijs, Brandstof, aantal_zitplaats, Regisratie_land))
        self.db.commit()

    def controleer_kenteken(self, Kenteken):
        self.cursor.execute("SELECT COUNT(*) FROM auto_voorraad WHERE Kenteken = ?", (Kenteken,))
        result = self.cursor.fetchone()
        count = result[0] #[0] moet tupel omgezet worden in list, zodat vergelijk gemaakt kan worden
        return count

    def sluit_verbinding(self):
        self.db.close()

    def nieuwe_auto_toevoegen(self):
        Kenteken = input("Kenteken: ").upper()
        count = self.controleer_kenteken(Kenteken)
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
        self.data_invoegen_db(Kenteken, Merk, Model, Kleur, Bouwjaar, Nieuw_prijs, Brandstof, aantal_zitplaats,Registratie_land)
        print("Voertuig {} is toegevoegd".format(Kenteken))
        time.sleep(3)
        self.sluit_verbinding()


class zoek_op_kenteken(AutoVoorraadBeheer):

    def zoek_auto(self, Kenteken):
        cursor.execute("SELECT * FROM auto_voorraad WHERE Kenteken = ?", (Kenteken,))
        info2 = cursor.fetchall()


        if len(info2) == 0:
            print("Kenteken niet gevonden...")

        else:
            print("{0:15s} {1:20s} {2:20s} {3:20s} {4:20} {5:20s} {6:20s} {7:20s} {8:20s}".format("Kenteken", "Merk",
                                                                                                  "Model",
                                                                                                  "Kleur", "Bouwjaar",
                                                                                                  "Nieuw_prijs",
                                                                                                  "Brandstof",
                                                                                                  "aantal_zitplaats",
                                                                                                  "Registratie_land"))
            print("{0:15s} {1:20s} {2:20s} {3:20s} {4:20} {5:20s} {6:20s} {7:20s} {8:20s}".format("-" * 15, "-" * 20,
                                                                                                  "-" * 20,
                                                                                                  "-" * 20, "-" * 20,
                                                                                                  "-" * 20,
                                                                                                  "-" * 20, "-" * 20,
                                                                                                  "-" * 20))

            for i in info2:
                print("{0:15s} {1:20s} {2:20s} {3:20s} {4:20s} {5:20s} {6:20s} {7:20s} {8:20s}".format(i[0], i[1], i[2],
                                                                                                       i[3], i[4],
                                                                                                       i[5], i[6], i[7],
                                                                                                       i[8]))


class zoek_op_type_brandstof(AutoVoorraadBeheer):

    @staticmethod
    def totaal_aantal_voertuigen(Brandstof_aantal):
        cursor.execute("SELECT COUNT(*) FROM auto_voorraad WHERE Brandstof = ?", (Brandstof_aantal,))
        result = cursor.fetchone()
        count = result[0]
        print(f"Zoek resultaat: u heeft van type brandstof: {brandstof} {count} stuks auto in uw wagen park")
        return count

    @staticmethod
    def zoek_brandstof(Brandstof):
        cursor.execute("SELECT * FROM auto_voorraad WHERE Brandstof = ?", (Brandstof,))
        info2 = cursor.fetchall()

        if len(info2) == 0:
            print("Kenteken niet gevonden...")

        else:
            print("{0:15s} {1:25s} {2:25s} {3:25s} {4:25} {5:25s} {6:25s} {7:25s} {8:26s}".format("Kenteken", "Merk",
                                                                                                "Model",
                                                                                                "Kleur", "Bouwjaar",
                                                                                                "Nieuw_prijs",
                                                                                                "Brandstof",
                                                                                                "aantal_zitplaats",
                                                                                                "Registratie_land"))

            print("{0:15s} {1:25s} {2:25s} {3:25s} {4:25} {5:25s} {6:25s} {7:25s} {8:26s}".format("-" * 15, "-" * 25,
                                                                                                  "-" * 25,
                                                                                                  "-" * 25, "-" * 25,
                                                                                                  "-" * 25,
                                                                                                  "-" * 25, "-" * 25,
                                                                                                  "-" * 25))
            for i in info2:
                print("{0:15s} {1:25s} {2:25s} {3:25s} {4:25s} {5:25s} {6:25s} {7:25s} {8:26s}".format(i[0], i[1], i[2],
                                                                                                       i[3],
                                                                                                       i[4],
                                                                                                       i[5], i[6], i[7],
                                                                                                       i[8]))


class zoek_op_aantal_zitplaatsen(AutoVoorraadBeheer):
    @staticmethod
    def totaal_aantal_zitplaatsen(Zitplaatsen_aantal):
        cursor.execute("SELECT COUNT(*) FROM auto_voorraad WHERE Aantal_zitplaatsen = ?", (Zitplaatsen_aantal,))
        result = cursor.fetchone()
        count = result[0]
        print(f"Zoek resultaat: u heeft {count} auto met {zoek_op_aantal_zitplaatsen} zitplaatsen")
        return count

    @staticmethod
    def zoek_aantal_zitplaatsen(aantal_zitplaatsen):
        cursor.execute("SELECT * FROM auto_voorraad WHERE Aantal_zitplaatsen = ?", (aantal_zitplaatsen,))
        info2 = cursor.fetchall()

        if len(info2) == 0:
            print("Geen auto gevonden met {} zitplaatsen".format(aantal_zitplaatsen))

        else:
            print("{0:15s} {1:25s} {2:25s} {3:25s} {4:25} {5:25s} {6:25s} {7:25s} {8:26s}".format("Kenteken", "Merk",
                                                                                                "Model",
                                                                                                "Kleur", "Bouwjaar",
                                                                                                "Nieuw_prijs",
                                                                                                "Brandstof",
                                                                                                "aantal_zitplaats",
                                                                                                "Registratie_land"))

            print("{0:15s} {1:25s} {2:25s} {3:25s} {4:25} {5:25s} {6:25s} {7:25s} {8:26s}".format("-" * 15, "-" * 25,
                                                                                                  "-" * 25,
                                                                                                  "-" * 25, "-" * 25,
                                                                                                  "-" * 25,
                                                                                                  "-" * 25, "-" * 25,
                                                                                                  "-" * 25))

            for i in info2:
                print("{0:15s} {1:25s} {2:25s} {3:25s} {4:25s} {5:25s} {6:25s} {7:25s} {8:26s}".format(i[0], i[1], i[2],
                                                                                                       i[3],
                                                                                                       i[4],
                                                                                                       i[5], i[6], i[7],
                                                                                                       i[8]))


class zoek_auto_op_land(AutoVoorraadBeheer):
    @staticmethod
    def zoek_op_land(zoek_land):
        cursor.execute("SELECT * FROM auto_voorraad WHERE Registratie_land = ?", (zoek_land,))
        info2 = cursor.fetchall()

        if len(info2) == 0:
            print("Geen auto gevonden met land code: {} ".format(zoek_land))

        else:
            print( "{0:15s} {1:25s} {2:25s} {3:25s} {4:25} {5:25s} {6:25s} {7:25s} {8:26s}".format("Kenteken", "Merk",
                                                                                                "Model",
                                                                                                "Kleur", "Bouwjaar",
                                                                                                "Nieuw_prijs",
                                                                                                "Brandstof",
                                                                                                "aantal_zitplaats",
                                                                                                "Registratie_land"))
            print("{0:15s} {1:25s} {2:25s} {3:25s} {4:25} {5:25s} {6:25s} {7:25s} {8:26s}".format("-" * 15, "-" * 25,
                                                                                                  "-" * 25,
                                                                                                  "-" * 25, "-" * 25,
                                                                                                  "-" * 25,
                                                                                                  "-" * 25, "-" * 25,
                                                                                                  "-" * 25))
            for i in info2:
                print("{0:15s} {1:25s} {2:25s} {3:25s} {4:25s} {5:25s} {6:25s} {7:25s} {8:26s}".format(i[0], i[1], i[2],
                                                                                                       i[3],
                                                                                                       i[4],
                                                                                                       i[5], i[6], i[7],
                                                                                                       i[8]))

    @staticmethod
    def totaal_aantal_voertuigen_land(zoek_land):
        cursor.execute("SELECT COUNT(*) FROM auto_voorraad WHERE Registratie_land = ?", (zoek_land,))
        result = cursor.fetchone()
        count = result[0]
        print("Zoek resultaat: u heeft van landcode: {} {} stuks auto in uw wagen park".format(zoek_land, count))
        return count


class zoek_auto_op_bouwjaar(AutoVoorraadBeheer):

    @staticmethod
    def zoek_op_bouwjaar(zoek_bouwjaar):
        cursor.execute("SELECT * FROM auto_voorraad WHERE Bouwjaar = ?", (zoek_bouwjaar,))
        info2 = cursor.fetchall()

        if len(info2) == 0:
            print("Geen auto gevonden met {} bouwjaar".format(zoek_bouwjaar))

        else:
            print(
                "{0:15s} {1:25s} {2:25s} {3:25s} {4:25} {5:25s} {6:25s} {7:25s} {8:26s}".format("Kenteken", "Merk",
                                                                                                "Model",
                                                                                                "Kleur", "Bouwjaar",
                                                                                                "Nieuw_prijs",
                                                                                                "Brandstof",
                                                                                                "aantal_zitplaats",
                                                                                                "Registratie_land"))
            print("{0:15s} {1:25s} {2:25s} {3:25s} {4:25} {5:25s} {6:25s} {7:25s} {8:26s}".format("-" * 15, "-" * 25,
                                                                                                  "-" * 25,
                                                                                                  "-" * 25, "-" * 25,
                                                                                                  "-" * 25,
                                                                                                  "-" * 25, "-" * 25,
                                                                                                  "-" * 25))
            for i in info2:
                print("{0:15s} {1:25s} {2:25s} {3:25s} {4:25s} {5:25s} {6:25s} {7:25s} {8:26s}".format(i[0], i[1], i[2],
                                                                                                       i[3],
                                                                                                       i[4],
                                                                                                       i[5], i[6], i[7],
                                                                                                       i[8]))

    @staticmethod
    def totaal_aantal_voertuigen_bouwjaar(Bouwjaar_aantal):
        cursor.execute("SELECT COUNT(*) FROM auto_voorraad WHERE Bouwjaar = ?", (Bouwjaar_aantal,))
        result = cursor.fetchone()
        count = result[0]
        print("Zoek resultaat: u heeft van bouwjaar: {} {} stuks auto in uw wagen park".format(bouwjaar, count))
        return count


class auto_verwijderen_kenteken(AutoVoorraadBeheer):

    @staticmethod
    def fn_verwijderen_kenteken(verw_kenteken):
        cursor.execute("Delete from auto_voorraad WHERE Kenteken = ?", (verw_kenteken,))
        db.commit()

        if not cursor.rowcount:
            print("Er is GEEN auto gevonden met kenteken {}".format(verw_kenteken))
        else:
            print("Kenteken {} is verwijderd".format(verw_kenteken))


class AutoGegevensWijzigen(AutoVoorraadBeheer):

    @staticmethod
    def controleer_kenteken_wijzigen(kenteken_wijzigen_1):
        cursor.execute("SELECT COUNT(*) FROM auto_voorraad WHERE Kenteken = ?", (kenteken_wijzigen_1,))
        result = cursor.fetchone()
        count = result[0]
        return count

    @staticmethod
    def wijzig_auto_gegevens(kenteken_opvragen, ):
        cursor.execute("SELECT * FROM auto_voorraad WHERE Kenteken = ?", (kenteken_opvragen,))
        info2 = cursor.fetchall()
        if len(info2) == 0:
            print(f"Geen auto gevonden met kenteken: {kenteken_opvragen}")
        else:
            print("{0:15s} {1:25s} {2:25s} {3:25s} {4:25s} {5:25s} {6:25s} {7:25s} {8:26s}".format("Kenteken", "Merk",
                                                                                                   "Model",
                                                                                                   "Kleur", "Bouwjaar",
                                                                                                   "Nieuw_prijs",
                                                                                                   "Brandstof",
                                                                                                   "Aantal_zitplaatsen",
                                                                                                   "Registratie_land"))
            print("{0:15s} {1:25s} {2:25s} {3:25s} {4:25s} {5:25s} {6:25s} {7:25s} {8:26s}".format("-" * 15, "-" * 25,
                                                                                                   "-" * 25,
                                                                                                   "-" * 25, "-" * 25,
                                                                                                   "-" * 25,
                                                                                                   "-" * 25, "-" * 25,
                                                                                                   "-" * 26))
            for i in info2:
                print("{0:15s} {1:25s} {2:25s} {3:25s} {4:25s} {5:25s} {6:25s} {7:25s} {8:26s}".format(i[0], i[1], i[2],
                                                                                                       i[3],
                                                                                                       i[4],
                                                                                                       i[5], i[6], i[7],
                                                                                                       i[8]))

                        keuze_wijzigen = input(
                            "Maak een keuze:\n1: Kenteken wijzigen\n2: Merk wijzigen\n3: Model wijzigen\n4: Kleur wijzigen\n5: Bouwjaar wijzigen\n6: Nieuw prijs wijzigen\n7: Brandstof wijzigen\n8: Aantal zitplaatsen wijzigen\n9: Registarie land wijzigen ")
                        if keuze_wijzigen == 1:
                            nieuwe_kenteken = input(
                                "Huidige kenteken is {}. Voer de nieuwe kenteken in: ".format(kenteken_opvragen)).upper()
                            count = AutoGegevensWijzigen.controleer_kenteken_wijzigen(nieuwe_kenteken)
                            if count > 0:
                                print(f"Kenteken {nieuwe_kenteken} bestaat al in uw auto voorraad")
                                return
                            cursor.execute("UPDATE auto_voorraad SET Kenteken = ? WHERE Kenteken = ?",
                                           (nieuwe_kenteken, kenteken_opvragen))
                            db.commit()
                            print("Kenteken succesvol gewijzigd naar: {}".format(nieuwe_kenteken))
                            db.close()
                        elif keuze_wijzigen == 2:
                            merk_wijzigen = input("Huidige merk is {}. Voer de nieuwe merk in: ",)
                            cursor.execute("update auto_voorraad set Merk = ?",merk_wijzigen)
                            info2 = cursor.fetchone()
                            print("Uw auto merk is gewijzigd naar: {} ", merk_wijzigen, info2)



while True:
    try:
        keuze = int(input(
            "Maak een keuze:\n1: Nieuwe auto toevoegen\n2: Zoek op kenteken\n3: Zoek op brandstof\n4: Zoek op aantal zitplaatsen\n5: Zoek op bouwjaar\n6: Verwijder kenteken\n7: Wijzig auto gegevens\n8: Zoek op registatie land\n0: Afsluiten\n"))
        if keuze == 1:
            auto_voorraad = AutoVoorraadBeheer("auto_data.db")
            auto_voorraad.nieuwe_auto_toevoegen()
            print(250 * "=")
        elif keuze == 2:
            zoek_kenteken = zoek_op_kenteken("auto_data.db")
            kenteken = input("Voer het kenteken in: ").upper()
            print("Kenteken wordt gezocht...")
            zoek_kenteken.zoek_auto(kenteken)
            print(250 * "=")
        elif keuze == 3:
            zoek_brandstof = zoek_op_type_brandstof("auto_data.db")
            brandstof = input("Voer uw type brandstof in: ").capitalize()
            zoek_op_type_brandstof.zoek_brandstof(brandstof)
            zoek_brandstof.totaal_aantal_voertuigen(brandstof)  # filter
            print(250 * "=")
        elif keuze == 4:
            aantal_zitplaatsen = zoek_op_aantal_zitplaatsen("auto_data.db")
            zitplaatsen = input("Voer aantal zitplaatsen in: ")
            zoek_op_aantal_zitplaatsen.zoek_aantal_zitplaatsen(zitplaatsen)
            zoek_op_aantal_zitplaatsen.totaal_aantal_zitplaatsen(zitplaatsen)  # regel voor filter
        elif keuze == 5:
            zoek_bouwjaar = zoek_auto_op_bouwjaar("auto_data.db")
            bouwjaar = input("Vul het bouwjaar in: ")
            zoek_auto_op_bouwjaar.zoek_op_bouwjaar(bouwjaar)
            zoek_auto_op_bouwjaar.totaal_aantal_voertuigen_bouwjaar(bouwjaar)  # regel voor filter
        elif keuze == 6:
            verwijder_kenteken = auto_verwijderen_kenteken("auto_data.db")
            verwijder = input("Vul uw kenteken in die u wilt verwijderen: ").upper()
            auto_verwijderen_kenteken.fn_verwijderen_kenteken(verwijder)
        elif keuze == 7:
            wijzigen_auto_gegevens = AutoGegevensWijzigen("auto_data.db")
            wijzig_auto = input("Vul hier uw kenteken in: ").upper()
            AutoGegevensWijzigen.wijzig_auto_gegevens(wijzig_auto)
        elif keuze == 8:
            zoek_auto_land = zoek_auto_op_land("auto_data.db")
            zoek_land = input("Vul hier uw landcode: ").upper()
            zoek_auto_op_land.zoek_op_land(zoek_land)
            zoek_auto_op_land.totaal_aantal_voertuigen_land(zoek_land)
        elif keuze > 9:
            print("=====Geen Geldige invoer, maak een keuze tussen 1 en 9=====")
        elif keuze == 0:
            print("Programma wordt afgesloten... ")
            break
    except:
        print("=====Geen Geldige invoer, maak een keuze tussen 1 en 8=====")
        continue
