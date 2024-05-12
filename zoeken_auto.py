from versie_def import versie_info
import print_gegevens_auto
import sqlite3
versie_info()

db = sqlite3.connect("auto_data.db")
cursor = db.cursor()


kenteken_zoeken = input("Kenteken: ").upper()
cursor.execute("SELECT * FROM auto_voorraad WHERE Kenteken = ?", (kenteken_zoeken,))
info_auto = cursor.fetchall()
if len(info_auto) == 0 or None:
    print(f"Kenteken: {kenteken_zoeken} niet gevonden!")
else:
    print_gegevens_auto.print_gegevens(info_auto)




