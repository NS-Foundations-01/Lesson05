son_1 = int(input("1-sonni kiriting -> "))
son_2 = int(input("2-sonni kiriting -> "))

amal = str(input(" (+, -, *, /, **) quyidagi amallarni kiriting -> "))

if amal == '+':
    print(son_1 + son_2)

elif amal == '-':
    print(son_1 - son_2)

elif amal == '*':
    print(son_1 * son_2)

elif amal == '/':
    if son_2 == 0:
        print("2-sonimiz 0 ga teng")
    else:
        print(son_1 / son_2)

elif amal == '**':
    print(son_1 ** son_2)

else:
    print("Sizda jarayon toliq emas!")