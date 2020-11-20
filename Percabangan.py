import os
import time
from time import sleep

keju = [25]
coklat = [35]
bayar_keju = []
total_keju = []
potongan_keju = []
bayar_coklat = []
total_coklat = []
potongan_coklat = []
disk =[]

def clear_screen():
    os.system('cls')
def awal():
    clear_screen()
    print ("="*45)
    print ("       SELAMAT DATANG DI TOKO KUE SULE       ")
    print ("-"*45)
    print (" >>> Hari ini kami memiliki PROMO SPESIAL <<<")
    print ("  **Masukkan 0 untuk melihat PROMO SPESIAL** ")
    print ("="*45)
    print ("\n")
    print (" >> Silahkan pilih apa yang akan kamu beli <<")
    print ("="*45)
    print ("              MENU TOKO KUE SULE             ")
    print ("="*45)
    print ("| NO |   NAMA KUE   |   HARGA    | TERSEDIA |")
    print ("-"*45)
    print ("| 1. |   KUE KEJU   |  Rp. 6000  |  {} PCS  |".format(keju[0]))
    print ("| 2. |  KUE COKLAT  |  Rp. 3500  |  {} PCS  |".format(coklat[0]))
    print ("="*45)
    print ("*masukkan 3 untuk keluar")
    print ("\n")
    a = input ("Silahkan Masukkan nomor pilihan    : ")
    if a == "1":
        menu_keju()
    elif a == "2":
        menu_coklat()
    elif a == "0":
        promo()
    elif a == "3":
        exit()
    else :
        print ("Mohon maaf, hanya masukkan angka 0 - 3")
        print ("============ Terima Kasih ============")
        print ("\n")
        print ("Tunggu sesaat untuk kembali ke awal....")
        time.sleep (2)
        awal()

def menu_keju():
    a1 = int(input ("Berapa banyak KUE KEJU yang ingin anda beli : "))
    sisa = keju[0]
    if a1 <= sisa and a1 > 0:
        clear_screen()
        print ("="*49)
        print ("Apakah anda yakin tidak akan membeli KUE COKLAT?")
        print ("-"*49)
        print ("1. Ya")
        print ("2. Ingin memesannya juga")
        print ("="*49)
        c = input ("Silahkan Masukkan nomor pilihan : ")
        if c == "1":
            if a1 >= 4 and a1 <= 15:
                clear_screen()
                bayar_awal = a1 * 6000
                potongan = int(bayar_awal * 10/100)
                bayar = int(bayar_awal - potongan)
                print ("="*62)
                print ("                      >> TOKO KUE SULE <<                     ")
                print ("                      ____________________                    ")
                print ("                     |TOTAL  PEMBELANJAAN |                   ")
                print ("-"*62)
                print ("| NO |   KETERANGAN   |   SATUAN   | PEMBELIAN |    TOTAL    |")
                print ("-"*62)
                print ("| 1. |    KUE KEJU    |  Rp. 6000  |  {} PCS   |   Rp.{}  |".format(a1,bayar_awal))
                print ("| 2. |     DISKON     |      -     |  4-15 PCS |  -Rp.{}   |".format(potongan))
                print ("-"*62)
                print ("| +  |                TOTAL                    |   Rp.{}  |".format(bayar))
                print ("="*62)
                print ("\n")
                input ("Tekan enter jika sudah selesai....")
                print ("Tunggu sesaat...")
                time.sleep (3)
                kembali ()
            elif a1 >= 16 and a1 <= 25:
                clear_screen()
                bayar_awal = a1 * 6000
                potongan = int(bayar_awal * 15/100)
                bayar = int(bayar_awal - potongan)
                print ("="*62)
                print ("                      >> TOKO KUE SULE <<                     ")
                print ("                      ____________________                    ")
                print ("                     |TOTAL  PEMBELANJAAN |                   ")
                print ("-"*62)
                print ("| NO |   KETERANGAN   |   SATUAN   | PEMBELIAN |    TOTAL    |")
                print ("-"*62)
                print ("| 1. |    KUE KEJU    |  Rp. 6000  |  {} PCS   |   Rp.{}  |".format(a1,bayar_awal))
                print ("| 2. |     DISKON     |      -     | 16-25 PCS |  -Rp.{}   |".format(potongan))
                print ("-"*62)
                print ("| +  |                TOTAL                    |   Rp.{}  |".format(bayar))
                print ("="*62)
                print ("\n")
                input ("Tekan enter jika sudah selesai....")
                print ("Tunggu sesaat...")
                time.sleep (3)
                kembali ()
            else:
                clear_screen()
                bayar = (a1 * 6000)
                print ("="*62)
                print ("                      >> TOKO KUE SULE <<                     ")
                print ("                      ____________________                    ")
                print ("                     |TOTAL  PEMBELANJAAN |                   ")
                print ("-"*62)
                print ("| NO |   KETERANGAN   |   SATUAN   | PEMBELIAN |    TOTAL    |")
                print ("-"*62)
                print ("| 1. |    KUE KEJU    |  Rp. 6000  |  {} PCS   |   Rp.{}  |".format(a1,bayar))
                print ("-"*62)
                print ("| +  |                TOTAL                    |   Rp.{}  |".format(bayar))
                print ("="*62)
                print ("\n")
                input ("Tekan enter jika sudah selesai....")
                print ("Tunggu sesaat...")
                time.sleep (3)
                kembali ()
        elif c == "2":
            if a1 >= 4 and a1 <= 15:
                bayar_awal = a1 * 6000
                potongan = int(bayar_awal * 10/100)
                bayar = int(bayar_awal - potongan)
                total_keju.append(bayar_awal)
                potongan_keju.append(potongan)
                bayar_keju.append(bayar)
                disk.append(" 4-15")
            elif a1 >= 16 and a1 <= 25:
                bayar_awal = a1 * 6000
                potongan = int(bayar_awal * 15/100)
                bayar = int(bayar_awal - potongan)
                total_keju.append(bayar_awal)
                potongan_keju.append(potongan)
                bayar_keju.append(bayar)
                disk.append("16-25")
            else:
                bayar = (a1 * 6000)
                total_keju.append(bayar)
                potongan_keju.append(0000)
                bayar_keju.append(bayar)
                disk.append(a1)
            a2 = int(input ("Berapa banyak Anda ingin membeli KUE COKLATnya : "))
            clear_screen()
            sisa1 = coklat[0]
            if a2 <= sisa1 and a2 > 0:
                if a2 >= 5 and a2 <= 20:
                    bayar_awal = a2 * 3500
                    potongan = int(bayar_awal * 7/100)
                    bayar = int(bayar_awal - potongan)
                    total_coklat.append(bayar_awal)
                    potongan_coklat.append(potongan)
                    bayar_coklat.append(bayar)
                    disk.append(" 5-20")
                elif a2 >= 21 and a2 <= 35:
                    bayar_awal = a2 * 3500
                    potongan = int(bayar_awal * 12/100)
                    bayar = int(bayar_awal - potongan)
                    total_coklat.append(bayar_awal)
                    potongan_coklat.append(potongan)
                    bayar_coklat.append(bayar)
                    disk.append("21-35")
                else:
                    bayar = (a2 * 3500)
                    total_coklat.append(bayar)
                    potongan_coklat.append(0000)
                    bayar_coklat.append(bayar)
                    disk.append(a2)
            elif a2 < 1 :
                clear_screen()
                print("Mohon Maaf hanya bisa Memesan lebih dari 0 kue")
                print("Tunggu sesaat...")
                time.sleep (3)
                menu_keju()
            else:
                clear_screen()
                print ("Mohon maaf KUE COKLAT kami hanya tersisa : {} PCS".format(coklat[0]))
                print("Tunggu sesaat...")
                time.sleep (3)
                kembali()

            bayar = int (bayar_coklat[0] + bayar_keju[0])
            clear_screen()
            print ("="*62)
            print ("                      >> TOKO KUE SULE <<                     ")
            print ("                      ____________________                    ")
            print ("                     |TOTAL  PEMBELANJAAN |                   ")
            print ("-"*62)
            print ("| NO |   KETERANGAN   |   SATUAN   | PEMBELIAN |    TOTAL    ")
            print ("-"*62)
            print ("| 1. |    KUE KEJU    |  Rp. 6000  |  {} PCS   |   Rp.{}  ".format(a1,total_keju[0]))
            print ("| 2. |   KUE COKLAT   |  Rp. 3500  |  {} PCS   |   Rp.{}  ".format(a2,total_coklat[0]))
            print ("| 3. |     DISKON     |      -     | {} PCS |  -Rp.{}      ".format(disk[0],potongan_keju[0]))
            print ("| 4. |     DISKON     |      -     | {} PCS |  -Rp.{}      ".format(disk[1],potongan_coklat[0]))
            print ("-"*62)
            print ("| +  |                TOTAL                    |   Rp.{}  ".format(bayar))
            print ("="*62)
            print ("\n")

            baru = keju [0] - a2
            baru2 = coklat [0] - a1
            bayar_keju [0:1] = []
            total_keju [0:1] = []
            potongan_keju [0:1] = []
            bayar_coklat [0:1] = []
            total_coklat [0:1] = []
            potongan_coklat [0:1] = []
            keju [0:1] = []
            coklat [0:1] = []
            keju.append (baru)
            coklat.append (baru2)
            
            input ("Tekan enter jika sudah selesai....")
            print ("Tunggu sesaat...")
            time.sleep (3)
            kembali()
        else:
            print ("Mohon maaf, hanya masukkan angka 1 - 2")
            print ("============ Terima Kasih ============")
            print ("\n")
            print ("Tunggu sesaat untuk kembali ke awal....")
            time.sleep (2)
            menu_keju()
    elif a1 < 1 :
        clear_screen()
        print("Mohon Maaf hanya bisa Memesan lebih dari 0 kue")
        print("Tunggu sesaat...")
        time.sleep (3)
        menu_keju()
    else:
        clear_screen()
        print ("Mohon maaf KUE KEJU kami hanya tersisa : ", keju[0])
        print("Tunggu sesaat...")
        time.sleep (3)
        kembali()

def menu_coklat():
    a1 = int(input ("Berapa banyak KUE COKLAT yang ingin anda beli : "))
    sisa1 = coklat[0]
    if a1 <= sisa1 and a1 > 0:
        clear_screen()
        print ("="*46)
        print ("Apakah anda yakin tidak akan membeli KUE KEJU?")
        print ("-"*46)
        print ("1. Ya")
        print ("2. Saya ingin memesannya juga")
        print ("="*46)
        c = input ("Silahkan Masukkan nomor pilihan : ")
        if c == "1":
            clear_screen()
            if a1 >= 5 and a1 <= 20:
                clear_screen()
                bayar_awal = a1 * 3500
                potongan = int(bayar_awal * 7/100)
                bayar = int(bayar_awal - potongan)
                print ("="*62)
                print ("                      >> TOKO KUE SULE <<                     ")
                print ("                      ____________________                    ")
                print ("                     |TOTAL  PEMBELANJAAN |                   ")
                print ("-"*62)
                print ("| NO |   KETERANGAN   |   SATUAN   | PEMBELIAN |    TOTAL    |")
                print ("-"*62)
                print ("| 1. |   KUE COKLAT   |  Rp. 3500  |  {} PCS   |   Rp.{}  |".format(a1,bayar_awal))
                print ("| 2. |     DISKON     |      -     |  5-20 PCS |  -Rp.{}   |".format(potongan))
                print ("-"*62)
                print ("| +  |                TOTAL                    |   Rp.{}  |".format(bayar))
                print ("="*62)
                print ("\n")
                input ("Tekan enter jika sudah selesai....")
                print ("Tunggu sesaat...")
                time.sleep (3)
                kembali ()
            elif a1 >= 21 and a1 <= 35:
                clear_screen()
                bayar_awal = a1 * 3500
                potongan = int(bayar_awal * 12/100)
                bayar = int(bayar_awal - potongan)
                print ("="*62)
                print ("                      >> TOKO KUE SULE <<                     ")
                print ("                      ____________________                    ")
                print ("                     |TOTAL  PEMBELANJAAN |                   ")
                print ("-"*62)
                print ("| NO |   KETERANGAN   |   SATUAN   | PEMBELIAN |    TOTAL    |")
                print ("-"*62)
                print ("| 1. |   KUE COKLAT   |  Rp. 3500  |  {} PCS   |   Rp.{}  |".format(a1,bayar_awal))
                print ("| 2. |     DISKON     |      -     | 21-35 PCS |  -Rp.{}   |".format(potongan))
                print ("-"*62)
                print ("| +  |                TOTAL                    |   Rp.{}  |".format(bayar))
                print ("="*62)
                print ("\n")
                input ("Tekan enter jika sudah selesai....")
                print ("Tunggu sesaat...")
                time.sleep (3)
                kembali ()
            else:
                bayar = (a1 * 3500)
                print ("="*62)
                print ("                      >> TOKO KUE SULE <<                     ")
                print ("                      ____________________                    ")
                print ("                     |TOTAL  PEMBELANJAAN |                   ")
                print ("-"*62)
                print ("| NO |   KETERANGAN   |   SATUAN   | PEMBELIAN |    TOTAL    |")
                print ("-"*62)
                print ("| 1. |   KUE COKALT   |  Rp. 3500  |  {} PCS   |   Rp.{}  |".format(a1,bayar))
                print ("-"*62)
                print ("| +  |                TOTAL                    |   Rp.{}  |".format(bayar))
                print ("="*62)
                print ("\n")
                input ("Tekan enter jika sudah selesai....")
                print ("Tunggu sesaat...")
                time.sleep (3)
                kembali ()
        
        elif c == "2":
            clear_screen()
            if a1 >= 5 and a1 <= 20:
                bayar_awal = a1 * 3500
                potongan = int(bayar_awal * 7/100)
                bayar = int(bayar_awal - potongan)
                total_coklat.append(bayar_awal)
                potongan_coklat.append(potongan)
                bayar_coklat.append(bayar)
                disk.append(" 5-20")
            elif a1 >= 21 and a1 <= 35:
                bayar_awal = a1 * 3500
                potongan = int(bayar_awal * 12/100)
                bayar = int(bayar_awal - potongan)
                total_coklat.append(bayar_awal)
                potongan_coklat.append(potongan)
                bayar_coklat.append(bayar)
                disk.append("21-35")
            else:
                bayar = (a1 * 3500)
                total_coklat.append(bayar)
                potongan_coklat.append(0000)
                bayar_coklat.append(bayar)
                disk.append(a1)
            a2 = int(input ("Berapa banyak Anda ingin membeli KUE KEJUnya : "))
            clear_screen()
            sisa1 = keju[0]
            if a2 <= sisa1 and a2 > 0:
                if a2 >= 4 and a2 <= 15:
                    bayar_awal = a2 * 6000
                    potongan = int(bayar_awal * 10/100)
                    bayar = int(bayar_awal - potongan)
                    total_keju.append(bayar_awal)
                    potongan_keju.append(potongan)
                    bayar_keju.append(bayar)
                    disk.append(" 4-15")
                elif a2 >= 16 and a2 <= 25:
                    bayar_awal = a2 * 6000
                    potongan = int(bayar_awal * 15/100)
                    bayar = int(bayar_awal - potongan)
                    total_keju.append(bayar_awal)
                    potongan_keju.append(potongan)
                    bayar_keju.append(bayar)
                    disk.append("16-25")
                else:
                    bayar = (a2 * 6000)
                    total_keju.append(bayar)
                    potongan_keju.append(0000)
                    bayar_keju.append(bayar)
                    disk.append(a2)
            elif a2 < 1 :
                clear_screen()
                print("Mohon Maaf hanya bisa Memesan lebih dari 0 kue")
                print("Tunggu sesaat...")
                time.sleep (3)
                menu_coklat()

            else:
                clear_screen()
                print ("Mohon maaf KUE KEJU kami hanya tersisa : {} PCS".format(keju[0]))
                print("Tunggu sesaat...")
                time.sleep (3)
                kembali()            
            bayar = int (bayar_coklat[0] + bayar_keju[0])
            clear_screen()
            print ("="*62)
            print ("                      >> TOKO KUE SULE <<                     ")
            print ("                      ____________________                    ")
            print ("                     |TOTAL  PEMBELANJAAN |                   ")
            print ("-"*62)
            print ("| NO |   KETERANGAN   |   SATUAN   | PEMBELIAN |    TOTAL    ")
            print ("-"*62)
            print ("| 1. |   KUE COKLAT   |  Rp. 3500  |  {} PCS   |   Rp.{}  ".format(a1,total_coklat[0]))
            print ("| 2. |    KUE KEJU    |  Rp. 6000  |  {} PCS   |   Rp.{}  ".format(a2,total_keju[0]))
            print ("| 3. |     DISKON     |      -     | {} PCS |  -Rp.{}      ".format(disk[0],potongan_keju[0]))
            print ("| 4. |     DISKON     |      -     | {} PCS |  -Rp.{}      ".format(disk[1],potongan_coklat[0]))
            print ("-"*62)
            print ("| +  |                TOTAL                    |   Rp.{}  ".format(bayar))
            print ("="*62)
            print ("\n")

            baru = keju [0] - a2
            baru2 = coklat [0] - a1
            bayar_keju [0:1] = []
            total_keju [0:1] = []
            potongan_keju [0:1] = []
            bayar_coklat [0:1] = []
            total_coklat [0:1] = []
            potongan_coklat [0:1] = []
            keju [0:1] = []
            coklat [0:1] = []
            keju.append (baru)
            coklat.append (baru2)

            input ("Tekan enter jika sudah selesai....")
            print ("Tunggu sesaat...")
            time.sleep (3)
            kembali()
        else:
            print ("Mohon maaf, hanya masukkan angka 1 - 2")
            print ("============ Terima Kasih ============")
            print ("\n")
            print ("Tunggu sesaat untuk kembali ke awal....")
            time.sleep (2)
            menu_coklat()
    elif a1 < 1:
        clear_screen()
        print("Mohon Maaf hanya bisa Memesan lebih dari 0 kue")
        print("Tunggu sesaat...")
        time.sleep (3)
        menu_coklat()


    else:
        clear_screen()
        print ("Mohon maaf KUE COKLAT kami hanya tersisa : {} PCS".format(coklat[0]))
        print("Tunggu sesaat...")
        time.sleep (3)
        kembali()

def kembali():
    clear_screen()
    print ("Apakah anda ingin tetap berbelanja?")
    print ("1. Ya")
    print ("2. Tidak")
    a=input ("Pilihan : ")
    if a == "1":
        awal()
    elif a == "2":
        exit()
    else:
        print("Hanya masukkan angka 1-2")
        print("Tunggu sesaat...")
        time.sleep (3)
        kembali() 

def promo():
    clear_screen()
    print ("="*45)
    print ("|        PROMO SPESIAL TOKO KUE SULE        |")
    print ("-"*45)
    print ("|            >>> PRIKITIW 1A <<<            |")
    print ("|      BELI 5-20 KUE COKLAT DISKON 7%       |")
    print ("|                   ~~~                     |")
    print ("|            >>> PRIKITIW 2A <<<            |")
    print ("|      BELI 21-35 KUE COKLAT DISKON 12%     |")
    print ("|                   ~~~                     |")
    print ("|            >>> PRIKITIW 1B <<<            |")
    print ("|       BELI 4-15 KUE KEJU DISKON 10%       |")
    print ("|                   ~~~                     |")
    print ("|            >>> PRIKITIW 2B <<<            |")
    print ("|       BELI 16-25 KUE KEJU DISKON 15%      |")
    print ("="*45)
    print ("\n")
    input ("Tekan enter untuk kembali....")
    print ("Tunggu sesaat....")
    time.sleep (2)
    awal()

awal()
