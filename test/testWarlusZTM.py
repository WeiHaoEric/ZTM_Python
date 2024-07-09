a = 'helooooooooooooo'

# 一般寫法
if(len(a) > 10):
    print(f"too long {len(a)} elements")

# Warlus寫法1:
if( (n:=len(a)) > 10):
    print(f"too long {n} elements")

# Warlus寫法2:
while((n:=len(a))>1):
    print(n)
    a = a[:-1]