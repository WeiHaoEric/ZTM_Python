def getCounter(c:int) -> int:
    return c

def makeJuice() -> None:
    print("Wow...nice juice!")


def main() ->None:
    print("test Walrus!")
    # === 說明 ===
    # 我們用一個變數counter來承接func回傳的值，但其實counter只有下方的if會用到，又多佔了一行，礙眼啊!
    # counter = getCounter(0) 

    if(counter:=getCounter(99)): # <-- Python3.8之後, 提供了Walrus(海象)的用法, := 這符號是不是很像 "海象" 
        makeJuice()
    else:
        print("Bye~")
        return


if __name__ == "__main__":
    main()