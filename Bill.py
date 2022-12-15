from files.flat import Bill, Flatmates
from files.pdf_generator import Pdf_report, filesharer

amount = float(input("Hey user, Enter bill amount: "))
period = input("What is period of bill, ex. Feb 2020: ")
name1 = input("What is name of 1st person: ")
days_in_house1 = float(input(f"How much days1 {name1} stays in house during bill period: "))
name2 = input("What is name of 2nd person: ")
days_in_house2 = float(input(f"How much days1 {name2} stays in house during bill period: "))

the_bill = Bill(amount ,period )
flatmate1 = Flatmates(name1 , days_in_house1)
flatmate2 = Flatmates(name2, days_in_house2)

pdfReport= Pdf_report(filename=f"{the_bill.period}.pdf")
pdfReport.generate(flatmate1 , flatmate2, bill = the_bill )

print(round(flatmate1.pay(the_bill, flatmate2)))
print(round(flatmate2.pay(the_bill, flatmate1)))

Filesharer = filesharer(filepath= pdfReport.filename)
print(Filesharer.share())