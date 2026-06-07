# ==========================================
# Nama Anggota : Amelia Pinasti Nugraheni 
# NIM          : K3525049
# Bagian Tugas : majalah.py
# ==========================================

from models.koleksi import Koleksi

class Majalah(Koleksi):
    # Class Majalah yang mewarisi Koleksi
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, edisi):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self.edisi = edisi

    def tampilkan_detail(self):
        # Mengisi fungsi dari induk dan menghasilkan data berbentuk dictionary
        return {
            "Jenis": "Majalah",
            "Kode": self.kode_koleksi,
            "Judul": self.judul,
            "Tahun": self.tahun_terbit,
            "Penerbit": self.penerbit,
            "Edisi": self.edisi
        }