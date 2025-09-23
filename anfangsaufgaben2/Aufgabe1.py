'''
Während einer Sonderaktion wird ein Rabatt von 10% auf alle Einkäufe mit einem Gesamtbetrag
von mehr als $10.00 gewährt. Schreiben Sie ein Programm, das nach dem Gesamtbetrag fragt und
den Discountpreis berechnet. Der Gesamtbetrag wird in Cent (als Ganzzahl) eingegeben.

Geben Sie den Gesamtbetrag ein: 2000
Discountpreis: 1800
'''

# 1. Benutzer nach dem Centbetrag fragen und speichern
cent=input("Geben Sie den Gesamtbetrag ein: ")




print("Hallo")

# 2. betrag in int umwandeln
cent=int(cent)

# 3. Fallunterscheidung einbauen
if cent>1000:
    # 3.1    über 1000 --> 10% Rabatt rechnen
    discountpreis=cent*0.9
else:
    # 3.2    unter 1000 --> Betrag bleibt gleich
    discountpreis=cent

discountpreis=int(discountpreis)

# 4. Ausgabe des Discountpreis
print("Discountpreis: ",discountpreis)

