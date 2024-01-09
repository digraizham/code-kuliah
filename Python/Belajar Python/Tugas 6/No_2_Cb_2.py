class Simpul:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next= None

    def display(self):
        print(self.val)

class SenaraiBerantai:
    def __init__(self):
        self.head = None
    
    def insert(self, key, val):
        new_node = Simpul(key, val)
 
        if self.head is None:
            self.head = new_node
            return
 
        ptr = self.head
        while (ptr.next):
            ptr = ptr.next
 
        ptr.next =  new_node

    def delete_node(self, key):
        temp = self.head

        if (temp is not None):
            if (temp.val== key):
                self.head = temp.next
                temp = None
                return

        while(temp is not None):
            if temp.val == key:
                break
            prev = temp
            temp = temp.next
 
        if(temp == None):
            return
 
        prev.next = temp.next
 
        temp = None
    
    def search(self, key):
        current = self.head
  
        while current != None:
            if current.key == key:
                return current.val
              
            current = current.next
          
        return "Data tidak ditemukan."

    def display(self):
        string = ""
        temp = self.head
        while (temp):
            string += f"[{temp.val}] --> "
            temp = temp.next
        string = string[:-5]
        print(string)

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = []
        for i in range(self.size):
            self.hash_table.append(None)
    
    def insert(self, key, val):
        index = key%self.size

        if self.hash_table[index] == None:
            self.hash_table[index] = SenaraiBerantai()
        self.hash_table[index].insert(key, val)

    def delete_val(self, key):
        index = key%self.size

        v = input("Masukkan value yang akan dihapus: ")
        if self.hash_table[index] != None:
            self.hash_table[index].delete_node(v)

    def search_val(self, key):
        index = key%self.size

        if (self.hash_table[index] != None):
            return self.hash_table[index].search(key)
            
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
                self.hash_table[i].display()
            else:
                print(f"index {i} = Kosong")
        return
                
print("=" * 44)
print("| Selamat Datang di Pemrograman Hash Table |")
print("|            Pembentukan Rantai            |")
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