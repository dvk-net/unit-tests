def my_mean(in_list):
    """
    Calculates mean of the provided list
    """
    summ = 0
    count = 0
    for i in in_list:
        count += 1
        summ += i
    return summ / count