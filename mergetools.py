string, k = input(), int(input())
start = 0
length = len(string)
step = length//k

for i in range(step):
    a = string[start:start+k]
    start += k
    newA = []
    for j in a:
        if j not in newA:
            newA.append(j)
    print ("".join(newA))

