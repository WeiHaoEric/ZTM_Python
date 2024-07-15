#Given the below class:
from typing import List


class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Judy", 8)
cat2 = Cat("Crazy", 3)
cat3 = Cat("CoCo", 10)

# 2 Create a function that finds the oldest cat
def oldCat(cats:List[Cat]):
    sortedCats = sorted(cats, key=lambda cat:cat.age)
    print("sorted cats: oldest one is", sortedCats[-1].name)

    return sortedCats[-1]



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldestCat = oldCat([cat1, cat2, cat3])
print(f'The oldest cat is {oldestCat.name} which is {oldestCat.age} years old.')