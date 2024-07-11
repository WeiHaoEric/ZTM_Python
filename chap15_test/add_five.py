from typing import Union

RESULT_TYPE = Union[int, float, str] # multiple hint

def add5(num:RESULT_TYPE)-> Union[RESULT_TYPE, ValueError]:
    try:
        if num:
            return int(num)+5
        else:
            return "[Error]: please provide the val for num."

    except ValueError as err:
        return err
    

add5(0)
# add5('okla')