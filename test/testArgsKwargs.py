def myFunc(*args, **kwargs)->int:
    print("check args:", args)
    print("check kwargs:", kwargs)
    
    total = 0
    for val in kwargs.values():
        total+=val
    return sum(args) + total

print('run myFunc:',myFunc(1,2,3,4,5, one=111, two=222))
