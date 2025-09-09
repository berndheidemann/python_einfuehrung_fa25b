# 3x2 -8x + 4


# x bekommt einen float zugewiesen (Kommazahl)
x = 4.0


# 3*x**2 ---> rechnet drei mal X-Quadrat
# 8*x  --> 8 mal x
# das gesamte Ergebnis wird dann y zugewiesen
y = 3*x**2 - 8*x + 4
# oder y = 3*x*x -8*x + 4
# x**4 wäre zum Beispiel x hoch 4

print("Bei x =", x, "ergibt die Quadratgleichung den Wert", y)

# erneute Wertzuweisung, d.h. der "Speicherslot" bekommt einen neuen Inhalt
x = 2/3
# darum berechnen wir y nochmal neu
y = 3*x**2 - 8*x + 4
print("Bei x =", x, "ergibt die Quadratgleichung den Wert", y)

x = 2
y = 3*x**2 - 8*x + 4
print("Bei x =", x, "ergibt die Quadratgleichung den Wert", y)