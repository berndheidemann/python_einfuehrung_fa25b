def get_max_period(temperature_list, min_value):
    count=0
    max_count=0
    for temp in temperature_list:
        if temp>=min_value:
            count+=1
            # wir müssen uns merken, ob wir gerade eine Reihe haben, die größer ist als alle bisher.
            # Falls ja, haben wir ein neues max_count
            if max_count<count:
                max_count=count
        else:
            count=0
    return max_count


data=[20,22,23,21,19,24,20,22,23,23,24,22,22,21]
print(get_max_period(data, 22))