# Meminta input dari pengguna
jam_kerja = float(input("Masukkan jumlah jam kerja dalam seminggu: "))
tarif_per_jam = float(input("Masukkan tarif per jam: "))

# Mendefinisikan batas jam normal
jam_normal = 40
gaji = 0.0

# Menghitung gaji
if jam_kerja <= jam_normal:
    gaji = jam_kerja * tarif_per_jam
else:
    jam_lembur = jam_kerja - jam_normal
    gaji_lembur = jam_lembur * tarif_per_jam * 1.5
    gaji = (jam_normal * tarif_per_jam) + gaji_lembur

# Menampilkan hasil
print(f"Gaji total karyawan adalah: Rp.{gaji:,.2f}")
