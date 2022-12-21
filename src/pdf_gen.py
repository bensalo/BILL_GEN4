from reportlab.pdfgen import canvas 
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
# First Template (German)

class mypdf:
    def __init__(self, path=""):
        self.vendor_name = "Max Mustermann"
        self.vendor_job = "Jurist"
        self.vendor_address = "lautstraße 2"
        self.vendor_city = "Entenhausen"
        self.vendor_city_key = "12345"
        self.vendor_phone = "0212/531762"
        self.vendor_iban = "DE12345678901234567890"
        self.filepath = path
        self.get_vendor_info()
 
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
        abs_path = self.filepath + "/" + rn + ".pdf"
        self.pdf = canvas.Canvas(abs_path)
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
        pdf.setFont("Courier-Bold", 16)
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
        
# Second Template (German)

class mypdf1:
    def __init__(self, path=""):
        self.vendor_name = "Max Mustermann"
        self.vendor_job = "Jurist"
        self.vendor_address = "lautstraße 2"
        self.vendor_city = "Entenhausen"
        self.vendor_city_key = "12345"
        self.vendor_phone = "0212/531762"
        self.vendor_iban = "DE12345678901234567890"
        self.filepath = path

        # Create a style sheet
        styles = getSampleStyleSheet()

        # Define a new style called "Custom"
        styles.add(ParagraphStyle(name='Custom', fontSize=14, leading=16, fontName='Helvetica'))

        self.get_vendor_info()
 
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
        abs_path = self.filepath + "/" + rn + ".pdf"
        self.pdf = canvas.Canvas(abs_path)
        self.pdf.setTitle("Rechnung")
        mypdf1.create_header(self, self.pdf, Datum)
        mypdf1.create_kundendaten(self, self.pdf, Name, Adresse, Ort)
        mypdf1.create_betreff(self, self.pdf, Betreff, rn)	
        mypdf1.create_briefinhalt(self, self.pdf, Briefinhalt, Betrag)
        self.pdf.save() 

    def create_header(self, pdf, datum):
        pdf.drawString(420, 800, self.vendor_city + ", den " + datum)
        text = pdf.beginText(30, 800)
        text.textLine(self.vendor_name)
        text.textLine(self.vendor_job)
        text.textLine(self.vendor_address)
        text.textLine(self.vendor_city_key + " " + self.vendor_city)
        text.textLine(self.vendor_phone)
        pdf.drawText(text)
        pdf.line(30, 730, 550, 730)

    def create_kundendaten(self, pdf, name, adresse, ort):
            text = pdf.beginText(30, 710)
            text.textLine(name)
            text.textLine(adresse)
            text.textLine(ort)
            pdf.drawText(text)   

    def create_betreff(self, pdf, betreff, rn_nr):
        pdf.setFont("Helvetica-Bold", 16)
        title = "Rechnung " + betreff
        title_rn = "Rechnungsnummer: " + rn_nr
        pdf.drawString(30, 600, title)
        pdf.drawString(30, 580, title_rn)

    def create_briefinhalt(self, pdf, briefinhalt, Betrag):
        pdf.setFont("Helvetica", 12)
        text = pdf.beginText(30, 450)
        text.textLine("Sehr geehrte Damen und Herren,")
        text.textLine("")
        text.textLine(briefinhalt + " bitte ich Sie, " + Betrag + " Euro auf mein Konto zu überweisen.") 
        text.textLine("")
        text.textLine("")   
        text.textLine("")    
        text.textLine("Mit freundlichen Grüßen,")
        text.textLine("")
        text.textLine(self.vendor_name)
        pdf.drawText(text)
        pdf.setFont("Helvetica-Bold", 12)
        text = pdf.beginText(30, 390)
        text.textLine("IBAN: " + self.vendor_iban)    
        pdf.drawText(text)


# executíon example
def test():
    data = ("123456", "Prename Name", "Straße 2", "12345 Berlin", "für auftrag X im November 2022", "01.11.2022", "100,00", "für den X. Auftrag im November 2022")
    testbill = mypdf1()    
    testbill.filepath = "output"
    testbill.merge_modules_data_and_save(data)

#test()