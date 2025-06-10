from perpustakaan import Perpustakaan

def main():
    perpustakaan = Perpustakaan()

    while True:
        print("\nSistem Perpustakaan")
        print("1. Tambah Buku")
        print("2. Tambah Anggota")
        print("3. Tampilkan Buku Tersedia")
        print("4. Pinjam Buku")
        print("5. Kembalikan Buku")
        print("6. Hapus Buku")
        print("7. Tampilkan Anggota Peminjam") 
        print("8. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            judul = input("Masukkan judul buku: ")
            pengarang = input("Masukkan nama pengarang: ")
            jumlah = int(input("Masukkan jumlah buku: "))
            perpustakaan.tambah_buku(judul, pengarang, jumlah)

        elif pilihan == "2":
            nama = input("Masukkan nama anggota: ")
            id_anggota = input("Masukkan ID anggota: ")
            perpustakaan.tambah_anggota(nama, id_anggota)

        elif pilihan == "3":
            perpustakaan.tampilkan_buku_tersedia()

        elif pilihan == "4":
            id_anggota = input("Masukkan ID anggota: ")
            judul_buku = input("Masukkan judul buku yang ingin dipinjam: ")
            perpustakaan.pinjam_buku(id_anggota, judul_buku)

        elif pilihan == "5":
            id_anggota = input("Masukkan ID anggota: ")
            judul_buku = input("Masukkan judul buku yang ingin dikembalikan: ")
            perpustakaan.kembalikan_buku(id_anggota, judul_buku)

        elif pilihan == "6":
            judul = input("Masukkan judul buku yang ingin dihapus: ")
            perpustakaan.hapus_buku(judul)

        elif pilihan == "7":
            perpustakaan.tampilkan_anggota_peminjam()

        elif pilihan == "8":
            print("Terima kasih telah menggunakan sistem perpustakaan.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()