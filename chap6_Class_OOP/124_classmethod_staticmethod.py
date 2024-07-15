class Calculator:
    def __init__(self, name="Siri"):
        self.name = name
        pass

    @staticmethod
    def add(num1, num2):
        result = num1+num2
        print(f'{num1}+{num2}={result}')
        return result

    @classmethod
    def comeOn(cls, name:str):
        #      ^^^
        # cls其實就是Calculator這個class
        # 嘗試著用cls來建立一個新的object
        return cls(name)

# test @staticmethod
print("=== test @staticmethod ===")
Calculator.add(1,3)

# test @classmethod
print("=== test @classmethod ===")
robot = Calculator.comeOn('Robot-XYZ')
robot.add(3,5)

