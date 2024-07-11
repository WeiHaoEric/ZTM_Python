from typing import Union

RESULT_TYPE = Union[int, float, str] # multiple hint

def add5(num:RESULT_TYPE)-> Union[RESULT_TYPE, ValueError]:
    try:
        return int(num)+5
    except ValueError as err:
        return err
    

add5(5)
# add5('okla')