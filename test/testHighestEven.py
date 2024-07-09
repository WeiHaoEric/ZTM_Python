def highest_even(data:list) -> bool:
    if(len(data)==0):
        return False    
    
    fData = list(filter(lambda d:d%2==0 ,data))
    if(len(fData)==0):
        print("oops...not found!!")
        return False
    
    print("result:", max(fData))
    return True
    
highest_even(data=[1,3,5])