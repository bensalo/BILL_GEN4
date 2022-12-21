from tinydb import TinyDB, Query
import pdf_gen as pg
import os
# Notice this first Version is only to work fast because i need to create a lot of Bills. GUI etc. will be added later.

# this script is capable of creating and managing groups.
# It has a database (TinyDB) where all customers of a class are stored.

# INPUT #
# - 

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

def new_class_member(rn, name, adresse, ort, email = "empty"):
    id = yogaclass.__len__()
    yogaclass.insert({'K_id' : str(id),'rn': rn,'name': name, 'adresse': adresse, 'ort': ort, 'email': email})

def show_all_members():
    pass

def create_group_bill():
    Group_Path = os.getenv('SAVE_PATH_GROUP', "")
    pg1 = pg.mypdf1(path=Group_Path)
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

# function to create new class member from console input

def create_new_class_member():
    rn = input("Rechnungsnummer: ")
    name = input("Name: ")
    adresse = input("Adresse: ")
    ort = input("Ort: ")
    email = input("Email: ")
    new_class_member(rn, name, adresse, ort, email)

#test
#create_new_class_member()
#create_new_class_member()
create_group_bill()
