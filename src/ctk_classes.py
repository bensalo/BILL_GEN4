import customtkinter
import database as db



class ChooseFromDB_RBFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="RadioButtonFrame", **kwargs):
        super().__init__(*args, **kwargs)

        self.header_name = header_name
        
        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, padx=10 , pady=10)

        self.radio_button_var = customtkinter.StringVar(value="")
        for kunde in db.get_whole_kunden_db():
            self.radio_button = customtkinter.CTkRadioButton(self, text=kunde["name"], variable=self.radio_button_var, value=int(kunde["K_id"]))
            self.radio_button.grid(row=int(kunde["K_id"])+1, column=0, padx=10 , pady=10)

    def get_selected_id(self):
        return self.radio_button_var.get()

    def set_value(self, selected_id):
        self.radio_button_var.set(selected_id)



class InputFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="InputFrame", **kwargs):
        super().__init__(*args, **kwargs)

        self.header_name = header_name
        self.rechnungsnummer_input = customtkinter.StringVar(value="")
        self.rechnungsbetreff_input = customtkinter.StringVar(value="")
        self.datum = customtkinter.StringVar(value="")
        self.betrag = customtkinter.StringVar(value="")
        self.briefinhalt = customtkinter.StringVar(value="")

        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, padx=10 , pady=10)

        self.rn_label = customtkinter.CTkLabel(self, text="Rechnungsnummer:")
        self.rn_label.grid(row=1, column=0, padx=10 , pady=10)

        self.rn_in = customtkinter.CTkEntry(self, textvariable=self.rechnungsnummer_input)
        self.rn_in.grid(row=1, column=1, padx=10 , pady=10)

        self.rb_label = customtkinter.CTkLabel(self, text="Rechnungsbetreff:")
        self.rb_label.grid(row=2, column=0, padx=10 , pady=10)

        self.rb_in = customtkinter.CTkEntry(self, textvariable=self.rechnungsbetreff_input)
        self.rb_in.grid(row=2, column=1, padx=10 , pady=10)

        self.datum_label = customtkinter.CTkLabel(self, text="Datum:")
        self.datum_label.grid(row=3, column=0, padx=10 , pady=10)

        self.datum_in = customtkinter.CTkEntry(self, textvariable=self.datum)
        self.datum_in.grid(row=3, column=1, padx=10 , pady=10)

        self.betrag_label = customtkinter.CTkLabel(self, text="Betrag:")
        self.betrag_label.grid(row=4, column=0, padx=10 , pady=10)

        self.betrag_in = customtkinter.CTkEntry(self, textvariable=self.betrag)
        self.betrag_in.grid(row=4, column=1, padx=10 , pady=10)

        self.briefinhalt_label = customtkinter.CTkLabel(self, text="Briefinhalt:")
        self.briefinhalt_label.grid(row=5, column=0, padx=10 , pady=10)

        self.briefinhalt_in = customtkinter.CTkEntry(self, textvariable=self.briefinhalt)
        self.briefinhalt_in.grid(row=5, column=1, padx=10 , pady=10)
        
    def get_values(self):
        return (self.rechnungsnummer_input.get(), self.rechnungsbetreff_input.get(), self.datum.get(), self.betrag.get(), self.briefinhalt.get())

class Input_User_Frame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="InputFrame", **kwargs):
        super().__init__(*args, **kwargs)

        self.header_name = header_name
        self.name = customtkinter.StringVar(value="")
        self.adresse = customtkinter.StringVar(value="")
        self.plz = customtkinter.StringVar(value="")
        self.email = customtkinter.StringVar(value="")
        self.rechnungsnummer_temp = customtkinter.StringVar(value="")

        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, padx=10 , pady=10)

        self.name_label = customtkinter.CTkLabel(self, text="Name:")
        self.name_label.grid(row=1, column=0, padx=10 , pady=10)

        self.name_in = customtkinter.CTkEntry(self, textvariable=self.name)
        self.name_in.grid(row=1, column=1, padx=10 , pady=10)

        self.adresse_label = customtkinter.CTkLabel(self, text="Adresse:")
        self.adresse_label.grid(row=2, column=0, padx=10 , pady=10)

        self.adresse_in = customtkinter.CTkEntry(self, textvariable=self.adresse)
        self.adresse_in.grid(row=2, column=1, padx=10 , pady=10)

        self.plz_label = customtkinter.CTkLabel(self, text="PLZ:")
        self.plz_label.grid(row=3, column=0, padx=10 , pady=10)

        self.plz_in = customtkinter.CTkEntry(self, textvariable=self.plz)
        self.plz_in.grid(row=3, column=1, padx=10 , pady=10)

        self.email_label = customtkinter.CTkLabel(self, text="Email:")
        self.email_label.grid(row=4, column=0, padx=10 , pady=10)

        self.email_in = customtkinter.CTkEntry(self, textvariable=self.email)
        self.email_in.grid(row=4, column=1, padx=10 , pady=10)

        self.rechnungsnummer_label = customtkinter.CTkLabel(self, text="Rechnungsnummer:")
        self.rechnungsnummer_label.grid(row=5, column=0, padx=10 , pady=10)

        self.rechnungsnummer_temp = customtkinter.CTkEntry(self, textvariable=self.rechnungsnummer_temp)
        self.rechnungsnummer_temp.grid(row=5, column=1, padx=10 , pady=10)

    def get_values(self):
        return (self.name.get(), self.adresse.get(), self.plz.get(), self.email.get(), self.rechnungsnummer_temp.get())
 
class show_values_Frame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Values Frame", values= [], **kwargs):
        super().__init__(*args, **kwargs)

        self.header_name = header_name 
        self.values = values 

        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, padx=10 , pady=10)
        
        row = 1
        for value in self.values:
            self.value_name = customtkinter.CTkLabel(self, text=value[0])
            self.value_name.grid(row=row, column=0, padx=10 , pady=10)
            self.value = customtkinter.CTkLabel(self, text=value[1])
            self.value.grid(row=row, column=1, padx=10 , pady=10)
            row += 1
