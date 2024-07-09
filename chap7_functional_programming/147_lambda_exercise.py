# square
myList = [5,4,3]
result = map(lambda x:x*x, myList)
print(list(result))


# sort
data = [(0,2), (4,3), (9,9), (10, -10)]

# === 以第二個值來做sort
data.sort(key=lambda x:x[1])
print(data)

# === 將所有第二個值聚集起來，再做sort
a = [(0,2), (4,3), (9,9), (10, -10)]
result3 = list(map(lambda x:x[1], a))
result3.sort()
print(result3)