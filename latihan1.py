nama = input("Masukkan Nama : ")
npm = int(input("Masukkan NPM : "))
prodi = input("Masukkan Prodi : ")
umur = int(input("Masukkan Umur : "))
tinggi = float(input("Masukkan Tinggi : "))

tugas = float(input("Masukkan Nilai Tugas : "))
uts = float(input("Masukkan Nilai UTS : "))
uas = float(input("Masukkan Nilai UAS : "))

nilai_akhir = (tugas + uts + uas) / 3

print("\n=== DATA MAHASISWA ===")
print(f"Nama   : {nama}")
print(f"Npm    : {npm}")
print(f"Prodi  : {prodi}")
print(f"Umur   : {umur} tahun")
print(f"Tinggi : {tinggi} cm")

print("\n=== NILAI ===")
print(f"Tugas       : {tugas}")
print(f"UTS         : {uts}")
print(f"UAS         : {uas}")
print(f"Nilai Akhir : {nilai_akhir : .2f}")

if nilai_akhir >= 75:
    print("Anda Lulus")
else:
    print("Anda Tidak Lulus")
    
