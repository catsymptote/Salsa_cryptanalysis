def average(values:list) -> int:
    total = 0
    for val in values:
        total += val
    #print(values)
    avg = total/len(values)
    return avg


def average_n(values:list, n=4) -> list:
    assert len(values) % n == 0

    avg_list = []
    for i in range(int(len(values)/n)):
        j = i*n
        avg_list.append(average(values[j:j+n]))
    return avg_list


def average_lists(lists:list) -> list:
    """list(list) --> list(int),
    where the ints are the average of the internal list."""
    list_of_avg = []
    for lst in lists:
        avg = average(lst)
        list_of_avg.append(avg)
    return list_of_avg
