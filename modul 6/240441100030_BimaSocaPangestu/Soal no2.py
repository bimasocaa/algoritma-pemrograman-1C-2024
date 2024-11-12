# 2. membuat sebuah program sistem peminjaman buku di perpustakaan 
# List untuk menyimpan data peminjaman buku
data_peminjaman = []

# Fungsi untuk menambahkan data peminjaman baru
def tambah_peminjaman():
    # Meminta input ID peminjaman dari pengguna
    id_peminjaman = input("ID Peminjaman: ")

    # Mengecek apakah ID peminjaman sudah ada dalam data
    for peminjaman in data_peminjaman:
        if peminjaman['id_peminjaman'] == id_peminjaman:
            print("ID peminjaman sudah ada. Gunakan ID lain.")
            return  # Menghentikan fungsi jika ID sudah ada

    # Meminta input nama peminjam, judul buku, dan tanggal peminjaman
    nama_peminjam = input("Nama Peminjam: ")
    judul_buku = input("Judul Buku: ")
    tanggal_peminjaman = input("Tanggal Peminjaman (DD-MM-YYYY): ")

    # Membuat dictionary untuk menyimpan data peminjaman
    peminjaman = {
        'id_peminjaman': id_peminjaman,
        'nama_peminjam': nama_peminjam,
        'judul_buku': judul_buku,
        'tanggal_peminjaman': tanggal_peminjaman
    }

    # Menambahkan data peminjaman ke dalam list `data_peminjaman`
    data_peminjaman.append(peminjaman)
    print("Data peminjaman berhasil ditambahkan.")

# Fungsi untuk menampilkan semua data peminjaman yang ada
def tampilkan_peminjaman():
    # Mengecek apakah list `data_peminjaman` kosong
    if not data_peminjaman:
        print("Belum ada data peminjaman.")
    else:
        # Menampilkan header daftar peminjaman buku
        print("Daftar Peminjaman Buku:")
        # Loop untuk menampilkan setiap data peminjaman
        for peminjaman in data_peminjaman:
            # Mengambil data dari dictionary dan menampilkannya
            print(f"ID: {peminjaman['id_peminjaman']}, Nama Peminjam: {peminjaman['nama_peminjam']}, "
                  f"Judul Buku: {peminjaman['judul_buku']}, Tanggal: {peminjaman['tanggal_peminjaman']}")

# Fungsi untuk memperbarui data peminjaman yang ada
def update_peminjaman():
    # Meminta input ID peminjaman yang akan diperbarui
    id_peminjaman = input("Masukkan ID peminjaman yang akan diupdate: ")

    # Mencari data peminjaman berdasarkan ID yang diberikan
    for peminjaman in data_peminjaman:
        if peminjaman['id_peminjaman'] == id_peminjaman:
            # Meminta input data baru dari pengguna
            print("Masukkan data baru:")
            nama_peminjam = input("Nama Peminjam: ")
            judul_buku = input("Judul Buku: ")
            tanggal_peminjaman = input("Tanggal Peminjaman (DD-MM-YYYY): ")

            # Memperbarui data peminjaman dengan data baru
            peminjaman['nama_peminjam'] = nama_peminjam
            peminjaman['judul_buku'] = judul_buku
            peminjaman['tanggal_peminjaman'] = tanggal_peminjaman
            print("Data peminjaman berhasil diperbarui.")
            return  # Keluar dari fungsi setelah data diperbarui

    # Menampilkan pesan jika ID peminjaman tidak ditemukan
    print("ID peminjaman tidak ditemukan.")

# Fungsi untuk menghapus data peminjaman berdasarkan ID
def hapus_peminjaman():
    # Meminta input ID peminjaman yang akan dihapus
    id_peminjaman = input("Masukkan ID peminjaman yang akan dihapus: ")

    # Mencari data peminjaman berdasarkan ID yang diberikan
    for peminjaman in data_peminjaman:
        if peminjaman['id_peminjaman'] == id_peminjaman:
            # Menghapus data peminjaman dari list
            data_peminjaman.remove(peminjaman)
            print("Data peminjaman berhasil dihapus.")
            return  # Keluar dari fungsi setelah data dihapus

    # Menampilkan pesan jika ID peminjaman tidak ditemukan
    print("ID peminjaman tidak ditemukan.")

# Fungsi utama yang berisi menu utama program
def main():
    # Loop untuk menampilkan menu dan menerima pilihan dari pengguna
    while True:
        print("=== Menu Sistem Peminjaman Buku ===")
        print("1. Tambah Peminjaman")
        print("2. Tampilkan Semua Peminjaman")
        print("3. Update Peminjaman")
        print("4. Hapus Peminjaman")
        print("5. Keluar")

        # Meminta input pilihan menu dari pengguna
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        # Memeriksa pilihan pengguna dan memanggil fungsi yang sesuai
        if pilihan == "1":
            tambah_peminjaman()

        elif pilihan == "2":
            tampilkan_peminjaman()

        elif pilihan == "3":
            update_peminjaman()

        elif pilihan == "4":
            hapus_peminjaman()

        elif pilihan == "5":
            # Keluar dari program
            print("Anda keluar dari program.")
            break

        else:
            # Menampilkan pesan jika pilihan tidak valid
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# Memanggil fungsi utama untuk memulai program
main()
