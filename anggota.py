class Anggota:
    def __init__(self, nama, id_anggota, buku_dipinjam=None):
        self.nama = nama
        self.id_anggota = id_anggota
        self.buku_dipinjam = buku_dipinjam if buku_dipinjam is not None else []

    def pinjam_buku(self, buku):
        if buku.jumlah > 0:
            self.buku_dipinjam.append(buku.judul) 
            buku.jumlah -= 1
            print(f"{buku.judul} berhasil dipinjam oleh {self.nama}.")
            return True
        else:
            print(f"Maaf, {buku.judul} tidak tersedia.")
            return False

    def kembalikan_buku(self, buku):
        if buku.judul in self.buku_dipinjam:
            self.buku_dipinjam.remove(buku.judul)
            buku.jumlah += 1
            print(f"{buku.judul} berhasil dikembalikan oleh {self.nama}.")
            return True
        else:
            print(f"{self.nama} tidak meminjam {buku.judul}.")
            return False

    def tampilkan_buku_dipinjam(self):
        if self.buku_dipinjam:
            print(f"{self.nama} sedang meminjam buku berikut:")
            for judul_buku in self.buku_dipinjam:
                print(f"- {judul_buku}")
        else:
            print(f"{self.nama} tidak sedang meminjam buku apapun.")

    def to_dict(self):
        return {
            "nama": self.nama,
            "id_anggota": self.id_anggota,
            "buku_dipinjam": self.buku_dipinjam
        }