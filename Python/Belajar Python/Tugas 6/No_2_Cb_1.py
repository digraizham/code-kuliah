class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = []
        for i in range(self.size):
            self.hash_table.append(None)
    
    def insert(self, key, val):
        index = key%self.size

        for i in range(self.size):
            if (index + i <= self.size - 1):
                if self.hash_table[index+i] == None:
                    self.hash_table[index+i] = [key,val]
                    return
            else:
                if self.hash_table[index+i-self.size] == None:
                    self.hash_table[index+i-self.size] = [key,val]
                    return

    def delete_val(self, key):
        index = key%self.size

        for i in range(self.size):
            if (index + i <= self.size - 1):
                if (self.hash_table[index+i] == None):
                    continue
                if self.hash_table[index+i][0] == key:
                    self.hash_table[index+i] = None
                    return
            else:
                if (self.hash_table[index+i-self.size] == None):
                    continue
                if self.hash_table[index+i-self.size][0] == key:
                    self.hash_table[index+i-self.size] = None
                    return 

    def search_val(self, key):
        index = key%self.size

        for i in range(self.size):
            if (index + i <= self.size - 1):
                if (self.hash_table[index+i] == None):
                    continue
                if self.hash_table[index+i][0] == key:
                    return self.hash_table[index+i][1]
            else:
                if (self.hash_table[index+i-self.size] == None):
                    continue
                if self.hash_table[index+i-self.size][0] == key:
                    return self.hash_table[index+i-self.size][1]

            return "Data tidak ditemukan."

    def print(self):
        for i in range(self.size):
            if (self.hash_table[i]):
                print(f"index {i} = [{self.hash_table[i][0]} : {self.hash_table[i][1]}]")
            else:
                print(f"index {i} = Kosong")
        return

print("=" * 44)
print("| Selamat Datang di Pemrograman Hash Table |")
print("|           Pengalamatan Terbuka           |")
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