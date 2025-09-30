
'''
1.	Implementiere die Methode def get_GGT(number1, number2)). Sie ermittelt den größten
gemeinsamen Teiler der beiden übergebenen Zahlen. Der ggT lässt sich ermitteln, indem die
kleinere der beiden Zahlen von der größeren abgezogen wird. Das Ergebnis wird dann in die
 Variable gespeichert, in der die größere Zahl steht. Dieser Vorgang wird solange wiederholt,
  bis das Ergebnis 0 ist.

Beispiel:
12 und 8
12-8 = 4
8-4=4
4-4=0
Der ggT ist also 4
'''



#               12      8
def get_GGT(number1, number2):
    # wiederhole

    while True:
        # prüfen welche Zahl größer ist
        if number1 > number2:
            # die kleinere Zahl von der größeren abziehen und das Ergebnis in die Variable speichern, die die größere Zahl ist
            number1=number1-number2
        else:
            number2=number2-number1

        if number1==0:
            # return beendet die ganze Funktion und damit auch die Endlosschleife
            return number2
        if number2==0:
            return number1


'''
2.	Implementiere die Methode def is_prime_number(number)). Sie ermittelt,ob es sich bei der übergebenen Zahl um eine 
Primzahl handelt. Primzahlen heißen Zahlen, die größer als 1, nur durch 1 und durch sich selbst ohne Rest teilbar sind. 
Handelt es sich um eine Primzahl, gibt die Methode `True`, andernfalls `False` zurück.
'''

#                       7
def is_prime_number(number):
    if number<2:
        return False

    # Modulo
    # 23%5       -> man rechnet 23/5 als Grundschüler. 23/5 = 4 Rest 3. Und Modulo errechnet nur den Rest
    # 11%10 --> 1
    # 127%100 --> 27
    # 3%2 --> 1


    # wie können wir prüfen, ob 7 wirklich eine Primzahl ist?
    # 7%2==0 --> Wenn das true wäre, wäre die 7 keine Primzahl (dann wäre die 7 ohne Rest durch 2 teilbar)
    # 7%3==0 --> Wenn das true wäre, wäre die 7 keine Primzahl (dann wäre die 7 ohne Rest durch 3 teilbar)
    # 7%4==0 --> Wenn das true wäre, wäre die 7 keine Primzahl (dann wäre die 7 ohne Rest durch 4 teilbar)
    # 7%5==0 --> Wenn das true wäre, wäre die 7 keine Primzahl (dann wäre die 7 ohne Rest durch 5 teilbar)
    # 7%6==0 --> Wenn das true wäre, wäre die 7 keine Primzahl (dann wäre die 7 ohne Rest durch 6 teilbar)
    divisor=2
    # laufe solange divisor kleiner als number ist
    while divisor<number:
        # ist number ohne Rest durch i teilbar?
        if number%divisor==0:
            # Falls ja, number ist KEINE Primzahl
            # breche die weitere Rechnung ab und gebe direkt False zurück
            return False
        divisor=divisor+1
    # Die Schleife wurde durchlaufen, d.h. number ist durch keine andere Zahl teilbar, also eine Primzahl
    return True

def is_prime_number_more_efficient(number):
    if number<2:
        return False

    divisor=2
    while divisor<=int((number+1)/2):
        if number%divisor==0:
            return False
        divisor=divisor+1
    return True

'''
3. Implementiere die Methode def get_prime_numbers(start, end). Sie gibt einen String zurück, der aus allen 
Primzahlen besteht, die sich in einem Intervall Start- und Endwert befinden. 
Beispiel: Startwert = 4 und Endwert = 19 
Der zurückgegebene String lautet "5 7 11 13 17 19"
'''
def get_prime_numbers(start, end):
    response=""
    # wir brauchen eine Schleife die von start bis end läuft
    while end>=start:
        # für jede Zahl in dem Intervall prüfen, ob es eine Primzahl ist
        if is_prime_number(start):
            # Falls ja: im Ergebnis abspeichern
            response=response+str(start)+" "
        # die "Laufvariable" verändern
        start=start+1
    return response

print(get_prime_numbers(5, 19))

#i=0
#while i<100:
#    print(i, is_prime_number(i))
#    i=i+1




#print(get_GGT(81, 12))



