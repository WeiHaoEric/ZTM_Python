# === Exercise Link: https://replit.com/@aneagoie/functional-1#main.py ===

from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
mResult = map(lambda d:d.upper(),my_pets)
print('capitalize result:', list(mResult))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]


zResult = zip(my_strings, my_numbers)
print(list(zResult))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
fResult = filter(lambda d: d>=50,scores)
print(list(fResult))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
reduce(lambda acc, x:acc+x, my_numbers+scores)
#                           ^^^^^^^^^^^^^^^^^
#                        python list直接相加的用法, 如JS的[...a, ...b]
