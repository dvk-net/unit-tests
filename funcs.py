'''
Module consists of functions to test 
'''
import requests
from requests.exceptions import ConnectionError
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


def get_site_status(url: str) -> Union[int, str]:
    pass
    # with requests.Session() as s:
    #     try:
    #         res = s.get(url)
    #         return res.status_code
    #     except ConnectionError as err:
    #         return str(err)

def site_checker(url) -> str:
    status = get_site_status(url)
    # status = get_site_status(url)
    if status == 200:
        return f'site { url } is ok.'
    else:
        return f'site { url } is not ok.'