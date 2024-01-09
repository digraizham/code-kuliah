def DTH(number):
    heksadesimal = ""

    while number > 0:
        sisa_bagi = number % 16
        if sisa_bagi == 0:
            heksadesimal = "0" + heksadesimal
        elif sisa_bagi == 1:
            heksadesimal = "1" + heksadesimal
        elif sisa_bagi == 2:
            heksadesimal = "2" + heksadesimal
        elif sisa_bagi == 3:
            heksadesimal = "3" + heksadesimal
        elif sisa_bagi == 4:
            heksadesimal = "4" + heksadesimal
        elif sisa_bagi == 5:
            heksadesimal = "5" + heksadesimal
        elif sisa_bagi == 6:
            heksadesimal = "6" + heksadesimal
        elif sisa_bagi == 7:
            heksadesimal = "7" + heksadesimal
        elif sisa_bagi == 8:
            heksadesimal = "8" + heksadesimal
        elif sisa_bagi == 9:
            heksadesimal = "9" + heksadesimal
        elif sisa_bagi == 10:
            heksadesimal = "A" + heksadesimal
        elif sisa_bagi == 11:
            heksadesimal = "B" + heksadesimal
        elif sisa_bagi == 12:
            heksadesimal = "C" + heksadesimal
        elif sisa_bagi == 13:
            heksadesimal = "D" + heksadesimal
        elif sisa_bagi == 14:
            heksadesimal = "E" + heksadesimal
        elif sisa_bagi == 15:
            heksadesimal = "F" + heksadesimal
        number = number // 16
    print(heksadesimal)

number = int(input("masukkan angka yang ingin dikonversikan: "))
DTH(number)
i = 1
while i > 0:
    data = str(input("Apakah anda ingin mencoba lagi (y/n) (lower case only): "))
    if data == 'y':
        number = int(input("masukkan angka yang ingin dikonversikan: "))
        DTH(number)
    if data == 'n':
        break