# Notice this first Version is only to work fast because i need to create a lot of Bills. GUI etc. will be added later.

# this script is capable of creating and managing groups.
# It has a database (TinyDB) where all customers of a class are stored.

# INPUT #
# - 
from tinydb import TinyDB, Query
import pdf_gen as pg
import os

# Variables 
rn = "user"
name = "user"	
adresse = "user"
ort = "user"
betreff = "Yogastunden 2022"
datum = "22.12.2022"
betrag = "user"
briefinhalt = "Yogastunden 2022" 

data = rn, name, adresse, ort, betreff, datum, betrag, briefinhalt
# use this data to create a pdf, change some values and create another pdf for the next user

yogaclass = TinyDB('yogaclass1.json')

def new_class_member(name, adresse, ort, email = "empty"):
    id = yogaclass.__len__()
    yogaclass.insert({'K_id' : str(id), 'name': name, 'adresse': adresse, 'ort': ort, 'email': email})

def show_all_members():
    pass

def create_group_bill():
    pg1 = pg.mypdf1()
    for member in yogaclass:
        print("Creating Bill for: ", member['name'])
        # get int input from console
        betrag = input("Rechnungsumme: ")
        pg1.merge_modules_data_and_save(change_data_to_new_user(member, betrag))

def change_data_to_new_user(member, betrag):
    rn = member['rn']
    name = member['name']
    adresse = member['adresse']
    ort = member['ort']
    return(rn, name, adresse, ort, betreff, datum, betrag, briefinhalt)

