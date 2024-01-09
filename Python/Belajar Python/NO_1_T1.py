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

print(" ")
print("Hallo! Selamat datang di konversi bilangan desimal")
print("--------------------------------------------------")
print("1. Biner")
print("2. Oktal")
print("3. Heksadesimal")
print("--------------------------------------------------")
tujuan = str(input("Masukkan tujuan perubahan : "))
if tujuan == "1" or tujuan == "Biner" or tujuan == "biner" :
    number = int(input("masukkan angka yang ingin dikonversikan: "))
    DTB(number)
elif tujuan == "2" or tujuan == "Oktal" or tujuan == "oktal" :
    number = int(input("masukkan angka yang ingin dikonversikan: "))
    DTO(number)
elif tujuan == "3" or tujuan == "Heksadesimal" or tujuan == "heksadesimal" :
    number = int(input("masukkan angka yang ingin dikonversikan: "))
    DTH(number)

i = 1
while (i > 0) :
    loop = str(input("Apakah anda ingin memasukkan angka lain? (y/n): "))
    if loop == 'y':
        tujuan = str(input("Masukkan tujuan perubahan: "))
        if tujuan == "1" or tujuan == "Biner" or tujuan == "biner" :
            number = int(input("masukkan angka yang ingin dikonversikan: "))
            DTB(number)
        elif tujuan == "2" or tujuan == "Oktal" or tujuan == "oktal" :
            number = int(input("masukkan angka yang ingin dikonversikan: "))
            DTO(number)
        elif tujuan == "3" or tujuan == "Heksadesimal" or tujuan == "heksadesimal" :
            number = int(input("masukkan angka yang ingin dikonversikan: "))
            DTH(number)
    if loop == 'n':
        print("Terima kasih! ")
        break