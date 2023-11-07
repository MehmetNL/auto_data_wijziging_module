def totaal_resultaat(self,):
    cursor.execute("SELECT COUNT(*) FROM auto_voorraad WHERE Bouwjaar = ?", (self,))
    result = cursor.fetchone()
    count = result[0]
    print("Zoek resultaat: u heeft van bouwjaar: {} {} stuks auto in uw wagen park".format(self, count))
    return count


cursor.execute("SELECT COUNT(*) FROM auto_voorraad WHERE Kenteken = ?", (kenteken_zoeken,))
result = cursor.fetchone()
count = result[0]
print(f"Zoek resultaat: u heeft van : {kenteken_zoeken} {count} stuks auto in uw wagen park")