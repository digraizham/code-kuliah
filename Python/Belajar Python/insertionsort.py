def insertion_sort(data):
    print("Base :", data)
    for i in range (1, len(data)):
        print("langkah", i)
        j = i
        while data[j-1] > data[j] and j > 0:
            data[j-1], data[j] = data[j], data[j-1]
            j -= 1
        print(data)

a = input("Angka ke-1: ")
b = input("Angka ke-2: ")
c = input("Angka ke-3: ")
d = input("Angka ke-4: ")
e = input("Angka ke-5: ")
int(a);int(b);int(c);int(d);int(e) 
data = [a, b, c, d, e]
insertion_sort(data)