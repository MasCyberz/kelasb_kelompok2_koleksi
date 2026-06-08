# ==========================================
# Nama Anggota : Bintang Fajar Khoiru Rizal
# NIM          : K3525001
# Bagian Tugas : buku.py
# ==========================================

from models.koleksi import Koleksi

class Buku(Koleksi):
    # Class Buku yang mewarisi Koleksi
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, pengarang):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self.pengarang = pengarang

    def tampilkan_detail(self):
        # Mengisi fungsi dari induk dan menghasilkan data berbentuk dictionary
        return {
            "Jenis": "Buku",
            "Kode": self.kode_koleksi,
            "Judul": self.judul,
            "Tahun": self.tahun_terbit,
            "Penerbit": self.penerbit,
            "Pengarang": self.pengarang
        }