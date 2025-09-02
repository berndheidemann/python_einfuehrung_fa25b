print("Hello")

test=5
print(test)

print(type(test))

test="Hallo"
print(test)
print(type(test))


# in test steht aktuell "Hallo"
test+=" Welt"     # Kurzform für test=test+" Welt
# Die Variable test hat jetzt den Wert --> "Hallo Welt"


test+=str(77)  # die Zahl 77 wird zu einem Text und an test angefügt
# Die Variable test hat jetzt den Wert --> "Hallo Welt77"


print(test)


anzahl_person=67            # Die Variable anzahl_person wird deklariert und mit dem Wert 67 initialisiert
print(anzahl_person)
anzahl_person=anzahl_person+9
# Die Variable anzahl_person hat jetzt den Wert --> 76

print("mehr:", anzahl_person)

anzahl_person=anzahl_person/2
# Die Variable anzahl_person hat jetzt den Wert --> 38.0
print("die Hälfte", anzahl_person)

print(type(anzahl_person))
anzahl_person=int(anzahl_person)   # Die Variable anzahl Person wird zu einem int (einer Ganzzahl) umgewandelt
# Die Variable anzahl_person hat jetzt den Wert --> 38

print(type(anzahl_person))
print("jetzt wieder int", anzahl_person)

