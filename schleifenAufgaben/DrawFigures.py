
def draw_square(sign, number_of_sign):
    if number_of_sign<1:
        return

    if number_of_sign==1:
        print(sign)
        return

    # erste Zeile ausgeben
    print(sign *number_of_sign)

    # alle Zeilen dazwischen ausgeben
    # Wie oft? bei number_of_signs 7 --> 5 mal
    row_count=number_of_sign-2

    # Schleife, die so oft läuft, wie row_count groß ist
    for i in range(row_count):
        # Eine Zeile dazwischen ausgeben
        # FÜR SIGN * und number_of_sign 5 --> *   *

        # -2, da ein Sternchen am Anfang und eines am Ende
        number_of_spaces=number_of_sign-2
        spaces=" "*number_of_spaces
        print(sign + spaces + sign)

    # letzte Zeile ausgeben
    print(sign *number_of_sign)


def draw_rhombus(diameter):
    # Gebe obersten Punkt in der Mitte aus
    spaces_count=int((diameter-1)/2)
    print(spaces_count*" "+".")

    # Gebe oberen schrägen Kasten aus
    upper_row_count=int((diameter-1)/2)-1
    initial_spaces = upper_row_count
    for i in range(upper_row_count):
        spaces=initial_spaces-i
        spaces_between=i*2+1
        print(spaces*" " + "/" + spaces_between*" " + "\\")

    # Gebe mittlere Zeile mit Punkten links und rechts aus
    spaces_count=diameter-2
    spaces=spaces_count*" "
    print("."+spaces+".")
    # Gebe unteren schrägen Kasten aus

    lower_row_count=upper_row_count
    for i in range(lower_row_count):
        spaces=i+1
        spaces_between=(diameter-4)-(2*i)
        print(spaces * " " + "\\" + spaces_between * " " + "/")

    # Gebe untersten Punkt in der Mitte aus
    spaces_count=int((diameter-1)/2)
    print(spaces_count*" "+".")


draw_rhombus(11)


#draw_square("*", 1)
