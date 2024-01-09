def DTB(number):
    biner = ""

    while number > 0:
        sisa_bagi = number % 2
        if sisa_bagi == 1:
            biner = "1" + biner
        else:
            biner = "0" + biner
        number = number // 2
    print(biner)

number = int(input("masukkan angka yang ingin dikonversikan: "))
DTB(number)
i = 1
while i > 0:
    data = str(input("Apakah anda ingin mencoba lagi (y/n) (lower case only): "))
    if data == 'y':
        number = int(input("masukkan angka yang ingin dikonversikan: "))
        DTB(number)
    if data == 'n':
        break