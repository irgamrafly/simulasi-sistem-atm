print("=== Simulasi Sistem ATM ===")

pin_sistem = 1234
kesempatan = 3
saldo = 500000
riwayat_transaksi = []

while kesempatan > 0:
    pin = int(input("Masukkan PIN Anda: "))

    if pin == pin_sistem:
        print("Login Berhasil!")
        break
    else:
        kesempatan -= 1
        print("PIN Salah! Sisa kesempatan:", kesempatan)

if kesempatan == 0:
    print("Kartu Anda diblokir karena salah memasukkan PIN 3 kali.")
else:

    while True:
        print("\n=== Menu ATM ===")
        print("1. Tarik Tunai")
        print("2. Riwayat Transaksi")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "3":
            print("Terima kasih telah menggunakan ATM kami.")
            break

        elif pilihan == "1":
            nominal = int(input("Masukkan nominal penarikan: "))

            if nominal > saldo:
                print("Saldo tidak mencukupi (Continue).")
                continue

            saldo -= nominal

            riwayat_transaksi.append(
                f"Tarik Tunai: Rp {nominal}"
            )

            print("Penarikan berhasil!")
            print("Sisa saldo saat ini: Rp", saldo)

        elif pilihan == "2":
            if len(riwayat_transaksi) == 0:
                print("Belum ada transaksi")
            else:
                print("\n=== Riwayat Transaksi ===")
                for transaksi in riwayat_transaksi:
                    print(transaksi)

        else:
            print("Pilihan tidak valid, silakan coba lagi.")
    #selesai
