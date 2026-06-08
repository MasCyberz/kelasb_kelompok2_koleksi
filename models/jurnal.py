# ==========================================
# Nama Anggota : Bintang Fajar Khoiru Rizal
# NIM          : K3525001
# Bagian Tugas : jurnal.py
# ==========================================

from models.koleksi import Koleksi

class Jurnal(Koleksi):
    # Class Jurnal yang mewarisi Koleksi
    def __init__(
        self,
        kode_koleksi,
        judul,
        tahun_terbit,
        penerbit,
        bidang_studi,
        impact_factor
    ):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self.bidang_studi = bidang_studi
        self.impact_factor = impact_factor

    def tampilkan_detail(self):
        # Mengisi fungsi dari induk dan menghasilkan data berbentuk dictionary
        return {
            "Jenis": "Jurnal",
            "Kode": self.kode_koleksi,
            "Judul": self.judul,
            "Tahun": self.tahun_terbit,
            "Penerbit": self.penerbit,
            "Bidang Studi": self.bidang_studi,
            "Impact Factor": self.impact_factor
        }
