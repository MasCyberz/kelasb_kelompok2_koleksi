#kode Sementara
# from .koleksi import Koleksi

class Buku(Koleksi):
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, pengarang):
        super().__init__(
            kode_koleksi,
            judul,
            tahun_terbit,
            penerbit
        )

        self.pengarang = pengarang

    def tampilkan_detail(self):
        return {
            "Jenis": "Buku",
            "Kode": self.kode_koleksi,
            "Judul": self.judul,
            "Tahun": self.tahun_terbit,
            "Pengarang": self.pengarang,
            "Penerbit": self.penerbit
        }
