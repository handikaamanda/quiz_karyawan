class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        print(f"Nama Produk : {self.nama}\n Harga : Rp{self.harga:,}")
        

    def hitung_total(self, jumlah):
        return self.harga * jumlah

produk1 = Produk("Keyboard", 250000)
produk2 = Produk("Mouse", 150000)

produk1.tampilkan_info()
print(f"Total Pembelian {produk1.nama} : {produk1.hitung_total(2)}")
produk2.tampilkan_info()
print(f"Total Pembelian {produk2.nama} : {produk2.hitung_total(3)}")