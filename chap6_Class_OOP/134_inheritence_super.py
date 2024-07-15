class User(): 
    # 幫User加入這行
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("sign_in!")


class Wizard(User):
    def __init__(self, name, power, email):
        #                           ^^^^^ email為新的輸入變數

        #=== 方法1: 呼叫父類別的__init__(self, email) ===
        # User.__init__(self, email) 

        #=== 方法2: 用super呼叫父類別，可省略(self) ===
        super().__init__(email) 


        self.name = name
        self.power = power
        print(f"[Wizard]:{self.name} has power-${self.power}")
    
    def attack(self):
            print(f"[Wizard]: attact with {self.power}")
        

wizard = Wizard("HarryPorter", 50, "wizard123@gmail.com")


print(wizard.email)