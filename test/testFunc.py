def func(d:int)->bool:
    '''
    check var d is > 0 or not.
    '''
    return d>0


def hello(name:str)->str:
    '''
     This function is return a str including 'Hello~'+name+' !'
    '''
    return 'Hello~'+name+' !'


def main()->None:
    # checkNum = func
    checkNum = lambda d:d>0
    print(checkNum(-100))
    print(hello('Eric'))
    print(hello.__doc__)
    # print(help(hello))



if __name__ == "__main__":
    main()