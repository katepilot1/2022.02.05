N, X = map(int, input().split())
a = list(map(int, input().split()))
c = ""
for b in a :
    if b < X :
      c += str(b)
      c += " "  
print(c)
