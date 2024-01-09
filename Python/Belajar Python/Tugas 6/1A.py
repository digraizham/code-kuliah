print('================')
print('|Selamat datang|')
print('================')

myList = [] 
run = True
while run:
    print("Menu")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Mulai Mencari Linear")
    print("5. Exit")
    choice = int(input("Pilih Menu: "))

    if(choice == 1):
        a = int(input("Banyaknya Data Yang Ingin Dimasukkan: "))
        for j in range(0, a):
            c = int(input("Masukkan Data : "))
            myList.append(c)
        print("")
    
    elif(choice == 2):
        for j in range(0, len(myList)):
            print(j, " = ", myList[j])
        e = int(input("Masukkan urutan dari data yang ingin dihapuskan: "))
        myList.pop(e)
        print("Data berhasil dihapus")

    elif(choice == 3):
        print(myList)
        print("")

    elif(choice == 4):
        cari = int(input("Masukkan Angka Yang Anda Cari : "))
        counter = 0
        while counter != len(myList):
            if myList[counter] == cari:
                print("Data ditemukan di Urutan : ",counter)
            counter += 1
        if cari not in myList:
            print("Data Tidak Ditemukan")
            print("")

    elif(choice == 5):
        print("TERIMAKASIH, SILAHKAN DATANG KEMBALI")
        run = False