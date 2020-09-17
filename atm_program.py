import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukkan pin Anda: "))
    trial = 0
    
    while id != int(atm.checkPin()) and trial < 3:
        id = int(input("Pin salah, silahkan coba lagi!: "))
        trial += 1

        if trial == 3:
            print("Anda sudah gagal 3x, ulangi lagi nanti")
            exit()
    while True:
        print("===============================")
        print("== Selamat datang di ATM RSC ==")
        print("===============================")
        menu_atm = ['Keluar','Cek Saldo','Debet','Simpan','Ganti Pin']
        i = 0
        for menu in menu_atm:
            print(str(i) + '. ' + menu)
            i += 1
        pilih_menu = int(input("Pilih menu: "))
        if pilih_menu == 0:
            print("Resi tercetak otomatis saat Anda keluar.\nHarap simpan tanda terima ini\nsebagai bukti transaksi Anda")
            print("No.Record:",random.randint(100000, 1000000))
            print("Tanggal:", datetime.datetime.now())
            print("Saldo akhir:", atm.checkBalance())
            print("Terimakasih telah menggunakan ATM RSC")
            exit()
        elif pilih_menu == 1:
            print("Saldo Anda : Rp.",atm.checkBalance() , "\n")
        elif pilih_menu == 2:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_debet = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? (y/n) "+ str(nominal) + " ")
            if verify_debet == "y":
                print("Saldo awal Anda adalah : Rp. ",atm.checkBalance())
            else:
                break
            if nominal < atm.checkBalance():
                atm.debetBalance(nominal)
                print("Debet berhasil!")
                print("Sisa saldo Anda adalah : Rp. ",atm.checkBalance())
            else:
                print("Maaf, saldo Anda tidak cukup!")
                print("Ayo tambah saldo Anda")
        elif pilih_menu == 3:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut ? (y/n) "+str(nominal) + " ")
            if verify_deposit == "y":
                atm.saveBalance(nominal)
                print("Saldo Anda sekarang adalah : Rp. ",atm.checkBalance())
            else:
                break

        elif pilih_menu == 4:
            verify_pin = int(input("Masukkan pin Anda: "))
            while verify_pin != atm.checkPin():
                print("Pin salah!")
                verify_pin = int(input("Masukkan ulang pin Anda: "))
            updated_pin = int(input("Silahkan masukkan pin baru: "))
            print("Pin Anda berhasil diganti!")
            verify_newpin = int(input("Coba masukkan pin baru: "))
            if verify_newpin == updated_pin:
                atm.pin = updated_pin
                print("Pin baru Anda suskes!")
            else:
                print("maaf, pin anda salah!")
        else:
            print("Maaf menu tidak tersedia!")
# by Achmad Fauzi
