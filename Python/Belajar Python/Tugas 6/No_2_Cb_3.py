class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = []
        for i in range(self.size):
            self.hash_table.append(None)
    
    def insert(self, key, val):
        index = key%self.size

        if self.hash_table[index] == None:
            self.hash_table[index] = [key, val, "none"]
        else:
            self.recursive_insert(key, val, self.hash_table[index])

    def delete_val(self, key):
        index = key%self.size

        v = input("Masukkan value yang akan dihapus: ")
        if self.hash_table[index] != None:
            if (self.hash_table[index][1] == v):
                if (self.hash_table[index][2] != "none"):
                    self.hash_table[index] = self.hash_table[index][2]
                else:
                    self.hash_table[index] = None
            else:
                if (self.hash_table[index][2] != "none"):
                    self.recursive_delete(v, self.hash_table[index]) 

    def search_val(self, key):
        index = key%self.size

        if (self.hash_table[index] != None):
            return self.recursive_search(key, self.hash_table[index])
            
    def recursive_insert(self, key, val, arr):
        if (arr[2] == "none"):
            arr[2] = [key, val, "none"]
            return

        self.recursive_insert(key, val, arr[2])

    def recursive_delete(self, val, arr):
        if (arr[2][1] == val):
            if (arr[2][2] != "none"):
                arr[2] = arr[2][2]
                return
            else:
                arr[2] = "none"
                return
        if (arr[2][2] != "none"):
            self.recursive_delete(val, arr[2])
        return

    def recursive_search(self, key, arr):
        if (arr[0] == key):
            return arr[1]
        if (arr[2] != "none"):
            self.recursive_search(key, arr[2])

    def print(self):
        for i in range(self.size):
            if (self.hash_table[i]):
                print(f"index {i} = ", end='')
                arr = self.hash_table[i]
                string = f"[{arr[0]} : {arr[1]}] --> "    

                while (arr[2] != "none"):
                    arr = arr[2]
                    string += f"[{arr[0]} : {arr[1]}] --> "
                    
                string = string[:-5]
                print(string)
            else:
                print(f"index {i} = Kosong")
        return

print("=" * 44)
print("| Selamat Datang di Pemrograman Hash Table |")
print("|            Pengalamatan Buket            |")
print("=" * 44)
print()
hash_table = HashTable(int(input("Silahkan Masukkan Batas Untuk Tabel Hash: ")))

run = 1
while run < 2:

    print()
    print("=" * 16)
    print("| Menu Program |")
    print("=" * 16)
    print("1. Insert Data Ke Dalam Hash Table")
    print("2. Remove Data Pada Hash Table")
    print("3. Search Data Pada Hash Table")
    print("4. Selesai")
    print("-" * 35)
    inp = int(input("Silahkan Tentukan Pilihan Anda: "))
    print()

    if inp == 1:
        k = int(input("Masukkan Key: "))
        v = input("Masukkan Value: ")
        hash_table.insert(k, v)
        hash_table.print()
        print()
    elif inp == 2:
        d = int(input("Masukkan Key untuk Data yang akan dihapus: "))
        hash_table.delete_val(d)
        hash_table.print()
        print()
    elif inp == 3:
        s = int(input("Masukkan Key untuk Data yang akan dicari: "))
        print("Value-nya adalah: " + hash_table.search_val(s))
        print()
    elif inp == 4:
        print("===== Terima Kasih =====")
        print()
        break