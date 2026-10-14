
from karyawan import Karyawan

jumlah = int(input("Jumlah Karyawan: "))

for i in range(jumlah):
    print("\nKaryawan ke-", i + 1)

    nama = input("Nama Karyawan : ")
    jabatan = input("Jabatan       : ")
    gaji = int(input("Gaji Harian   : "))
    hari = int(input("Hari Kerja    : "))

    karyawan = Karyawan(nama, jabatan, gaji)

    print("\n=== SLIP GAJI ===")
    karyawan.tampilkan_data()

    print("Hari Kerja     :", hari)
    print("Gaji Pokok     : Rp", karyawan.hitung_gaji(hari))
    print("Bonus          : Rp", karyawan.hitung_bonus(hari))
    print("Total Gaji     : Rp", karyawan.total_gaji(hari))
