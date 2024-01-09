class HashTable:

	def __init__(self, size):
		self.size = size
		self.hash_table = self.create_buckets()

	def create_buckets(self):
		return [[] for _ in range(self.size)]

	def set_val(self, key, val):
		
		hashed_key = hash(key) % self.size
		
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			if record_key == key:
				found_key = True
				break

		if found_key:
			bucket[index] = (key, val)
		else:
			bucket.append((key, val))

	def get_val(self, key):
		
		hashed_key = hash(key) % self.size
		
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			if record_key == key:
				found_key = True
				break

		if found_key:
			return record_val
		else:
			return "Data yang dicari tidak ada"

	def delete_val(self, key):
		
		hashed_key = hash(key) % self.size
		
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			if record_key == key:
				found_key = True
				break
		if found_key:
			bucket.pop(index)
		return

	def __str__(self):
		return "".join(str(item) for item in self.hash_table)


print("=" * 44)
print("| Selamat Datang di Pemrograman Hash Table |")
print("=" * 44)

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
        k = input("Masukkan Key: ")
        v = input("Masukkan Value: ")
        hash_table.set_val(k, v)
        print(hash_table)
        print()
    elif inp == 2:
        d = input("Masukkan Key untuk Data yang akan dihapus: ")
        hash_table.delete_val(d)
        print(hash_table)
        print()
    elif inp == 3:
        s = input("Masukkan Key untuk Data yang akan dicari: ")
        print("Value-nya adalah: " + hash_table.get_val(s))
        print()
    elif inp == 4:
        print("===== Terima Kasih =====")
        print()
        break
