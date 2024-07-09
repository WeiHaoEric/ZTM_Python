from functools import reduce

data = [1,2,3,4,5]
result = reduce(lambda acc, item:acc+item, data, 0)
#               ^^^^^^^^^^^^^^^^^^^^^^^^^  ^^^^ ^^^
#                       arg1                arg2 arg3
# arg1: func
# arg2: iterable data, list/tuple
# arg3: init value

print(result) # 15