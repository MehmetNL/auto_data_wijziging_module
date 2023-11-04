import sqlite3

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


zoek_auto_verwijderen = input("Welke kenteken wilt u verwijderen: ").upper()
cursor.execute("SELECT * FROM auto_voorraad WHERE Kenteken = ?", (zoek_auto_verwijderen,))
info_verwijderen_auto = cursor.fetchall()
if len(info_verwijderen_auto) == 0:
    print(f"Ingevoerde kenteken: {zoek_auto_verwijderen}, kan niet gevonden worden in de database!")
else:
    for i in info_verwijderen_auto:
        cursor.execute("DELETE FROM auto_voorraad WHERE Kenteken = ?",(i[0],))
        print(f"Kenteken {i[0]} is verwijderd!")
        Database.sluit_verbinding()