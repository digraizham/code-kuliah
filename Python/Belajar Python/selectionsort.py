def selection_sort(data):
    for i in range (0, len(data)-1):
        print("Langkah", i+1)
        cur_min = i
        for j in range (i+1, len(data)):
            if data[j] < data[cur_min]:
                cur_min = j
        data[i], data[cur_min] = data[cur_min], data[i]
        print(data)

a = input("Angka ke-1: ")
b = input("Angka ke-2: ")
c = input("Angka ke-3: ")
d = input("Angka ke-4: ")
e = input("Angka ke-5: ")
int(a);int(b);int(c);int(d);int(e) 
data = [a, b, c, d, e]
selection_sort(data)