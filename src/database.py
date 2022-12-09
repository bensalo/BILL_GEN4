from tinydb import TinyDB, Query, where, operations

kunden_db = TinyDB('kunden.json')
Rechnungen_DB = TinyDB('rechnungen.json')

def new_kunde(name, adresse, ort, rechnungsnummer_temp, email = "empty"):
    id = kunden_db.__len__()
    kunden_db.insert({'K_id' : str(id), 'name': name, 'adresse': adresse, 'ort': ort, 'email': email, 'rechnungsnummer_temp': rechnungsnummer_temp, 'letzte_rechnungsnummer': "leer"})

def generate_random_kunden():
    # insert 10 random kunden
    for i in range(10):
        kunden_db.insert({'K_id' : str(i), 'name': 'user'+str(i), 'adresse': "leer", 'ort': "leer", 'email': "leer", 'rechnungsnummer_temp': str(i), 'letzte_rechnungsnummer': str(i)})

def get_kunde_by_id(id):
    kunde = Query()
    return kunden_db.search(kunde.K_id == str(id))
    
def get_whole_kunden_db():
    return kunden_db

def update_kunde(kunden_id,letzte_rechnungsnummer):
    kunde = Query()
    kunden_db.update({'letzte_rechnungsnummer': letzte_rechnungsnummer}, kunde.K_id == str(kunden_id))

def new_rechnung(kunden_id, name, betreff, datum, betrag, rechnungsnummer):
    # function to store important data from a bill in the rechnungen.json database
    Rechnungen_DB.insert({'K_id' : str(kunden_id), 'name': name, 'betreff': betreff, 'datum': datum, 'betrag': betrag, 'rechnungsnummer': rechnungsnummer})
    print("Rechnung wurde gespeichert")

def get_rechnungen():
    return Rechnungen_DB

#generate_random_kunden()