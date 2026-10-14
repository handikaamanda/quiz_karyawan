from nama_produk import Produk

jumlah_produk = int(input("Masukkan Jumlah Produk : "))

for i in range(jumlah_produk):
    nama_produk = input("Masukkan Nama Produk : ")
    harga_produk = float(input("Masukkan Harga Produk : "))
    jumlah_beli = int(input("Masukkan Jumlah Beli : "))

    produks = Produk(nama_produk, harga_produk)
    produks.tampilkan_info
    print(f"Total Pembelian {produks.nama} : {produks.hitung_total(jumlah_beli)}")

#produk1 = Produk("Keyboard", 250000)
#produk2 = Produk("Mouse", 150000)

#produk1.tampilkan_info()
#print(f"Total Pembelian {produk1.nama} : {produk1.hitung_total(2)}")
#produk2.tampilkan_info()
#print(f"Total Pembelian {produk2.nama} : {produk2.hitung_total(3)}")
  