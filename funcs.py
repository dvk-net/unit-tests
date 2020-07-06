'''
Module consists of functions to test 
'''
from typing import List, Union
def my_mean(in_list: List[Union[int, float]]) -> float:
    """
    Calculates mean of the provided list
    """
    summ = 0
    count = 0
    for i in in_list:
        count += 1
        summ += i
    return summ / count