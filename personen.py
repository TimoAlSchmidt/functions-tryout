def naamPrinter(naam, leeftijd):
    print("Hallo "+str(naam)+", je leeftijd is "+str(leeftijd)+" jaar.")

while True:
    naam = input("Wat is uw naam?\n")
    if naam == "stop":
        break
    leeftijd = int(input("Wat is uw leeftijd?\n"))
    naamPrinter(naam, leeftijd)
