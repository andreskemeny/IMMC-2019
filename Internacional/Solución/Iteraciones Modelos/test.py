from numpy import random
mazo = []
i = 0
cartas = []
a = 0
while a < 4:
    b=1
    while b < 14:
        cartas.append(b)
        b+=1
    a += 1
cartas.sort()
partidas = 0
while partidas < 1:
    partidas = float(input("Cuantas jugadas?: "))
    if partidas < 1:
        print("no pueden ser jugadas negativas o iguales que 0")

while i < partidas and len(cartas) >= 5:
    m = 0
    for mayor in cartas:
        if m < mayor:
            m = mayor
    mazo = []
    a = random.randint(1, m+1)
    b = random.randint(1, m+1)
    while a not in cartas:
        a = random.randint(1, m+1)
    while b not in cartas:
        b = random.randint(1, m+1)
    if a == 1:
        mazo.append("A")
        x = 11
    elif a == 11:
        mazo.append("J")
        x = 10
    elif a == 12:
        mazo.append("Q")
        x = 10
    elif a == 13:
        mazo.append("K")
        x = 10
    else:
        mazo.append(a)
        x = a
    if b == 1:
        mazo.append("A")
        y = 11
    elif b == 11:
        mazo.append("J")
        y = 10
    elif b == 12:
        mazo.append("Q")
        y = 10
    elif b == 13:
        mazo.append("K")
        y = 10
    else:
        mazo.append(b)
        y = b
    y += x
    f = cartas.index(a)
    fu = cartas.index(b)
    cartas.pop(f)
    cartas.pop(fu)
    print(mazo)
    siono = input("Desea otra carta? (Si-No): ")
    if siono == "Si":
        a = random.randint(1, m+1)
        while a not in cartas:
            a = random.randint(1, m+1)
        if a == 1:
            mazo.append("A")
            x = 11
        elif a == 11:
            mazo.append("J")
            x = 10
        elif a == 12:
            mazo.append("Q")
            x = 10
        elif a == 13:
            mazo.append("K")
            x = 10
        else:
            mazo.append(a)
            x = a
        y += x
        f = cartas.index(a)
        cartas.pop(f)
        print(mazo)
    c = random.randint(1, m+1)
    d = random.randint(1, m+1)
    while c not in cartas:
        c = random.randint(1, m+1)
    while d not in cartas:
        d = random.randint(1, m+1)
    if c == 1:
        p = 11
    elif c == 11:
        p = 10
    elif c == 12:
        p = 10
    elif c == 13:
        p = 10
    else:
        p = c
    if d == 1:
        q = 11
    elif d == 11:
        q = 10
    elif d == 12:
        q = 10
    elif d == 13:
        q = 10
    else:
        q = d
    z = q + p
    f = cartas.index(c)
    fu = cartas.index(d)
    cartas.pop(f)
    cartas.pop(fu)
    if y > 21:
        print("jugador: "+str(y)+" - computador: "+str(z))
        print("perdiste")
    elif y < z:
        print("jugador: "+str(y)+" - computador: "+str(z))
        print("perdiste")
    elif y == z:
        print("jugador: "+str(y)+" - computador: "+str(z))
        print("empate")
    else:
        print("jugador: "+str(y)+" - computador: "+str(z))
        print("ganaste")
    i+=1
if len(cartas) < 5:
    print("quedan menos de cinco cartas no podemos continuar")