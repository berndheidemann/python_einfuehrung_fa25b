'''
Es soll ein DateValidator geschrieben werden, der Datumsangaben auf ihre Richtigkeit überprüft.
Das Datum 22.08.1977 ist beispielsweise ein gültiges Datum; 32.08.2019 ist dagegen ungültig.
Dabei ist die Schaltjahresregel zu berücksichtigen: wenn das Jahr durch 4 teilbar ist, ist es
ein Schaltjahr. Ist dieses Jahr allerdings auch durch 100 teilbar, ist es kein Schaltjahr.
Ist ein Jahr allerdings durch 4, durch 100 und durch 400 teilbar, ist es doch ein Schaltjahr.
'''

tag = 29
monat=2
jahr=2019


def date_error():
    print("Fehlerhaftes Datum!!")
    exit()


if tag<1 or tag>31:
    date_error()

if monat<1 or monat > 12:
    date_error()

if monat in [4, 6, 9, 11] and tag>30:   # Monate mit 30 Tagen
    date_error()

schaltjahr=False

if jahr%4==0:
    schaltjahr=True

if jahr%100==0:
    schaltjahr=False

if jahr%400==0:
    schaltjahr=True

if schaltjahr and monat==2 and tag>29:
    date_error()

if not schaltjahr and monat==2 and tag>28:
    date_error()

print("gültiges Datum!")






