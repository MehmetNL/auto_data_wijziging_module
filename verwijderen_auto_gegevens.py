import sqlite3
from versie_def import versie_info
versie_info()

db = sqlite3.connect("auto_data.db")
cursor = db.cursor()


def sluit_verbinding():
    db.commit()
    db.close()


zoek_auto_verwijderen = input("Welke kenteken wilt u verwijderen: ").upper()
cursor.execute("SELECT * FROM auto_voorraad WHERE Kenteken = ?", (zoek_auto_verwijderen,))
info_verwijderen_auto = cursor.fetchall()
if len(info_verwijderen_auto) == 0:
    print(f"Ingevoerde kenteken: {zoek_auto_verwijderen}, kan niet gevonden worden in de database!")
else:
    keuze = input(f"Weet u zeker dat u kenteken: {zoek_auto_verwijderen} wilt verwijderen ? kies ja voor defentief verwijderen" ).lower()
    if keuze == "ja":
        for i in info_verwijderen_auto:
            cursor.execute("DELETE FROM auto_voorraad WHERE Kenteken = ?",(i[0],))
            print(f"Kenteken {i[0]} is verwijderd!")
            sluit_verbinding()
    else:
        print("Geen kenteken verwijderd!")