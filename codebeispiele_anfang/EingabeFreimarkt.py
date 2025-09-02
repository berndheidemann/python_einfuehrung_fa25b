
# Es kommt eine Ausgabe mit "Gib deinen Kontostand ein:" und dann wartet das Programm auf
# eine Eingabe vom Benutzer
kontostand = input("Gib deinen Kontostand ein: ")

# Problem, diese Eingabe ist immer ein Text, wir brauchen aber eine Zahl um damit zu rechnen
kontostand = int(kontostand)  # Umwandeln in eine Zahl

# Es kommt eine Ausgabe mit "Hast du Lust auf Party? (ja/nein):" und dann wartet das Programm auf
# eine Eingabe vom Benutzer
bock_auf_party = input("Hast du Lust auf Party? (ja/nein): ")

# Es kommt eine Ausgabe mit "Bist du eingeladen? (ja/nein):" und dann wartet das Programm auf
# eine Eingabe vom Benutzer
eingeladen = input("Bist du eingeladen? (ja/nein): ")


''' 
bock_auf_party   |    kontostand>30     |   eingeladen      |   Freimarkt
      nein                  nein                ja                  nein
      nein                  ja                  ja                  nein
      ja                    nein                ja                  ja
      ja                    ja                  ja                  ja
      ja                    ja                  nein                ja
      nein                  nein                nein                nein
'''
if bock_auf_party=="ja" and (kontostand>30 or eingeladen=="ja"):
    print("Ich gehe zum Freimarkt...")
else:
    print("Ich bleibe zuhause...")
