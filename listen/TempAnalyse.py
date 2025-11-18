temperaturen = [
    [22, 24, 19, 23, 25, 20, 21],  # Woche 1
    [18, 22, 21, 25, 26, 24, 19],  # Woche 2
    [20, 23, 22, 27, 24, 22, 18],  # Woche 3
    [19, 21, 24, 26, 25, 23, 20],  # Woche 4
    [23, 25, 27, 26, 22, 24, 21]   # Woche 5
]

monat_temperaturen = [
    [   # Woche 1
        [21, 24, 22, 18, 25, 26, 19],  # Tag 1
        [22, 21, 23, 19, 24, 27, 20],  # Tag 2
        [23, 22, 24, 20, 25, 28, 21],  # Tag 3
        [24, 23, 25, 21, 26, 29, 22],  # Tag 4
        [25, 24, 26, 22, 27, 30, 23]   # Tag 5
    ],
    [   # Woche 2
        [26, 23, 27, 22, 28, 31, 24],  # Tag 1
        [27, 24, 28, 23, 29, 32, 25],  # Tag 2
        [28, 25, 29, 24, 30, 33, 26],  # Tag 3
        [29, 26, 30, 25, 31, 34, 27],  # Tag 4
        [30, 27, 31, 26, 32, 35, 28]   # Tag 5
    ],
    [   # Woche 3
        [20, 19, 21, 15, 23, 26, 18],  # Tag 1
        [22, 20, 22, 16, 24, 27, 19],  # Tag 2
        [23, 21, 23, 17, 25, 28, 20],  # Tag 3
        [24, 22, 24, 18, 26, 29, 21],  # Tag 4
        [25, 23, 25, 19, 27, 30, 22]   # Tag 5
    ],
    [   # Woche 4
        [21, 23, 22, 19, 26, 28, 20],  # Tag 1
        [22, 24, 23, 20, 27, 29, 21],  # Tag 2
        [23, 25, 24, 21, 28, 30, 22],  # Tag 3
        [24, 26, 25, 22, 29, 31, 23],  # Tag 4
        [25, 27, 26, 23, 30, 32, 24]   # Tag 5
    ]
]

import random

def random_temp_list():
    weeks=5
    days=7
    temp_list=[]
    # Schleife die so oft läuft, wie die Anzahl der Wochen
    for w in range(weeks):
        week_temp=[]
        # Schleife die so oft läuft, wie die Anzahl der Tage
        for d in range(days):
            # für jeden Tag wird eine zufällige Temperatur zwischen 15 und 30 Grad erzeugt
            week_temp.append(random.randint(15,30))
        # die Liste der Temperaturen für die Woche wird der Liste der Wochen hinzugefügt
        temp_list.append(week_temp)
    return temp_list

def print_temperaturen(temperaturen):
    idx=1
    for week in temperaturen:
        week_str=f"Woche {idx}: "
        for day in week:
            week_str+=f"{day}, "
        print(week_str)
        idx+=1

def print_temperaturen2(temperaturen):
    idx=1
    for week in temperaturen:
        week_str=f"Woche {idx}: "
        # map(str, week) ---> für jedes Element in week wird die Funktion str angewendet
        # join --> "klebt" die Strings mit dem Trennzeichen , zusammen
        week_str+=",".join(map(str, week))
        idx+=1
        print(week_str)

def durchschnitt_temperatur_woche(temperaturen):
    week_avg=[]
    for week in temperaturen:
        week_avg.append(sum(week)/len(week))
    return week_avg

def max_temperatur_pro_tag(temperaturen):
    # wir fangen bei 0 an zu zählen bis inkl. 6, da wir eine Liste mit 7 Elementen haben und bei 0 starten
    for week_day in range(7):
        # hier eine Temperatur eintragen, die definitiv kleiner ist als alle anderen
        max_temp=float("-inf")
        # hier eine ID die nicht existiert
        max_week=-10
        for idx, week in enumerate(temperaturen):
            if week[week_day]>max_temp:
                max_temp=week[week_day]
                max_week=idx
        # week_day +1 da der Benutzer als ersten Wochentag keine 0 sondern eine 1 will
        print(f"der wärmste Wochentag für Wochentag {week_day+1}, war in Woche {max_week+1}")

def max_temperatur_pro_tag2(temperaturen):
    return [max(tag_list) for tag_list in zip(*temperaturen)]

def tage_mit_maximum(temperaturen):
    tage_max = []
    for tag_index, woche in enumerate(temperaturen):
        max_temp = max(woche)
        tag_index = woche.index(max_temp)
        tage_max.append(tag_index)
    return tage_max

def tage_mit_maximum2(temperaturen):
    return [week.index(max(week)) for week in temperaturen]


#Aufgabe 2
#2.1
def monat_temperaturen2(messurements=7, days=5, week=4, min_temps=10, max_temps=35):
    temperatur = [[[random.randint(min_temps, max_temps) for i in range(messurements)]for i in range(days)] for i in range(week)]
    return temperatur

#für Lesbarkeit
def print_temperaturen2(temperaturen):
    week_index=1
    tag_index=1
    for week in temperaturen:
        print()
        print(f"Woche{week_index}:", end="\t")
        week_index += 1
        for day in week:
            print()
            print(f"Tag{tag_index}:", end="\t")
            tag_index += 1
            for messurement in day:
                print(f"{messurement}C°", end="\t")
    print()

def durchschnitt_temperatur_woche(temps):
    for idx, week in enumerate(temps):
        week_sum=0
        measurements_count=0
        for measurements in week:
            sum_measurements=sum(measurements)
            measurements_count+=len(measurements)
            week_sum+=sum_measurements
        print(f"Woche {idx+1}: {week_sum/(measurements_count)}")

def durchschnitt_temperatur_woche_ohne_enumerate(temp_data):
    week_idx=0
    for week in temp_data:
        week_sum=0
        measurements_count=0
        for measurements in week:
            sum_measurements=sum(measurements)
            measurements_count+=len(measurements)
            week_sum+=sum_measurements
        week_idx+=1
        print(f"Woche {week_idx+1}: {week_sum/(measurements_count)}")

def durchschnitt_temperatur_monat3(monat_temperaturen):
    comp = [[round(sum(days)/len(days),2) for days in week ] for week in monat_temperaturen]
    sec = [round(sum(tage)/len(tage),2) for tage in comp]
    print(sec)


def heissester_tag_monat(temps):
    max_temp=-10000
    max_week=-2
    max_day=-2
    # Schleife, die über jede Woche der Liste iteriert. Enumerate ermöglicht das verwenden von week_idx
    for week_idx, week in enumerate(temps):
        # Schleife, die über jeden tag der Woche iteriert
        for day_idx, day in enumerate(week):
            # ...
            for measurement in day:
                # Wenn der Messpunkt über der bisher größten Temperatur liegt
                if measurement>max_temp:
                    # Die Variable max_temp bekommt einen neuen Wert zugewiesen (den aktuellen Messpunkt)
                    max_temp=measurement
                    # in max_week speichern wir, in welcher Woche wir gerade sind
                    max_week=week_idx
                    # in max_day speichern wir, an welchem Tag wir gerade sind
                    max_day=day_idx
    print(f"der heisseste Tag war in Woche {max_week} und Tag {max_day} mit: {max_temp} Grad")

def wochen_mit_extremen_temperaturen(temps):
    extreme_weeks=[]
    for week_idx, week in enumerate(temps):
        for day in week:
            for measurement in day:
                if measurement<12 or measurement>30:
                    extreme_weeks.append(week_idx+1)
    print(f"extreme Wochen: {set(extreme_weeks)}")


def sortiere_temperaturen(temps):
    temp_list = []
    for week in temps:
        for day in week:
            for measurement in day:
                temp_list.append(measurement)
    temp_list.sort()
    print(temp_list)

# sortiere_temperaturen(monat_temperaturen_fixed)
#wochen_mit_extremen_temperaturen(monat_temperaturen_fixed)
#heissester_tag_monat(monat_temperaturen_fixed)


#durchschnitt_temperatur_woche2(monat_temperaturen_fixed)
#durchschnitt_temperatur_monat3((monat_temperaturen_fixed))


'''
print(tage_mit_maximum(temperaturen))
print(tage_mit_maximum2(temperaturen))



print([tag for tag in zip(*temperaturen)])
print(temperaturen)
print(*temperaturen)

liste1=[7, 12, 13]
liste2=["a", "b", "c"]

for i, s in zip(liste1, liste2):
    print(str(i), s)

for a,b,c,d,e in zip(*temperaturen):
    print(a)

tempMontag, tempDienstag, tempMittwoch, woche4, woche5, woche6, woche7=zip(*temperaturen)
print(tempMontag)



max_temperatur_pro_tag(temperaturen)
print(durchschnitt_temperatur_woche(temperaturen))
'''






