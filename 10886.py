a = int(input())
notcute = 0
cute = 0
for b in range(a) :
    c = input()
    if c == "0" :
        notcute += 1
    else :
        cute += 1

if notcute > cute :
    print ("Junhee is not cute!")
else : 
    print ("Junhee is cute!")
