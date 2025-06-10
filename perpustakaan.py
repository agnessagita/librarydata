import json
import os
from buku import Buku
from anggota import Anggota

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []
        self.daftar_anggota = []
        self.load_data()

    def tambah_buku(self, judul, pengarang, jumlah):
        buku_baru = Buku(judul, pengarang, jumlah)
        self.daftar_buku.append(buku_baru)
        self.save_data()
        print(f"Buku '{judul}' telah ditambahkan ke perpustakaan.")

    def hapus_buku(self, judul):
        buku = self.cari_buku(judul)
        if buku:
            # Cek apakah buku sedang dipinjam
            for anggota in self.daftar_anggota:
                if buku.judul in anggota.buku_dipinjam:
                    print(f"Gagal menghapus. Buku '{judul}' sedang dipinjam oleh {anggota.nama}.")
                    return False
            
            self.daftar_buku.remove(buku)
            self.save_data()
            print(f"Buku '{judul}' berhasil dihapus.")
            return True
        else:
            print(f"Buku '{judul}' tidak ditemkan.")
            return False

    def tambah_anggota(self, nama, id_anggota):
        anggota_baru = Anggota(nama, id_anggota)
        self.daftar_anggota.append(anggota_baru)
        self.save_data()
        print(f"Anggota '{nama}' telah terdaftar.")

    def tampilkan_buku_tersedia(self):
        if self.daftar_buku:
            print("Buku yang tersedia di perpustakaan:")
            for buku in self.daftar_buku:
                print(buku)
        else:
            print("Tidak ada buku yang tersedia di perpustakaan.")

    def cari_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul.lower():
                return buku
        return None

    def cari_anggota(self, id_anggota):
        for anggota in self.daftar_anggota:
            if anggota.id_anggota == id_anggota:
                return anggota
        return None

    def pinjam_buku(self, id_anggota, judul_buku):
        anggota = self.cari_anggota(id_anggota)
        buku = self.cari_buku(judul_buku)
        
        if not anggota or not buku:
            print("Anggota atau buku tidak ditemukan.")
            return False
        
        if anggota.pinjam_buku(buku):
            self.save_data()
            return True
        return False

    def tampilkan_anggota_peminjam(self):
        print("\nDaftar Anggota yang Meminjam Buku:")
        ada_peminjam = False
        
        for anggota in self.daftar_anggota:
            if anggota.buku_dipinjam:
                ada_peminjam = True
                print(f"\nNama: {anggota.nama}")
                print(f"ID Anggota: {anggota.id_anggota}")
                print("Buku yang dipinjam:")
                for judul_buku in anggota.buku_dipinjam:
                    buku = self.cari_buku(judul_buku)
                    if buku:
                        print(f"- {buku.judul} oleh {buku.pengarang}")
        
        if not ada_peminjam:
            print("Tidak ada anggota yang meminjam buku saat ini.")

    def kembalikan_buku(self, id_anggota, judul_buku):
        anggota = self.cari_anggota(id_anggota)
        buku = self.cari_buku(judul_buku)
        
        if not anggota or not buku:
            print("Anggota atau buku tidak ditemukan.")
            return False
        
        if anggota.kembalikan_buku(buku):
            self.save_data()
            return True
        return False

    def save_data(self):
        data = {
            "buku": [buku.to_dict() for buku in self.daftar_buku],
            "anggota": [anggota.to_dict() for anggota in self.daftar_anggota]
        }
        with open("perpustakaan_data.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if os.path.exists("perpustakaan_data.json"):
            with open("perpustakaan_data.json", "r") as file:
                data = json.load(file)
                
                
                self.daftar_buku = [Buku(**buku) for buku in data["buku"]]
                
                
                self.daftar_anggota = []
                for anggota_data in data["anggota"]:
                    anggota = Anggota(
                        nama=anggota_data["nama"],
                        id_anggota=anggota_data["id_anggota"],
                        buku_dipinjam=anggota_data.get("buku_dipinjam", [])
                    )
                    self.daftar_anggota.append(anggota)