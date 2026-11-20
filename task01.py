raqamlar = [12, 323, 45, 4567456745, 144, 3, 0, 0, 0]

juft = []
toq = []
nol = []

for raqam in raqamlar:
    if raqam % 2 == 1:
        toq.append(raqam)

    elif raqam == 0:
        nol.append(raqam)

    else:
        juft.append(raqam)


print(juft)
print(toq)
print(nol)