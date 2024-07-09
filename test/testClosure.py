# === closure ===
def dogHouse(x:int):
    total=x;

    def calDog(y:int):
        # nonlocal total
        # return total+y
        print("inner:", total)
        return total+y
    
    return calDog;


dh = dogHouse(10);
print(dh(5))


#=== curry func ===
# def sum(x:int):
#     return lambda y: x+y

# print(sum(5)(10))

#=== test nonlocal ===
# def outer():
#     x=10
#     def inner():
#         nonlocal x
#         x+=9
#         print("inner:", x)

#     inner()
#     print("outer:", x)
#     return x

# print(outer())