import webbrowser
import os
from fpdf import FPDF
from filestack import Client

class Pdf_report:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatemate1, flatemate2, bill):

        flatmate2_pay = str(round(flatemate2.pay(bill=bill,flatmate2=flatemate1),2))
        flatmate1_pay = str(round(flatemate1.pay(bill=bill,flatmate2=flatemate2),2))
        pdf = FPDF(orientation='P', unit='pt', format= 'A4')
        pdf.add_page()
        pdf.image("files/sm_5afb1035655ac.jpg", w=45,h=45)
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill" , border=0, align="C",ln = 1)

        pdf.set_font(family='Times', size=12, style= "B" )

        pdf.cell(w=250, h=40, txt="Period:",align="C", border=0)
        pdf.cell(w=250, h=40, txt=bill.period,align="C", border=0, ln=1)

        pdf.set_font(family='Times', size=12, )

        pdf.cell(w=250, h=25, txt=flatemate1.name,align="C", border=0)
        pdf.cell(w=250, h=25, txt=flatmate1_pay, align="C",border=0,ln=1)
        pdf.cell(w=250, h=25, txt=flatemate2.name, align="C",border=0)
        pdf.cell(w=250, h=25, txt=flatmate2_pay,align="C", border=0)

        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)

class filesharer:
    def __init__(self,filepath, api_key="AtTSxWz9Tgi3tllCZjrcEz"):
        self.filepath= filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url