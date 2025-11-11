from ply.yacc import resultlimit


# list_to_analyse --> Name des Parameters in der Funktion
def sum_all_1(list_to_analyse):
    result=0
    # liefert mir alle "Zeilen-IDs"
    for row_idx in range(len(list_to_analyse)):    # len(list_to_analyse) --> 3
        # liefert mir alle "Spalten-IDs"
        for col_idx in range(len(list_to_analyse[row_idx])):  # len(list_to_analyse[row_idx]) --> 3
            result+=list_to_analyse[row_idx][col_idx]
    return result

def sum_all_2(list_to_analyse):
    result=0
    # ich bekomme für jede Zeile direkt die ganze Zeile als Liste geliefert
    for row in list_to_analyse:
        for col_idx in range(len(row)):
            result+=row[col_idx]
    return result

def sum_all_3(list_to_analyse):
    result=0
    for row in list_to_analyse:
        result+=sum(row)
    return result

def sum_all_4(list_to_analyse):
    return sum([sum(row) for row in list_to_analyse])


def row_sum(list_to_analyse):     # --> [27, 18, 19]
    result=[]
    for row in list_to_analyse:
        result.append(sum(row))
    return result

def col_sum_1(list_to_analyse):   # --> [17, 11, 6, 11, 15, 6]
    result=[]
    # list_to_analyse[0] --> komplette erste Zeile --> [7, 9, 1, 3, 7, 2]
    # len(list_to_analyse[0]) --> 6 (Länge der Liste der ersten Zeile)
    # for col_idx in range(len(list_to_analyse[0])): --> for col_idx in range(6): --> Eine Schleife die 6x läuft
    # col_idx --> im ersten Schleifendurchlauf eine 0, dann eine 1, dann eine 2, dann eine 3, dann eine 4, dann eine 5
    for col_idx in range(len(list_to_analyse[0])):
        col_sum=0
        # len(list_to_analyse) --> 3
        # for row_idx in range(3):
        for row_idx in range(len(list_to_analyse)):
            col_sum+=list_to_analyse[row_idx][col_idx]
        result.append(col_sum)
    return result

def col_sum_2(list_to_analyse):
    result=[0]*len(list_to_analyse[0])      # --> [0, 0, 0, 0, 0, 0]
    for row in list_to_analyse:
        for col_idx in range(len(row)):
            result[col_idx]+=row[col_idx]
    return result




sample_table = [
    [7, 9, 1, 3, 7, 2],
    [1, 2, 3, 4, 7, 1],
    [9, 0, 2, 4, 1, 3]
]


# sample_table --> Name des Parameters beim Aufrufen der Funktion
print("sum_all_1", sum_all_1(sample_table))
print("sum_all_2", sum_all_2(sample_table))
print("sum_all_3", sum_all_3(sample_table))
print("sum_all_4", sum_all_4(sample_table))
print("row_sum", row_sum(sample_table))
print("col_sum_1", col_sum_1(sample_table))
print("col_sum_2", col_sum_1(sample_table))