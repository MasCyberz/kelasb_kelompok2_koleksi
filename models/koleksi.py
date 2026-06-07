# ==========================================
# Nama Anggota : Amelia Pinasti Nugraheni 
# NIM          : K3525049
# Bagian Tugas : koleksi.py
# ==========================================

from abc import ABC, abstractmethod

class Koleksi(ABC):
    #Class Induk Abstrak untuk semua jenis media di perpustakaan.
    def __init__(self, kode_koleksi: str, judul: str, tahun_terbit: str, penerbit: str):
        self.kode_koleksi = kode_koleksi
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        self.penerbit = penerbit

    @abstractmethod
    def tampilkan_info(self):
        #Method abstrak yang wajib di-override oleh class anak (Buku, Jurnal, Majalah).
        pass