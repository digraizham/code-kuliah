class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        print("\n")
        if self.head is None:
            print("Linked list kosong")
            return
        itr = self.head
        beStr = ''
        while itr:
            beStr += str(itr.data)+ " - "  if itr.next else str(itr.data)
            itr = itr.next
        print(beStr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def remove_end(self):
        self.remove_at(self.get_length()-1)
        return

    def remove_data(self, dataRemove):
        count = 0
        itr = self.head
        while itr:
            if str(itr.data) == str(dataRemove) :
                itr.next = itr.next.next

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)


iter=1
print("======================")
print("PROGRAM LINKED LIST (Tumpukan)")
print("======================")

ll = LinkedList()

while (iter > 0):
    print("\n--------| Menu |--------")
    print("1.Menambah data")
    print("2.Tampilkan data")
    print("3.Menghapus data")
    print("4.Keluar")

    choice= int(input("Pilih Menu:"))

    if(choice == 1):
        strInput=input("Masukkan Data, \njika ingin memasukan data lebih dari 1 data, \nsisipkan tanda '-' sebagai penghubung kalimat: \n")
        strVal = strInput.split('-')
        ll.insert_values(strVal)
        ll.display()
    elif (choice == 2):
        ll.display()
    elif(choice == 3):
        ll.remove_end()
        ll.display()
    elif (choice == 4):
        print("\nTerimakasih program selesai\n")
        break