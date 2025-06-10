class Buku:
    def __init__(self, judul, pengarang, jumlah):
        self.judul = judul
        self.pengarang = pengarang
        self.jumlah = jumlah

    def __str__(self):
        return f"{self.judul} oleh {self.pengarang} (Tersedia: {self.jumlah})"
    
    def to_dict(self):
        return {
            "judul": self.judul,
            "pengarang": self.pengarang,
            "jumlah": self.jumlah
        }