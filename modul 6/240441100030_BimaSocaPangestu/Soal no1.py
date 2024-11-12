# 1. membuat program manajemen data karyawan, Input data karyawan (minimal 5 data).
# List untuk menyimpan data karyawan
data_karyawan = []

# Fungsi untuk menambahkan data karyawan
def tambah_karyawan(nip, nama, alamat, departemen, jabatan):
    # Membuat tuple karyawan dengan data yang diberikan
    karyawan = (nip, nama, alamat, departemen, jabatan)
    # Menambahkan tuple karyawan ke dalam list data_karyawan
    data_karyawan.append(karyawan)
    print("Data karyawan berhasil ditambahkan.")

# Fungsi untuk menambahkan 5 data karyawan sekaligus
def tambah_banyak_karyawan():
    # Mengulangi proses input sebanyak 5 kali
    for i in range(5):
        print(f"Menambah Karyawan ke-{i+1}:")
        nip = input("NIP: ")
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        departemen = input("Departemen: ")
        jabatan = input("Jabatan: ")
        # Memanggil fungsi tambah_karyawan untuk menyimpan data
        tambah_karyawan(nip, nama, alamat, departemen, jabatan)

# Fungsi untuk menampilkan seluruh data karyawan
def tampilkan_karyawan():
    # Mengecek apakah ada data karyawan
    if not data_karyawan:
        print("Belum ada data karyawan.")
    else:
        print("Daftar Karyawan:")
        # Loop untuk menampilkan setiap karyawan
        for karyawan in data_karyawan:
            print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

# Fungsi untuk mencari karyawan berdasarkan atribut tertentu
def cari_karyawan(key, value):
    # List untuk menyimpan hasil pencarian
    hasil_cari = []
    # Mengubah nilai pencarian menjadi lowercase agar tidak case-sensitive
    value = value.lower()
    # Loop melalui setiap karyawan dalam data_karyawan
    for karyawan in data_karyawan:
        # Cek apakah atribut sesuai dengan nilai yang dicari
        if (key == "nip" and value in karyawan[0].lower()) or \
           (key == "nama" and value in karyawan[1].lower()) or \
           (key == "alamat" and value in karyawan[2].lower()) or \
           (key == "departemen" and value in karyawan[3].lower()) or \
           (key == "jabatan" and value in karyawan[4].lower()):
            # Jika cocok, tambahkan ke hasil pencarian
            hasil_cari.append(karyawan)
    # Mengembalikan hasil pencarian
    return hasil_cari

# Fungsi utama yang menampilkan menu dan memproses pilihan pengguna
def main():
    while True:
        # Menampilkan menu
        print("=== Menu Utama ===")
        print("1. --Tambah Data Karyawan--")
        print("2. --Tambah 5 Karyawan Sekaligus--")
        print("3. --Tampilkan Semua Karyawan--")
        print("4. --Cari Karyawan Berdasarkan Atribut--")
        print("5. --Keluar--")
        
        # Meminta input pilihan dari pengguna
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        # Memproses pilihan menu
        if pilihan == "1":
            # Meminta data karyawan dari pengguna
            nip = input("NIP: ")
            nama = input("Nama: ")
            alamat = input("Alamat: ")
            departemen = input("Departemen: ")
            jabatan = input("Jabatan: ")
            # Menambahkan karyawan menggunakan fungsi tambah_karyawan
            tambah_karyawan(nip, nama, alamat, departemen, jabatan)
        
        elif pilihan == "2":
            # Menambahkan 5 karyawan sekaligus
            tambah_banyak_karyawan()
        
        elif pilihan == "3":
            # Menampilkan semua data karyawan
            tampilkan_karyawan()
        
        elif pilihan == "4":
            # Meminta atribut dan nilai pencarian dari pengguna
            print("Pencarian Data Karyawan")
            print("Atribut pencarian: nip, nama, alamat, departemen, jabatan")
            key = input("Masukkan atribut yang dicari: ").lower()
            value = input("Masukkan nilai untuk pencarian: ")
            
            # Mencari karyawan menggunakan fungsi cari_karyawan
            hasil = cari_karyawan(key, value)
            # Menampilkan hasil pencarian
            if hasil:
                print("Hasil Pencarian:")
                for karyawan in hasil:
                    print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
            else:
                print("Data karyawan tidak ditemukan dengan kriteria tersebut.")
        
        elif pilihan == "5":
            # Keluar dari program
            print("Anda keluar dari program.")
            break
        
        else:
            # Jika input pilihan tidak valid
            print("Pilihan tidak valid, silakan pilih menu yang tersedia.")

# Menjalankan fungsi utama
main()





