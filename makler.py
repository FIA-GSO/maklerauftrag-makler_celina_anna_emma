
import json
print("Befinden Sie sich im ersten Raum? Ja/Nein") 
nextRoom = input()
i = 0
wohnung = [] #leere Liste für unsere Wohnung

def raumMessen(raumnummer): #Funktion für die Raummessung
    print("Wie soll der Raum heißen") #Raumbenennung
    raumName = input()
    print("Hat der Raum 4 Ecken?") #Kann man den Flächeninhalt vom Raum mit 2 Wänden berechnen?
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
        erstesMaß = wandeinsraumeins*wandzweiraumeins #Flächeninhalt vom ersten Teilraum wird berechnet
        zweitesMaß= wandeinsraumzwei*wandzweiraumzwei #Flächeninhalt vom zweiten Teilraum wird berechnet
        gesamtFlaeche = erstesMaß+zweitesMaß #Gesamtfläche des ursprünglichen Raumes wird berechnet indem beide Teilräume addiert werden.
    else:
        print("Wielang ist die erste Wand?")
        erstesMaß = float(input())
        print("Wielang ist die zweite Wand?")
        zweitesMaß = float(input())
        gesamtFlaeche = erstesMaß*zweitesMaß #Gesamtfläche des rechteckigen Raumes wird berechnet.
    raumnummer = { # Initialisierung eines Dictionaries mit Raumname, Maßen von zwei Wänden und der Gesamtfläche
        "raumName" : raumName,
        "erstesMaß": erstesMaß,
        "zweitesMaß":zweitesMaß,
        "gesamtFlaeche": gesamtFlaeche
    }
    print(raumnummer)
    wohnung.append(raumnummer) #Der Raum wird der Wohnungsliste hinzugefügt

while(nextRoom == "Ja"): # Wenn es weitere Räume gibt, werden auch diese ausgemessen
    i = i+1
    raumMessen(i)
    print("gibt es noch einen Raum?")
    nextRoom = input()

if(nextRoom == "Nein"): # Wenn es keinen weiteren Raum gibt, wird die Gesamtfläche der Wohnung und die durchschnittliche Fläche pro Raum berechnet.
    wohnungGesamt = 0
    for dict in wohnung:
        wohnungGesamt = wohnungGesamt+dict["gesamtFlaeche"]
    round(wohnungGesamt,2)
    print("Die Gesamtfläche beträgt:")
    print(round(wohnungGesamt,2))
    print("Die durchschnittliche Fläche pro Raum beträgt:")
    print(round(wohnungGesamt/i,2))
    

    

    

    



