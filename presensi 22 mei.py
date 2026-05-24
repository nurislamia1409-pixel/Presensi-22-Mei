# ==============================================
# PROGRAM DECISION TREE PRESENSI MAHASISWA
# Mata Kuliah : Kecerdasan Komputasional
# ==============================================

print("\n==========================================")
print("      PROGRAM PRESENSI MAHASISWA")
print("==========================================")

# Data mahasiswa
nama_mahasiswa = ["Rara", "Fikri", "Dinda", "Aldi", "Putra"]

kehadiran = [
    "Tinggi",
    "Rendah",
    "Tinggi",
    "Rendah",
    "Tinggi"
]

tugas = [
    "Lengkap",
    "Tidak Lengkap",
    "Tidak Lengkap",
    "Lengkap",
    "Lengkap"
]

# Variabel rekap
jumlah_aktif = 0
jumlah_tidak_aktif = 0

# Menampilkan data mahasiswa
for i in range(len(nama_mahasiswa)):

    # Menentukan status berdasarkan kehadiran
    if kehadiran[i] == "Tinggi":
        status = "Aktif"
        jumlah_aktif += 1
    else:
        status = "Tidak Aktif"
        jumlah_tidak_aktif += 1

    # Menentukan keterangan tambahan
    if kehadiran[i] == "Tinggi" and tugas[i] == "Lengkap":
        keterangan = "Mahasiswa Rajin"
    elif kehadiran[i] == "Tinggi" and tugas[i] == "Tidak Lengkap":
        keterangan = "Tugas Belum Maksimal"
    else:
        keterangan = "-"

    # Output data
    print("\n------------------------------------------")
    print("Nama        :", nama_mahasiswa[i])
    print("Kehadiran   :", kehadiran[i])
    print("Tugas       :", tugas[i])
    print("Status      :", status)
    print("Keterangan  :", keterangan)

# Rekap data
print("\n==========================================")
print("               REKAP DATA")
print("==========================================")

print("Mahasiswa Aktif        :", jumlah_aktif)
print("Mahasiswa Tidak Aktif  :", jumlah_tidak_aktif)

# ==============================================
# FITUR TAMBAHAN
# Input mahasiswa baru
# ==============================================

print("\n==========================================")
print("          TAMBAH DATA MAHASISWA")
print("==========================================")

pilihan = input("Ingin menambah data? (ya/tidak) : ")

if pilihan == "ya":

    nama_baru = input("Masukkan nama mahasiswa : ")
    hadir_baru = input("Masukkan kehadiran (Tinggi/Rendah) : ")
    tugas_baru = input("Masukkan tugas (Lengkap/Tidak Lengkap) : ")

    # Menentukan status mahasiswa baru
    if hadir_baru == "Tinggi":
        status_baru = "Aktif"
    else:
        status_baru = "Tidak Aktif"

    # Menentukan keterangan mahasiswa baru
    if hadir_baru == "Tinggi" and tugas_baru == "Lengkap":
        ket_baru = "Mahasiswa Rajin"
    elif hadir_baru == "Tinggi" and tugas_baru == "Tidak Lengkap":
        ket_baru = "Tugas Belum Maksimal"
    else:
        ket_baru = "-"

    # Menampilkan hasil data baru
    print("\n==========================================")
    print("           HASIL DATA BARU")
    print("==========================================")

    print("Nama        :", nama_baru)
    print("Kehadiran   :", hadir_baru)
    print("Tugas       :", tugas_baru)
    print("Status      :", status_baru)
    print("Keterangan  :", ket_baru)

else:
    print("\nProgram selesai.")

print("\n==========================================")
print("      TERIMA KASIH TELAH MENGGUNAKAN")
print("==========================================")