def bubblesort(data):
    for i in range (len(data)-1, 0, -1):
        for j in range (0, len(data)-1):
            if (data[j] > data[j+1]):
                data[j],data[j+1] = data[j+1],data[j]
        print(data)

a = input("Angka ke-1: ")
b = input("Angka ke-2: ")
c = input("Angka ke-3: ")
d = input("Angka ke-4: ")
e = input("Angka ke-5: ")
int(a);int(b);int(c);int(d);int(e) 
data = [a, b, c, d, e]
bubblesort(data)