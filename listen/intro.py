data1 = []   # leere liste
data2 = [1, 7, 10, 12 ] # gefüllte liste
data3 = ["Hallo", 1, 12.9, 27, 1] # gefüllte Liste mit verschiedenen Datentypen

print(data2[2])  # Ausgabe 10
data2[2] = 12 # Element an der Stelle 2 neu setzen
print(data2)

# Element der Liste hinzufügen
data2.append(99)
print(data2)

# Wie groß ist die Liste?
print(len(data2))

# Alle geraden Elemente in einer Liste aufsummieren (mit einer Schleife)
sum_even=0
for index in range(len(data2)):   # index --> 0, 1, 2, 3, 4
    if data2[index]%2==0:
        sum_even+=data2[index]
print("sum_even", sum_even)

sum_even=0
# jeder Wert in data2 wird einmal in die Variable value gelegt und der Schleifenrumpf (der Code darunter)
# wird für diesen Wert ausgeführt
for value in data2:              # value --> 1, 7, 12, 12, 99
    if value%2==0:
        sum_even+=value
print("sum_even die zweite", sum_even)


# Zufallszahlen
import random
print(random.randint(0, 9))


