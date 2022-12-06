from reportlab.pdfgen import canvas 

class mypdf:
    def __init__(self, filename="test.pdf"):
        self.filename = filename
        self.vendor_name = "Max Mustermann"
        self.vendor_job = "Jurist"
        self.vendor_address = "lautstraße 2"
        self.vendor_city = "Entenhausen"
        self.vendor_city_key = "12345"
        self.vendor_phone = "0212/531762"
        self.vendor_iban = "DE12345678901234567890"
        self.get_vendor_info()
        self.pdf = canvas.Canvas(self.filename)
    
    def get_vendor_info(self):
        import os
        from dotenv import load_dotenv

        load_dotenv()
        self.vendor_name = os.getenv("VENDOR_NAME")
        self.vendor_job = os.getenv("VENDOR_JOB")
        self.vendor_address = os.getenv("VENDOR_ADDRESS")
        self.vendor_city = os.getenv("VENDOR_CITY")
        self.vendor_city_key = os.getenv("VENDOR_CITY_KEY")
        self.vendor_phone = os.getenv("VENDOR_PHONE")
        self.vendor_iban = os.getenv("VENDOR_IBAN")

        
 
 
    def merge_modules_data_and_save(self,data):
        
        rn, Name, Adresse, Ort, Betreff, Datum, Betrag, Briefinhalt = data

        self.pdf.setTitle("Rechnung")
        mypdf.create_header(self, self.pdf, Datum)
        mypdf.create_kundendaten(self.pdf, Name, Adresse, Ort)
        mypdf.create_betreff(self.pdf, Betreff, rn)	
        mypdf.create_briefinhalt(self, self.pdf, Briefinhalt, Betrag)
        self.pdf.save() 

    def create_header(self, pdf, datum):
        pdf.drawString(420, 800, self.vendor_city + ", den " + datum)
        text = pdf.beginText(30, 800)
        text.setFont("Courier", 12)
        text.textLine(self.vendor_name)
        text.textLine(self.vendor_job)
        text.textLine(self.vendor_address)
        text.textLine(self.vendor_city_key + " " + self.vendor_city)
        text.textLine(self.vendor_phone)
        pdf.drawText(text)
        pdf.line(30, 730, 550, 730)


    def create_kundendaten(pdf, name, adresse, ort):
            text = pdf.beginText(30, 710)
            text.setFont("Courier", 12)
            text.textLine(name)
            text.textLine(adresse)
            text.textLine(ort)
            pdf.drawText(text)   

    def create_betreff(pdf, betreff, rn_nr):
        pdf.setFont("Courier-Bold", 18)
        title = "Rechnung " + betreff
        title_rn = "Rechnungsnummer: " + rn_nr
        pdf.drawString(30, 600, title)
        pdf.drawString(30, 580, title_rn)

    def create_briefinhalt(self, pdf, briefinhalt, Betrag):
        text = pdf.beginText(30, 450)
        text.setFont("Courier", 12)
        text.textLine("Sehr geehrte Damen und Herren,")
        text.textLine("")
        text.textLine(briefinhalt + " bitte ich Sie " + Betrag + " Euro") 
        text.textLine("auf mein Konto zu überweisen.")
        text.textLine("")
        text.textLine("IBAN: " + self.vendor_iban)
        text.textLine("Mit freundlichen Grüßen")
        text.textLine("")
        text.textLine(self.vendor_name)
        pdf.drawText(text)
        

## executíon example
# test data
# data = ("123456", "Sabine Salomon", "Binsenweg 2", "52076 Aachen", "für Yogastunden im November 2022", "01.11.2022", "100,00", "für die Yogastunden im November 2022")
# testbill = mypdf()    
# testbill.merge_modules_data_and_save(data)
