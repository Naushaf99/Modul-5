import namanimshift
print("Selamat Datang di Program Pembelian Keripik Kentang MASMISKUN");
str(input("Masukkan Nama Anda = "));
int(input("Masukkan Usia Anda = "));
str(input("Masukkan Nomor Telephone/HP yanng anda gunakan = "));
str(input("MAsukkan Nomor KTP anda = "));
print("================================================================");
print("Data Data yang anda Masukkan diatas sebagai bukti pertanggungjawaban anda dalam memesan melalui program kami")
print("============================================================================================================ \n")
print("berikut adalah daftar rasa keripik kentang MASMISKUN");
list = [" NO    Rasa Keripik Kentang  ",
        " 1     Sambal Balado         ",
        " 2     Keju   Susu           ",
        " 3     Jagung Bakar          ",
        " 4     Rumput Laut           "]
for a in list :
    print(a)
pilihan = int(input("Masukkan Nomor pilihan Rasa = "))

if pilihan == 1:
    print("Anda memilih rasa Sambal Balado")
elif pilihan > 1 and pilihan == 2:
    print("Anda memilih rasa Keju Susu")                      
elif pilihan > 2 and pilihan == 3:
    print("Anda memilih rasa Jagung Bakar")
elif pilihan > 3 and pilihan == 4:
    print("Anda memilih rasa Rumput Laut")
else:
    print("pilihan yang anda masukkan salah")

print("=======================================")

print("berikut daftar jumlah pemesanan beserta harga yang harus dibayar")
list = [" NO    Jumlah       Harga    ",
        " 1     1 buah       Rp 5000  ",
        " 2     5 buah       Rp 25000 ",
        " 3     1 lusin      Rp 60000",
        " 4     1 Box        Rp 720.000"]
for b in list :
    print(b)
minta = int(input("Masukkan pilihan jumlah yang ingin dipesan = "))

if minta == 1 :
    print("anda memesan sebanyak 1 buah dengan harga  Rp 5000 ")
elif minta > 1 and minta == 2 :
    print("Anda memesan sebanyak 5 buah dengan harga  Rp 25000 ")
elif minta > 2 and minta == 3 :
    print("Anda memesan sebanyak 1 lusin dengan harga Rp 60000 ")
elif minta > 3 and minta == 4 :
    print("Anda memesan sebanyak 1 Box dengan harga   Rp 720000 ")
else :
    print("Data yang anda masukkan salah")

       


print("Apakah Anda Puas Dengan Program Kami?")
print("1.Ya      2.Tidak")
jawab = int(input(" Masukkan Angka Tanggapan Anda "))
if jawab == 1:
    print("Terima Kasih atas Tanggapan Anda")
else:
    print("Mohon Maaf atas kekurangan program kami")

import perusahaan