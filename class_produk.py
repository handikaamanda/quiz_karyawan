class Produk:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def total(self):
        return self.harga * self.jumlah

    def diskon(self, total):
        if total > 5000:
            return total * 5 / 100
        return 0


jumlah_produk = int(input("Jumlah produk: "))
total_belanja = 0

for i in range(jumlah_produk):
    print("\nProduk ke-", i + 1)

    nama = input("Nama produk: ")
    harga = int(input("Harga: "))
    jumlah = int(input("Jumlah beli: "))

    produk = Produk(nama, harga, jumlah)
    print("Total produk: Rp", produk.total())
    total_belanja += produk.total()


diskon = produk.diskon(total_belanja)
total_bayar = total_belanja - diskon

print("\n=== HASIL PEMBELIAN ===")
print("Total Pembelian : Rp", total_belanja)
print("Diskon 5%       : Rp", diskon)
print("Total Bayar     : Rp", total_bayar)