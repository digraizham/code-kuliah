
def merge(arr, l, m, r):
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
 
def mergeSort(arr, l, r):
    if l < r:
 
        m = l+(r-l)//2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def Tambah_data(arr, b):
    i = 0
    while i in range(b):
        c = int(input("Masukkan data:"))
        arr.append(c)
        i += 1
    print("Tambah data berhasil")

def Hapus_data(arr, d):
    arr.pop(d)
    print("Hapus data berhasil")

def Print_data(arr):
    for i in range(len(arr)):
        print(arr[i], "," ,end=" ")
    print()
  
arr = []
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
        print("")
        b = int(input("Berapa banyak data yang ingin dimasukkkan: "))
        Tambah_data(arr, b)
        print("")
    if (a == 2):
        print("")
        j = 0
        while j in range(len(arr)):
            print(j, " : ", arr[j])
        d = int(input("Masukkan indeks dari data yang ingin dihapus: "))
        Hapus_data(arr, d)
        print("")
    if (a == 3):
        print("")
        n = len(arr)
        print("Data yang diberikan: ")
        for i in range(n):
            print("%d" % arr[i],end=" ")

        mergeSort(arr, 0, n-1)

        print("\n\nData yang sudah disusun: ")
        for i in range(n):
            print("%d" % arr[i],end=" ")
        print("")
    if (a == 4):
        print("")
        Print_data(arr)
        print("")
    if (a == 5):
        print("")
        print("|----Terima Kasih----|")
        print("")
        break
