a = 1

def parent():
    a = 99 #<-- 嘗試著把這個commend掉，看看結果
    def confusion():
        return a
        
    return confusion()

print(parent())