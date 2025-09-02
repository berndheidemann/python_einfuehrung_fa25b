bock_auf_party=True
kontostand=4
eingeladen=True

if bock_auf_party==True and (kontostand>30 or eingeladen==True):
    print("Ich gehe zum Freimarkt...")
else:
    print("Ich bleibe zuhause...")