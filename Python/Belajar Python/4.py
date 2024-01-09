def biner() :
    num = int(input("Masukkan angka yang ingin diubah : "))
    biner = ""
    while num > 0:
        mod = num % 2
        if mod == 1:
            biner = "1" + biner
        else:
            biner = "0" + biner
        num = num // 2
    print(biner)

def octal() :
    num = int(input("Masukkan angka yang ingin di ubah : "))
    octal = ""
    while num > 0 :
        mod = num % 8
        if mod == 0 :
            octal = "0" + octal
        if mod == 1 :
            octal = "1" + octal
        if mod == 2 :
            octal = "2" + octal
        if mod == 3 :
            octal = "3" + octal
        if mod == 4 :
            octal = "4" + octal
        if mod == 5 :
            octal = "5" + octal
        if mod == 6 :
            octal = "6" + octal
        if mod == 7 :
            octal = "7" + octal
        num = num // 8
    print(octal)

def hexadecimal() :
    number = int(input("masukkan angka yang ingin dikonversikan: "))
    hex_dec = ""
    while number > 0:
        mod = number % 16
        if mod == 0:
            hex_dec = "0" + hex_dec
        if mod == 1:
            hex_dec = "1" + hex_dec
        if mod == 2:
            hex_dec = "2" + hex_dec
        if mod == 3:
            hex_dec = "3" + hex_dec
        if mod == 4:
            hex_dec = "4" + hex_dec
        if mod == 5:
            hex_dec = "5" + hex_dec
        if mod == 6:
            hex_dec = "6" + hex_dec
        if mod == 7:
            hex_dec = "7" + hex_dec
        if mod == 8:
            hex_dec = "8" + hex_dec
        if mod == 9:
            hex_dec = "9" + hex_dec
        if mod == 10:
            hex_dec = "A" + hex_dec
        if mod == 11:
            hex_dec = "B" + hex_dec
        if mod == 12:
            hex_dec = "C" + hex_dec
        if mod == 13:
            hex_dec = "D" + hex_dec
        if mod == 14:
            hex_dec = "E" + hex_dec
        if mod == 15:
            hex_dec = "F" + hex_dec
        number = number // 16
    print(hex_dec)

print("Hallo! Selamat datang di konversi bilangan desimal")

print("1. Biner")
print("2. Oktal")
print("3. Heksadesimal")
judul_2 = str(input("Masukkan tujuan perubahan : "))
if judul_2 == "1" or "Biner" or "biner" :
    biner()
elif judul_2 == "2" or "Oktal" or "oktal" :
    octal()
elif judul_2 == "3" or "Heksadesimal" or "heksimal" :
    hexadecimal()

i = 1
while (i > 0) :
    loop = str(input("Apakah anda ingin memasukkan angka lain? (y/n): "))
    if loop == 'y':
        judul_2 = str(input("Masukkan tujuan perubahan: "))
        if judul_2 == "1" or "Biner" or "biner" :
            biner()
        elif judul_2 == "2" or "Oktal" or "oktal" :
            octal()
        elif judul_2 == "3" or "Heksadesimal" or "heksimal" :
            hexadecimal()
    if loop == 'n':
        print("Terima kasih! ")
        break