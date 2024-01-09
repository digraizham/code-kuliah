def merge_ascending(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0     
    j = 0     
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
def mergeSort_ascending(arr, l, r):
    if l < r:
 
        m = l+(r-l)//2

        mergeSort_ascending(arr, l, m)
        mergeSort_ascending(arr, m+1, r)
        merge_ascending(arr, l, m, r)
        print("\nProses: ", arr)

def merge_descending(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0     
    j = 0     
    k = l     
 
    while i < n1 and j < n2:
        if L[i] >= R[j]:
            arr[k] = L[i]
            i += 1 
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
def mergeSort_descending(arr, l, r):
    if l < r:
 
        m = l+(r-l)//2

        mergeSort_descending(arr, l, m)
        mergeSort_descending(arr, m+1, r)
        merge_descending(arr, l, m, r)
        print("\nProses: ", arr)

def Tambah_data(arr, arr2, b):
    i = 0
    while i in range(b):
        c = int(input("Masukkan data:"))
        arr.append(c)
        arr2.append(c)
        i += 1
    print("Tambah data berhasil")

def Hapus_data(arr, arr2):
    print("Menu: ")
    print("1. Menghapus data dari urutan terakhir")
    print("2. Menghapus data dari urutan awal")
    print("3. Menghapus seluruh data")
    d = str(input("Pilihan (1, 2, 3 atau 4 dan tekan Enter): "))
    if(d == "1"):
        arr.pop()
        arr2.pop()
    elif(d == "2"):
        arr.pop(0)
        arr2.pop(0)
    elif(d == "3"):
        for i in range(len(arr)):
            arr.pop()
            arr2.pop()
    print("Data berhasil dihapuskan")

def Print_data(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
arr = []
arr2 = []
while 1 > 0:
    print("|----Merge sort Menu:----|")
    print("|1. Tambah Data          |")
    print("|2. Hapus Data           |")
    print("|3. Merge Sort           |")
    print("|4. Tampilkan Data       |")
    print("|5. Selesai              |")
    print("|------------------------|")
    a = int(input("Masukkan angka: "))

    if (a == 1):
        print(" ")
        b = int(input("Berapa banyak data yang ingin dimasukkkan: "))
        Tambah_data(arr, arr2, b)
        print(" ")
    if (a == 2):
        print(" ")
        Hapus_data(arr, arr2)
        print(" ")
    if (a == 3):
        print(" ")
        print("|-------Menu: -------|")
        print("|1. Ascending        |")
        print("|2. Descending       |")
        print("|--------------------|")
        f = int(input("Masukkan pilihan angka: "))
        if (f == 1):
            n = len(arr)
            print("Data yang diberikan: ")
            for i in range(n):
                print("%d" % arr[i],end=" ")

            mergeSort_ascending(arr, 0, n-1)

            print("\n\nData yang sudah disusun: ")
            for i in range(n):
                print("%d" % arr[i],end=" ")
        elif (f == 2):
            n1 = len(arr2)
            print("Data yang diberikan: ")
            for i in range(n1):
                print("%d" % arr2[i],end=" ")

            mergeSort_descending(arr2, 0, n1-1)

            print("\n\nData yang sudah disusun: ")
            for i in range(n1):
                print("%d" % arr2[i],end=" ")
        print(" ")
    if (a == 4):
        print(" ")
        print("Data Ascending: ")
        Print_data(arr)
        print(" ")
        print("Data Descending: ")
        Print_data(arr2)
        print(" ")
    if (a == 5):
        print(" ")
        print("|----Terima Kasih----|")
        print(" ")
        break
