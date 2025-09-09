

# input("Gib eine Temperatur in Celsius ein: ") -->
# stellt die Frage an den Anwender und erwartet eine Eingabe vom User (als string).
# das Programm "pausiert" bis der User etwas eingegeben hat
celsius=input("Gib eine Temperatur in Celsius ein: ")

# Warum diese Zeile? --> wir müssen den Datentyp von str auf int wechseln um zu rechnen
celsius=int(celsius)


fahrenheit=9/5 * celsius + 32

print(celsius, "Grad Celsius sind ",fahrenheit, "Grad Fahrenheit.")