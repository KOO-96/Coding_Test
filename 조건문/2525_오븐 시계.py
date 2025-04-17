A, B = map(int, input().split())
C = int(input())

def minu(A, B, C):    
    res = (A*60) + B + C
    hour = (res)//60
    minute = res - (hour*60)
    if hour >= 24:
        print(hour - 24, minute)
    else:
        print(hour, minute)

minu(A, B, C)