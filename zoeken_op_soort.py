from versie_def import versie_info
import sqlite3
import print_gegevens_auto

versie_info()

db = sqlite3.connect("auto_data.db")
cursor = db.cursor()


def zoek_op_soort():

    keuze_check = int(input("Zoek soort: Maak een keuze uit: 1:Kleur 2:Bouwjaar 3:Brandstof 4: Aantal zitplaatsen 5:Landcode "))
    if keuze_check == 1:
        keuze_check = "Kleur"
    elif keuze_check == 2:
        keuze_check = "Bouwjaar"
    elif keuze_check == 3:
        keuze_check = "Brandstof"
    elif keuze_check == 4:
        keuze_check = "Aantal_zitplaatsen"
    else:
        print("Geen geldige keuze")

    zoek_op_soort_type = input("Zoek op soort: ").capitalize()

    cursor.execute(f"SELECT COUNT(*) FROM auto_voorraad WHERE {keuze_check} = ?", (zoek_op_soort_type,))


    info_auto = cursor.fetchall()
    count = info_auto[0]
    if len(info_auto) == 0:
        print(f"Geen informatie gevonden over: {zoek_op_soort_type}")

    else:
        print(f"Zoek resultaat: u heeft van {zoek_op_soort_type}: {count} stuks auto in uw wagen park.")
        cursor.execute(f"SELECT * FROM auto_voorraad WHERE {keuze_check} = ?", (zoek_op_soort_type,)) #opnieuw een sql query
        lijst2 = cursor.fetchall()
        print_gegevens_auto.print_gegevens(lijst2)








zoek_op_soort()
