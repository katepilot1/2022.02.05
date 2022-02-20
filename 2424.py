H, M = map(int, input().split())
T = int(input())
if M + T < 60 :
    print(H, M+T)
else :
    A = (M+T)//60
    B = (M+T)%60
    if H+A>23 :
        print(H+A-24, B)
    else :
        print(H+A, B)
