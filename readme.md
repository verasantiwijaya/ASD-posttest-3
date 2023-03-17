Nama : Vera Santi Wijaya

NIM  : 2209116007

SINGLY LINKED LIST

A. PENJELASAN ALGORITMA

-Mengimport library pretty table untuk membuat tampilan display nantinya dapat terlihat lebih rapi

![Screenshot (548)](https://user-images.githubusercontent.com/122012870/225840525-7bb30458-d678-4a41-9f08-9477b44ead84.png)

-Membuat class yang gunanya sebagai wadah yang diberi nama yaitu Node, Node adalah tempat data disimpan dalam linked list

-Constructornya adalah __init__() yang berbentuk seperti method khusus dengan argumen self dan data yang selalu dipanggil pertama kali

-Self adalah keyboard default yang harus selalu digunakan didalam parameter 

-Data sendiri adalah potongan informasi yang ingin diinisialisasi berupa atribut menggunakan self.data agar dapat diterima oleh init

![Screenshot (549)](https://user-images.githubusercontent.com/122012870/225846615-f8f7b3b9-b4c3-46fb-aeb6-e2b538b6ea17.png)

-Membuat class untuk linked list

-Dengan simpul kepalanya menggunakan self.head

![Screenshot (550)](https://user-images.githubusercontent.com/122012870/225852966-3589b46b-9d34-486a-84b2-0277442b5380.png)

-Kemudian ada beberapa fungsi yang digunakan sebagai representasi perilaku yang dimiliki oleh objek 

-Ada fungsi Display yang memiliki parameter self, fungsi ini memiliki perilaku untuk menampilkan data yang telah dibuat, ditambahkan, maupun dihapus di output yang telah dikemas dalam pretty table

-Jika datanya belum ada maka otomatis akan menampilkan pengkondisian if (maaf data masih kosong)

![Screenshot (554)](https://user-images.githubusercontent.com/122012870/225855416-2a7425b0-0f59-4be7-890a-67261009fec7.png)

-Selanjutnya ada fungsi addFirst yang berguna untuk menambah data ke dalam linked list dengan urutan tambah diawal data, sehingga data yang paling baru akan berada di paling depan yang konsepnya mirip seperti tumpukan

![Screenshot (555)](https://user-images.githubusercontent.com/122012870/225856157-1e3aa487-1d70-4288-b9f6-7f1af23e0176.png)

-Selanjutnya ada fungsi delete, di dalam fungsi ini terdapat dua pengkondisian, yang dimana jika data yang diinput pengguna sesuai dengan yang berada di data, otomatis data yang diinputkan tersebut akan terhapus

-Lalu pada pengkondisian kedua jika data yang diinputkan salah maka yang terhapus adalah data terbaru atau tumpukan paling atas

![Screenshot (556)](https://user-images.githubusercontent.com/122012870/225857399-eb60c3b3-4d14-47d1-bf07-612f794f2fa0.png)

-Selanjutnya adalah fungsi untuk menghapus seluruh data yang telah dimasukkan dengan fungsi yang diberi nama clear

![Screenshot (557)](https://user-images.githubusercontent.com/122012870/225857919-5b992410-6ca2-459e-8e17-76156d44bcca.png)

-Terakhir adalah fungsi yang diberi nama menu, di dalam fungsi ini adalah tempat untuk memanggil fungsi fungsi diatas agar dapat dijalankan

-Pada pilihan nomor 1 yaitu memasukkan antrean terdapat for i in yang berguna agar antrean nantinya dapat dimasukkan lebih dari 1 inputan nama buku

-Pada pilihan nomor 2 yaitu tambah barang terdapat try dan except untuk menghindari error ketika pengguna terdapat kesalahan

-Pada pilihan nomor 3 yaitu hapus barang maka perilaku dari sifat delete akan dijalankan

-Pada pilihan nomor 4 yaitu menu hapus semua data barang maka perilaku dari fungsi clear akan dijalankan

-Pada pilihan nomor 5 yaitu display barang maka perilaku dari fungsi display akan dijalankan

-Pada pilihan nomor 6 yaitu history data keluar dan data masuk diperoleh dari inputan pengguna

![Screenshot (560)](https://user-images.githubusercontent.com/122012870/225859788-bd2dad16-0d40-4b73-804d-4fbf455675a4.png)

![Screenshot (561)](https://user-images.githubusercontent.com/122012870/225860269-4a6a9dfa-58a5-4e2c-85da-9e64f8afd261.png)

-Untuk memanggil fungsi menu sebagai fungsi utama yang pertama kali setiap program dijalankan maka perlu mengeksekusi fungsi sebagai __main__

![Screenshot (562)](https://user-images.githubusercontent.com/122012870/225862259-d895a08e-8cbe-43b5-bd32-89086c769c1e.png)


-

B. PENJELASAN OUTPUT

-Menu ini adalah menu pertama yang harus di buka untuk dapat mengakses menu lain

-Menu Masukkan Antrean, ini menu ini pengguna dapat memasukkan jumlah tumpukan yang diinginkan kemudian memasukkan nama buku sesuai yang diinginkan 

-Menu display untuk menampilkan buku yang telah diinput pengguna yang telah tersusun dalam bentuk table 

![Screenshot (564)](https://user-images.githubusercontent.com/122012870/225863746-3252860d-f5b2-4f0e-923c-916c223b7b90.png)

-Menu tambah barang, sama seperti menu sebelumnya namun dimenu ini pengguna hanya dapat menginput 1 jenis buku saja

-Menu display untuk menampilkan buku yang telah diinput pengguna yang telah tersusun dalam bentuk table

![Screenshot (566)](https://user-images.githubusercontent.com/122012870/225864565-9cc0e601-8b20-4d5a-bab5-802b580a0ddd.png)

-Menu Hapus buku untuk menghapus nama buku yang sesuai dengan inputan pengguna

-Menu display untuk menampilkan buku yang telah diinput pengguna yang telah tersusun dalam bentuk table

sebelum dihapus

![Screenshot (570)](https://user-images.githubusercontent.com/122012870/225866400-eb54bf54-af53-40b1-9255-a9bfabcf29c5.png)

setelah dihapus

![Screenshot (569)](https://user-images.githubusercontent.com/122012870/225866475-e5a59836-21af-4b0e-accf-be58465a2243.png)

-Menu Hapus Seluruh Barang, pada menu ini data yang seluruhnya tersimpan akan terhapus pada terakhir kali 

-Menu display untuk menampilkan buku yang telah diinput pengguna yang telah tersusun dalam bentuk table

![Screenshot (575)](https://user-images.githubusercontent.com/122012870/225868870-4e07d0d1-fcb0-4f23-baae-d2b5740164ad.png)


-Menu History Barang, pada menu ini kita dapat melihat history barang masuk pada pilihan 1 dan barang keluar pada pilihan kedua

-Menu ini hanya dapat melihat history pemasukan dan pengeluaran yang terakhir pada data

![Screenshot (573)](https://user-images.githubusercontent.com/122012870/225868509-1762115c-800d-4a66-89c3-c79529a1bd13.png)

