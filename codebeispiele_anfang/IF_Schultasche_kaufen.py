
# Variable Kontostand wird mit dem Wert 130 initialisiert
kontostand = 49

# Ausgabe
print("Wir haben gerade ", kontostand, " Euro auf dem Konto")

# Kontrollstruktur, d.h.
if kontostand>=50:    # liefert immer TRUE oder FALSE zurück
    #WENN der Kontostand größer oder gleich 50 ist,
    print("Schultasche gekauft für 50 Euro")
    # reduzieren den Kontostand um den Wert 50
    kontostand=kontostand-50
    # Ausgabe des neuen Kontostands
    print("Wir jetzt noch ", kontostand, " Euro auf dem Konto")

else:
    # WENN der Kontostand kleiner 50 ist
    print("Spar mal lieber...")

