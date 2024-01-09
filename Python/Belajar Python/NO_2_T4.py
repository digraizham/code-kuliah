def insertion_sort_ascending(data):
    k = 1
    print("Base data: ", data)
    for i in range (1, len(data)):
        
        j = i
        if data[j-1] > data[j]:
            print("langkah", k)
            while data[j-1] > data[j] and j > 0:
                print("Tukar ", data[j-1] ," Dengan ", data[j])
                data[j-1], data[j] = data[j], data[j-1]
                j -= 1
            k += 1
        else:
            continue
        print(data)
    k = 1

def insertion_sort_descending(data):
    k = 1
    print("Base data: ", data)
    for i in range (1, len(data)):
        
        j = i
        if data[j-1] < data[j]:
            print("langkah", k)
            while data[j-1] < data[j] and j > 0:
                print("Tukar ", data[j-1] ," Dengan ", data[j])
                data[j-1], data[j] = data[j], data[j-1]
                j -= 1
            k += 1
        else:
            continue
        print(data)
    k = 1

data = []
i = 1
while(i > 0):
    print("|======== Menu =========|")
    print("|1. Tambah Data         |")
    print("|2. Hapus Data          |")
    print("|3. Tampilkan data      |")
    print("|4. Mulai Insertion sort|")
    print("|5. Selesai             |")
    print("|=======================|")

    a = int(input("Masukkan pilihan anda: "))

    if (a == 1):
        b = int(input("Berapa banyak data yang ingin dimasukkan: "))
        for j in range(0, b):
            c = input("Masukkan angka: ")
            data.append(c)
        print("")
    elif(a == 2):
        print("")
        print("|=========Menu Hapus Data=========|")
        print("|1. Hapus dari belakang           |")
        print("|2. Hapus dari depan              |")
        print("|3. Hapus sesuai dengan letak data|")
        print("|=================================|")

        d = int(input("Masukkan pilihan angka: "))
        if(d == 1):
            data.pop()
            print("Data berhasil dihapus")
        elif(d == 2):
            data.pop(0)
            print("Data berhasil dihapus")
        elif(d == 3):
            for j in range(0, len(data)):
                print(j, " = ", data[j])
            e = int(input("Masukkan urutan dari data yang ingin dihapuskan: "))
            data.pop(e)
            print("Data berhasil dihapus")
        print("")
    elif(a == 3):
        print("Data: ", data)
        print("")
    elif(a == 4):
        print("")
        print("|==Insertion Sort Menu==|")
        print("|1. Descending          |")
        print("|2. Ascending           |")
        print("|=======================|")
        f = int(input("Masukkan pilihan anda: "))

        if (f == 1):
            insertion_sort_descending(data)
        if (f == 2):
            insertion_sort_ascending(data)
        print("")
    elif(a == 5):
        print("")
        print("|===Terima Kasih===|")
        print("")
        break