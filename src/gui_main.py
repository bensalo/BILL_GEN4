import database as db
import customtkinter
import ctk_classes as cc
import pdf_gen as pg

### NEEDED DATA FOR BILL GENERATION ###
Selected_User_ID = None
Selected_User_rn_temp = ""
Selected_User_rn_last = ""
Selected_User_Name = ""
Selected_User_Adresse = ""
Selected_User_Ort = ""
Selected_User_rn = ""
Selected_User_Betreff = ""
Selected_User_Datum = ""
Selected_User_Betrag = ""
Selected_User_Briefinhalt = ""

def main():
    app = App()
    app.mainloop()


class row1(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.radio_button_frame_1 = cc.ChooseFromDB_RBFrame(self, header_name="Kunden auswählen")
        self.radio_button_frame_1.grid(row=0, column=0, padx=20, pady=20)

        self.button = customtkinter.CTkButton(self, text="Auswählen", command=self.get_kunden_id)
        self.button.grid(row=1, column=0, padx=20, pady=20)

        Rechnungsnummer = [["Rechnungsnummer_Base:",Selected_User_rn_temp],["Letzte_Rechnungsnummer",Selected_User_rn_last],["ID:",Selected_User_ID]]     
        self.rechnungsnummer_frame = cc.show_values_Frame(self, header_name="Rechnungsnummer", values = Rechnungsnummer)
        self.rechnungsnummer_frame.grid(row=2, column=0, padx=20, pady=20)
        KundenDaten = [["Name:",""],["Adresse:",""],["Ort:",""],["E-Mail:",""]]
        self.kundendaten_frame = cc.show_values_Frame(self, header_name="Kundendaten", values = KundenDaten)
        self.kundendaten_frame.grid(row=0, column=1, padx=20, pady=20)


    def get_kunden_id(self):
        kunden_id = self.radio_button_frame_1.get_selected_id()
        global Selected_User_ID
        global Selected_User_rn_temp
        global Selected_User_rn_last
        global Selected_User_Name
        global Selected_User_Adresse
        global Selected_User_Ort
        Selected_User_ID = kunden_id
        kunde = db.get_kunde_by_id(kunden_id)[0]
        Selected_User_rn_temp = kunde["rechnungsnummer_temp"]
        Selected_User_rn_last = kunde["letzte_rechnungsnummer"]
        Selected_User_Name = kunde["name"]
        Selected_User_Adresse = kunde["adresse"]
        Selected_User_Ort = kunde["ort"]
        Rechnungsnummer = [["Rechnungsnummer_Base:",kunde["rechnungsnummer_temp"]],["Letzte_Rechnungsnummer:",kunde["letzte_rechnungsnummer"]],["ID:",int(kunden_id)]]
        self.rechnungsnummer_frame = cc.show_values_Frame(self, header_name="Rechnungsnummer", values = Rechnungsnummer)
        self.rechnungsnummer_frame.grid(row=2, column=0, padx=20, pady=20)
        KundenDaten = [["Name:",kunde["name"]],["Adresse:",kunde["adresse"]],["Ort:",kunde["ort"]],["E-Mail:",kunde["email"]]]
        self.kundendaten_frame = cc.show_values_Frame(self, header_name="Kundendaten", values = KundenDaten)
        self.kundendaten_frame.grid(row=0, column=1, padx=20, pady=20)



class row2(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        self.input_frame_1 = cc.InputFrame(self, header_name="Rechnungsdaten")
        self.input_frame_1.grid(row=1, column=0, padx=20, pady=20)

        self.button = customtkinter.CTkButton(self, text="Auswählen", command=self.save_input_values)
        self.button.grid(row=2, column=0, padx=20, pady=20)

    def save_input_values(self):
        global Selected_User_rn
        global Selected_User_Betreff
        global Selected_User_Datum
        global Selected_User_Betrag
        global Selected_User_Briefinhalt
        Selected_User_rn, Selected_User_Betreff, Selected_User_Datum, Selected_User_Betrag, Selected_User_Briefinhalt = self.input_frame_1.get_values()




class row3(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.button = customtkinter.CTkButton(self, text="Vorschau", command=self.preview_bill)
        self.button.grid(row=0, column=0, padx=20, pady=20)

        self.button = customtkinter.CTkButton(self, text="Rechnung Erstellen", command=self.generate_bill)
        self.button.grid(row=2, column=0, padx=20, pady=20)
        

    def preview_bill(self):
        #get all global variables
        global Selected_User_ID
        global Selected_User_rn
        global Selected_User_Name
        global Selected_User_Adresse
        global Selected_User_Ort
        global Selected_User_Betreff
        global Selected_User_Datum
        global Selected_User_Betrag
        global Selected_User_Briefinhalt
        print("--------------------")
        print("Selected_User_ID: ",Selected_User_ID)
        print("Selected_User_rn: ",Selected_User_rn)
        print("Selected_User_Name: ",Selected_User_Name)
        print("Selected_User_Adresse: ",Selected_User_Adresse)
        print("Selected_User_Ort: ",Selected_User_Ort)
        print("Selected_User_Betreff: ",Selected_User_Betreff)
        print("Selected_User_Datum: ",Selected_User_Datum)
        print("Selected_User_Betrag: ",Selected_User_Betrag)
        print("Selected_User_Briefinhalt: ",Selected_User_Briefinhalt)
        print("--------------------")




    def generate_bill(self):
        #load template
        #edit word/pdf document
        #save document
        
        #get all global variables
        global Selected_User_ID
        global Selected_User_rn
        global Selected_User_Name
        global Selected_User_Adresse
        global Selected_User_Ort
        global Selected_User_Betreff
        global Selected_User_Datum
        global Selected_User_Betrag
        global Selected_User_Briefinhalt
        
        #update database
        bill = pg.mypdf() #filename in here
        data = (Selected_User_rn, Selected_User_Name, Selected_User_Adresse, Selected_User_Ort, Selected_User_Betreff, Selected_User_Datum, Selected_User_Betrag, Selected_User_Briefinhalt)
        bill.merge_modules_data_and_save(data)
        db.new_rechnung(Selected_User_ID, Selected_User_Name, Selected_User_Betreff, Selected_User_Datum, Selected_User_Betrag, Selected_User_rn)
        db.update_kunde(Selected_User_ID, Selected_User_rn)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x850")
        self.title("BILL_GEN_4")

        
        self.row1 = row1(master = self)
        self.row1.grid(row=0, column=0, padx=20, pady=20)

        self.row2 = row2(master = self)
        self.row2.grid(row=0, column=1, padx=20, pady=20)

        self.row3 = row3(master = self)
        self.row3.grid(row=0, column=2, rowspan=2, padx=20, pady=20)



if __name__ == "__main__":
    main()
    