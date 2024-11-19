# Inisialisasi dictionary untuk menyimpan data siswa
kelas_siswa = {}

def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    kelas = input("Masukkan kelas: ")
    asal_sekolah = input("Masukkan asal sekolah: ")

    if kelas not in kelas_siswa:
        kelas_siswa[kelas] = set()  # Membuat set baru jika kelas belum ada
    if len(kelas_siswa[kelas]) < 3:  # Memastikan tidak lebih dari 3 siswa per kelas
        kelas_siswa[kelas].add((nama, asal_sekolah))  # Menambahkan tuple (nama, asal_sekolah)
        print(f"Siswa {nama} ditambahkan ke kelas {kelas}.")
    else:
        print(f"Kelas {kelas} sudah penuh. Membuka kelas baru.")
        tambah_siswa()  # Meminta input lagi untuk menambahkan ke kelas baru

def tampilkan_siswa():
    if not kelas_siswa:
        print("Tidak ada data siswa.")
        return
    for kelas, siswa in kelas_siswa.items():
        print(f"Kelas {kelas}:")
        for nama, asal_sekolah in siswa:
            print(f" - Nama: {nama}, Asal Sekolah: {asal_sekolah}")

def hapus_siswa():
    nama = input("Masukkan nama siswa yang ingin dihapus: ")
    kelas = input("Masukkan kelas siswa tersebut: ")
    
    if kelas in kelas_siswa and any(nama in s for s in kelas_siswa[kelas]):
        kelas_siswa[kelas] = {s for s in kelas_siswa[kelas] if s[0] != nama}
        print(f"Siswa {nama} dihapus dari kelas {kelas}.")
    else:
        print(f"Siswa {nama} tidak ditemukan di kelas {kelas}.")

def update_asal_sekolah():
    nama = input("Masukkan nama siswa yang ingin diperbarui: ")
    kelas = input("Masukkan kelas siswa tersebut: ")
    asal_sekolah_baru = input("Masukkan asal sekolah baru: ")

    if kelas in kelas_siswa:
        for siswa in list(kelas_siswa[kelas]):
            if siswa[0] == nama:
                kelas_siswa[kelas].remove(siswa)
                kelas_siswa[kelas].add((nama, asal_sekolah_baru))
                print(f"Asal sekolah {nama} diperbarui menjadi {asal_sekolah_baru}.")
                return
    print(f"Siswa {nama} tidak ditemukan di kelas {kelas}.")

def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Tambah Siswa")
        print("2. Tampilkan Siswa")
        print("3. Hapus Siswa")
        print("4. Update Asal Sekolah")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tambah_siswa()
        elif pilihan == '2':
            tampilkan_siswa()
        elif pilihan == '3':
            hapus_siswa()
        elif pilihan == '4':
            update_asal_sekolah()
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
menu()