class Toy():
    def __init__(self, name):
        self.name = name
        data={"yoyo":100, "godzilla":600, "car":1200}

    # __str__ 就是對應回傳class object的string，也等同於 str(toy)會呼叫的函示
    def __str__(self):
        return self.name
    
    # __len__: 
    def __len__(self):
        return 1688
    
    # __call__:有宣告才能直接被呼叫
    def __call__(self, txt):
        print("Sooooo Cool...!!"+txt)
    

# 宣告一個變數
toy = Toy("Toyrus")

print("=== test toy.__str__() 以及 str(toy) ")
print(toy.__str__()) # 等同於 str(toy)
print(str(toy))


print("=== test toy.__len__() 以及 str(toy) ")
print(toy.__len__()) # 等同於 len(toy
print(len(toy))


print("=== test toy() 以及 str(toy) ")
toy.__call__("Goofy")
toy("Goofy")