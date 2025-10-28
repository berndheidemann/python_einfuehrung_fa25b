

# def --> Schlüsselwort, welches Python mitteilt, dass jetzt eine Funktion kommt
# double_all_values --> Der Name der Funktion
# (values) --> Parameter, eine oder mehrere Variablen mit denen die Funktion arbeiten soll
def double_all_values(values):
    # Code der Funktion
    for i in range(len(values)):
        values[i]=values[i]*2

    # return --> Das, was rechts neben dem return steht, ist die Antwort der Funktion
    return values


# das ( ) neben double_all_values bewirkt, dass die Funktion wirklich aufgerufen wird
print(double_all_values([8, 9, 12, 77]))