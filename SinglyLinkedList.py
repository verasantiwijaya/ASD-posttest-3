from prettytable import PrettyTable

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class Linkedlist:
    def __init__(self):
        self.head = None

    def display(self):        
        myTable = PrettyTable(["List Tumpukan Buku"])
        if self.head is None:
            print("Maaf Data Masih Kosong")
        else:
            n = self.head
            while n is not None:
                myTable.add_row([n.data])
                n = n.next
        print(myTable)   


    def addFirst(self, data):
        data_baru = Node(data)
        if self.head == None:
            self.head = data_baru
        else:
            data_baru.next = self.head
            self.head = data_baru
  
    def delete(self, data):
        temp = self.head
        if (temp.next is not None):
            if(temp.data == data):
                self.head = temp.next
                temp = None
                return
            else:
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    prev = temp        
                    temp = temp.next
                if temp == None:
                    return
                prev.next = temp.next
                return
    
    def clear(self):
        self.head = None
        return True   
    
    def menu(self):
        while True:
            print("\n==================================")
            print("MENU YANG TERSEDIA")
            print("==================================")
            print("1. MASUKKAN ANTREAN")
            print("2. TAMBAH ANTREAN")
            print("3. HAPUS BUKU")
            print("4. HAPUS SELURUH DATA BUKU")
            print("5. TAMPILKAN DISPLAY SEKARANG") 
            print("6. TAMPILKAN DARI HISTORY TERAKHIR")
            print("==================================")    
            tanyamu = input("Masukkan menu: ")
            if tanyamu == "1":
                listy = Linkedlist()
                brp = int(input("Berapa data yang ingin diinput? : "))
                for i in range(brp):
                    data = str(input('masukkan nama buku: '))
                    listy.addFirst(data)
                #listy.display()
            elif tanyamu == "2":
                try:
                    data = str(input('masukkan nama buku: '))
                    listy.addFirst(data)
                    #listy.display()
                except:
                    print("Mohon masukkan antrean pada nomor 1 terlebih\ndahulu jika ingin menggunakan menu nomor 2")
            elif tanyamu == "3":
                #jika data yang dicari tidak ada maka dia otomatis menghapus baris pertama
                try: 
                    masukkan = input("Nama buku yang ingin dihapus: ")
                    listy.delete(masukkan)
                    #listy.display()
                except:
                    print("Mohon masukkan antrean pada nomor 1 terlebih\ndahulu jika ingin menggunakan menu nomor 3")
            elif tanyamu == "4":
                tanyalagi = str(input("Yakin Ingin Menghapus Semua Data? [y/n]: "))
                if tanyalagi=="y":
                    listy = Linkedlist()
                    listy.clear()
                    print("DATA BERHASI DIHAPUS")
                    # listy.display()
                else:
                    print("data tidak jadi dihapus")
                    listy.display()
            elif tanyamu == "5":
                try: 
                    print("DISPLAY SELURUH TUMPUKAN BUKU")
                    listy.display()
                except:
                    print("Mohon masukkan antrean pada nomor 1 terlebih\ndahulu jika ingin menggunakan menu nomor 5")
            elif tanyamu == "6":
                try: 
                    print("HISTORY DATA\n 1. History Tambah\n 2. History Hapus")
                    tanyadlu = int(input("\nMasukkan pilihan [1/2]: ")) 
                    if tanyadlu == 1:
                        print("Buku yang terakhir masuk  :", data)
                    elif tanyadlu == 2:
                        print("Buku yang terakhir keluar :", masukkan )
                except:
                    print("Mohon tambah/hapus data diatas terlebih \ndahulu jika ingin menggunakan menu")
            

if __name__ == "__main__":
    p = Linkedlist()
    p.menu()