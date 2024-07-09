def mpBy2(data:list[int])-> list[int]:
    result = []
    for d in data:
        result.append(d*2)
    print("result:", result);
    return result;

mpBy2([1,2,3])