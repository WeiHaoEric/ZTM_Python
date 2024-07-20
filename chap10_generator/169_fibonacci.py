def fibList(num:int):
    if(num==0 or num==1):
        return num
    
    result = [0, 1]
    for i in range(2,num-2):
        idx1 = i-1
        idx2 = i-2
        result.append(result[idx2]+result[idx1])

    return result


def fib(nth:int):
    if(nth==0 or nth==1):
        return nth

    def genFib(num):
        p1 = 1
        p2 = 0
        for i in range(2, num-2):
            current = p1+p2
            
            # switch
            p2 = p1
            p1 = current
            # yield
            yield current
    
    # call generator
    myFibGenerator = genFib(nth)
    result = -1

    # Loop for generator
    while True:
        try :
            result = next(myFibGenerator)
        except StopIteration:
            break


    return result

print('case1: list fib',fibList(10))
print('case2: generator fib',fib(10))




