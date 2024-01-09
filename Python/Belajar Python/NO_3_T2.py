def Tambah_data(data):
    len = int(input("Berapa banyak data yang akan anda masukkan: "))
    for i in range (len):
        a = input("Silahkan tambahkan data: ")
        data.append(a)
    print("Data berhasil ditambahkan")

def Hapus_data(data):
    print("Menu: ")
    print("1. Menghapus sesuai dengan urutan data")
    print("2. Menghapus data dari urutan terakhir")
    print("3. Menghapus data dari urutan awal")
    print("4. Menghapus seluruh data")
    b = str(input("Pilihan (1, 2, 3 atau 4 dan tekan Enter): "))
    if (b == "1"):
        for i in range(0, len(data)):
            print(i ," = ", data[i])
        c = int(input("Masukkan urutan dari data yang ingin dihapus: "))
        data.pop(c)
    elif(b == "2"):
        data.pop()
    elif(b == "3"):
        data.pop(0)
    elif(b == "4"):
        for i in range(len(data)):
            data.pop()
    print("Data berhasil dihapuskan")

data = []
i=1
while(i>0):
    print(" ")
    print("======= Menu =======")
    print("1. Tambah data")
    print("2. Hapus data")
    print("3. Tampilkan data")
    print("4. Selesai")
    print("====================")
    a = str(input("Pilihan (1, 2, 3, atau 4 dan tekan Enter): "))
    if (a == "1"):
        print(" ")
        print("Tambah data")
        Tambah_data(data)
    elif(a == "2"):
        print(" ")
        print("Hapus data")
        Hapus_data(data)
    elif(a == "3"):
        print(" ")
        print("Tampilkan data")
        print(str(data).replace("deque",""))
    elif(a == "4"):
        print(" ")
        print("---------------")
        print("Selesai")
        print("Terima kasih")
        print("---------------")
        print(" ")
        break