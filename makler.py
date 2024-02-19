
import json
print("Befinden Sie sich im ersten Raum?")
nextRoom = input()
i = 0
wohnung = []

def raumMessen(raumnummer):
    print("Wie soll der Raum heißen")
    raumName = input()
    print("Hat der Raum 4 Ecken?")
    if(input()=="Nein"):
        print("Teilen Sie den Raum in 2 Vierecke auf!!")
        print("Geben Sie die Maße vom ersten Raum ein. Wielang ist die erste Wand?")
        wandeinsraumeins = float(input())
        print("Geben Sie die Maße vom ersten Raum ein. Wielang ist die zweite Wand?")
        wandzweiraumeins = float(input())
        print("Geben Sie die Maße vom zweiten Raum ein. Wielang ist die erste Wand?")
        wandeinsraumzwei = float(input())
        print("Geben Sie die Maße vom zweiten Raum ein. Wielang ist die zweiten Wand?")
        wandzweiraumzwei = float(input())
        erstesMaß = wandeinsraumeins*wandzweiraumeins
        zweitesMaß= wandeinsraumzwei*wandzweiraumzwei
        gesamtFlaeche = erstesMaß+zweitesMaß
    else:
        print("Wielang ist die erste Wand?")
        erstesMaß = float(input())
        print("Wielang ist die zweite Wand?")
        zweitesMaß = float(input())
        gesamtFlaeche = erstesMaß*zweitesMaß
    raumnummer = {
        "raumName" : raumName,
        "erstesMaß": erstesMaß,
        "zweitesMaß":zweitesMaß,
        "gesamtFlaeche": gesamtFlaeche
    }
    print(raumnummer)
    wohnung.append(raumnummer)
    print(wohnung)

    

while(nextRoom == "Ja"):
    i = i+1
    raumMessen(i)
    print("gibt es noch einen Raum?")
    nextRoom = input()

if(nextRoom == "Nein"):
    wohnungGesamt = 0
    for dict in wohnung:
        wohnungGesamt = wohnungGesamt+dict["gesamtFlaeche"]
    round(wohnungGesamt,2)
    print("Die Gesamtfläche beträgt:")
    print(round(wohnungGesamt,2))
    print("Die durchschnittliche Fläche pro Raum beträgt:")
    print(round(wohnungGesamt/i,2))

    

    

    



