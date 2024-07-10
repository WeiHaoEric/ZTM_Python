# Find the char that shows twice

some_list= ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# === Eric 解析 ===
# 先用Set可以過濾重複的，並以此為引述做查詢
# List.count(key) 可以回傳每個key在List中的數量
# 透過這個條件式，找到結果

duplicate = [c for c in set(some_list) if some_list.count(c)>1]
print(duplicate)
