class User(): #<-- (object): 小括號裡面其實有object
    def sign_in(self):
        print("sign_in!")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        print(f"[Wizard]:{self.name} has power-${self.power}")
    
    def attack(self):
            print(f"[Wizard]: attact with {self.power}")
        
class Archer(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        print(f"[Archer]:{self.name} has power-${self.power}")

def attack(self):
        print(f"[Archer]: attact with {self.power}")

wizard = Wizard("HarryPorter", 50)
archer = Archer("NiceShot", 100)

# 用 isinstance(object, class) 來驗證看看
print("wizard 是不是 Wizard 的實例化：",isinstance(wizard, Wizard))
print("wizard 是不是 User 的實例化："  ,isinstance(wizard, User))
print("wizard 是不是 object 的實例化：",isinstance(wizard, object))

print("===")
print("archer 是不是 Archer 的實例化：",isinstance(archer, Archer))
print("archer 是不是 User 的實例化："  ,isinstance(archer, User))
print("archer 是不是 object 的實例化：",isinstance(archer, object))
