a = int(input())
for b in range(a) :
    H, W, N = map(int, input().split())
    c = (N % H) * 100
    if c == 0 :
        c = H * 100
        d = N // H 
    else :
        d = N // H + 1
    print(c+d)
