# 🏧 Simulasi Sistem ATM Berbasis Python

## 📌 Deskripsi

**Simulasi Sistem ATM** merupakan program sederhana berbasis Python yang dirancang untuk menggambarkan proses penggunaan mesin ATM, mulai dari autentikasi PIN, pengelolaan saldo, penarikan uang tunai, hingga pencatatan riwayat transaksi.

Program ini memiliki sistem keamanan berupa batas maksimal tiga kali percobaan memasukkan PIN. Setelah berhasil login, pengguna dapat memilih menu penarikan tunai, melihat riwayat transaksi, atau keluar dari sistem ATM.

Project ini dibuat sebagai latihan fundamental programming untuk memahami penggunaan perulangan `while`, percabangan, serta pengelolaan data menggunakan struktur data list.

## 🎯 Tujuan Pembuatan

- Memahami penggunaan perulangan `while`.
- Mempelajari penggunaan `break` untuk menghentikan perulangan.
- Memahami penggunaan `continue` untuk melewati proses tertentu.
- Mengimplementasikan percabangan `if`, `elif`, dan `else`.
- Memahami penggunaan list untuk menyimpan data transaksi.
- Mempelajari penggunaan `append()` untuk menambahkan data ke dalam list.
- Memahami penggunaan `len()` untuk menghitung jumlah elemen dalam list.
- Mengimplementasikan operasi aritmatika untuk mengelola saldo.
- Memahami penerapan logika autentikasi PIN sederhana.

## ⚙️ Fitur Program

### 1. Sistem Autentikasi PIN
Pengguna harus memasukkan PIN yang sesuai dengan PIN sistem untuk dapat mengakses menu ATM.

### 2. Batas Kesempatan Login
Program memberikan maksimal tiga kali kesempatan untuk memasukkan PIN. Jika seluruh kesempatan digunakan tanpa memasukkan PIN yang benar, akses ATM akan dihentikan dan kartu disimulasikan terblokir.

### 3. Menu Utama ATM
Setelah berhasil login, pengguna dapat memilih tiga menu utama:
- Tarik Tunai.
- Riwayat Transaksi.
- Keluar.

### 4. Penarikan Uang Tunai
Pengguna dapat memasukkan nominal uang yang ingin ditarik. Program akan memeriksa apakah saldo mencukupi sebelum melakukan penarikan.

### 5. Pengecekan Saldo (`continue`)
Jika nominal penarikan melebihi saldo yang tersedia, program menampilkan pesan bahwa saldo tidak mencukupi dan menggunakan `continue` untuk kembali ke menu ATM tanpa mengurangi saldo.

### 6. Pencatatan Riwayat Transaksi
Setiap penarikan yang berhasil akan disimpan ke dalam list menggunakan metode `append()`.

### 7. Menampilkan Riwayat Transaksi
Program dapat menampilkan seluruh transaksi penarikan yang telah berhasil dilakukan. Jika belum ada transaksi, program akan menampilkan pesan bahwa riwayat transaksi masih kosong.

### 8. Keluar dari Sistem (`break`)
Pengguna dapat memilih menu keluar untuk menghentikan perulangan menu ATM dan mengakhiri program.

## 🧠 Konsep Pemrograman yang Digunakan

| Konsep | Fungsi |
|---|---|
| `input()` | Menerima masukan dari pengguna. |
| `int()` | Mengubah input menjadi tipe data integer. |
| `while` | Menjalankan perulangan selama kondisi terpenuhi. |
| `while True` | Membuat perulangan menu ATM yang berjalan terus hingga dihentikan. |
| `if` | Memeriksa kondisi tertentu. |
| `elif` | Memeriksa kondisi alternatif. |
| `else` | Menjalankan perintah ketika kondisi sebelumnya tidak terpenuhi. |
| `break` | Menghentikan perulangan login atau menu ATM. |
| `continue` | Melewati proses penarikan ketika saldo tidak mencukupi. |
| `list` | Menyimpan kumpulan riwayat transaksi. |
| `append()` | Menambahkan transaksi baru ke dalam list. |
| `len()` | Menghitung jumlah transaksi dalam list. |
| `-=` | Mengurangi saldo setelah penarikan berhasil. |

## 💻 Teknologi yang Digunakan

- **Bahasa Pemrograman:** Python
- **Konsep:** Fundamental Programming
- **Struktur Data:** List
- **Editor:** Visual Studio Code / Python IDE lainnya

## ▶️ Cara Menjalankan Program

1. Pastikan Python sudah terinstal pada komputer.
2. Clone repository ini:

   ```bash
   git clone https://github.com/USERNAME/simulasi-sistem-atm.git
   ```

3. Masuk ke direktori repository:

   ```bash
   cd simulasi-sistem-atm
   ```

4. Jalankan program:

   ```bash
   python main.py
   ```

## 📷 Contoh Tampilan Program

```text
=== Simulasi Sistem ATM ===
Masukkan PIN Anda: 1234
Login Berhasil!

=== Menu ATM ===
1. Tarik Tunai
2. Riwayat Transaksi
3. Keluar
Pilih menu (1/2/3): 1

Masukkan nominal penarikan: 100000
Penarikan berhasil!
Sisa saldo saat ini: Rp 400000

=== Menu ATM ===
1. Tarik Tunai
2. Riwayat Transaksi
3. Keluar
Pilih menu (1/2/3): 2

=== Riwayat Transaksi ===
Tarik Tunai: Rp 100000

=== Menu ATM ===
1. Tarik Tunai
2. Riwayat Transaksi
3. Keluar
Pilih menu (1/2/3): 3

Terima kasih telah menggunakan ATM kami.
```

## 📚 Catatan Pembelajaran

Project ini merupakan latihan penerapan konsep dasar pemrograman Python melalui studi kasus sistem ATM sederhana.

Melalui project ini, dapat dipelajari bagaimana perulangan `while` digunakan untuk mengatur proses login dan menu ATM, bagaimana percabangan digunakan untuk menentukan tindakan berdasarkan pilihan pengguna, serta bagaimana list dimanfaatkan untuk menyimpan riwayat transaksi.

Project ini juga memberikan pemahaman mengenai penerapan logika autentikasi, pengecekan saldo, dan pengelolaan data transaksi dalam sebuah program.

**Catatan:** Program ini merupakan simulasi pembelajaran dan bukan sistem ATM sungguhan. PIN dan saldo masih ditentukan langsung di dalam kode.

---

## 👨‍💻 Author

**Irga Mochamad Rafly**

- **NPM:** 267006111160
- **Kelas:** B
- **Program Studi:** Informatika
- **Fakultas:** Teknik
- **Universitas:** Universitas Siliwangi (UNSIL)

---

*Dibuat sebagai bagian dari proses pembelajaran Fundamental Programming menggunakan Python.*
