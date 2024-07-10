# === List 進階用法 ===

print([char for char in 'hello'])

# 快速產生1~10個偶數
print([num for num in range(1,10)])

# 從1~10找出偶數
print([num for num in range(1,10) if num % 2 ==0] )


# === Set 進階用法 ===
# avaliable in Set
print({c for c in "hello"})



# === Dictionary 進階用法 ===
data = {'a':1, 'b':2, 'c':3, 'd':4} ;

# 將資料變成 dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(data.items())

# 將來源的dict變成另一組dict
print({k:v**2 for k,v in data.items() if v %2==0})

# 使用一個值產生一個dict
print({k:k**2 for k in [1,2,3]});