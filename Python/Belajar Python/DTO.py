def DTO(number):
    oktal = ""

    while number > 0:
        sisa_bagi = number % 8
        if sisa_bagi == 0:
            oktal = "0" + oktal
        elif sisa_bagi == 1:
            oktal = "1" + oktal
        elif sisa_bagi == 2:
            oktal = "2" + oktal
        elif sisa_bagi == 3:
            oktal = "3" + oktal
        elif sisa_bagi == 4:
            oktal = "4" + oktal
        elif sisa_bagi == 5:
            oktal = "5" + oktal
        elif sisa_bagi == 6:
            oktal = "6" + oktal
        elif sisa_bagi == 7:
            oktal = "7" + oktal
        number = number // 8
    print(oktal)

number = int(input("masukkan angka yang ingin dikonversikan: "))
DTO(number)
i = 1
while i > 0:
    data = str(input("Apakah anda ingin mencoba lagi (y/n) (lower case only): "))
    if data == 'y':
        number = int(input("masukkan angka yang ingin dikonversikan: "))
        DTO(number)
    if data == 'n':
        break