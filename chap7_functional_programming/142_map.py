def mpBy2(data:list[int])-> list[int]:
    result = []
    for d in data:
        result.append(d*2)
    print("result:", result);
    return result


# === 目標: 將mpBy2()簡化並套用 map 函式 ===

result = map(lambda d:d*2,[1,2,3])
print("map address:",result) # 回傳一個map address，要得到這個資料，
print('get data:',list(result))


### 😏 Think in JavaScript
# - 這與JavaScript的`Array.map(data, func) `會回傳資料，且不影響原來的data值(immutable)，一樣的概念，相當簡潔。