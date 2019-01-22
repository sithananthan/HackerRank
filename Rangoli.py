def rangoli(n):
    c = (n*4) - 3
    r = (n*2) - 1
    ll = n + (n-1)
    initAlpha = 96
    laste = -1


    lista = list("-" * ll)

    for i in range(1, n+1):
        for j in range(1,i+1):
            if j % 2 == 1 :
                lista[laste] = chr(initAlpha + n - (i-1))
                laste -= 2
                if  -len(lista) > laste:
                    break
        print ("".join(lista))

rangoli(3)