
import random

def get_random_numbers(number):
    liste1 = []
    for i in range(number):
       liste1.append(random.randint(0, 9))
    return liste1

def evaluate_list(random_numbers, digit):
    # Wir müssen zählen, wie oft digit in random_numbers vorkommt
    count=0
    for zahl in random_numbers:
        if zahl==digit:
            count+=1
    return count

def get_random_numbers_to_string(random_numbers):
    my_list=[]
    for number in random_numbers:
        my_list.append(str(number))
    return " ".join(my_list)

def get_random_numbers_to_string2(random_numbers):
    result=""
    for zahl in random_numbers:
        result = result + str(zahl) + " "
    return result

data=get_random_numbers(100)
print(evaluate_list(data, 7))
print(get_random_numbers_to_string(data))
print(get_random_numbers_to_string2(data))