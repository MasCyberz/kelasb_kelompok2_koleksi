# service.py
# Nama: Sekar Hanny Keisha Azahra
# NIM: K3525041
# Bagian: Service - operasi tambah, hapus, tampil koleksi

from models.buku import Buku
from models.jurnal import Jurnal
from models.majalah import Majalah


# Implementasi service (SRP - satu class satu tugas)
# (DIP - data diterima dari luar, tidak dibuat sendiri)

class KoleksiService:
    def __init__(self, repository):
        self.repository = repository

    def TambahBuku(self, kode_koleksi, judul, tahun_terbit, penerbit, pengarang):
        if self.repository.cari(kode_koleksi):
            raise ValueError("Kode koleksi sudah digunakan!")
        
        if not judul.strip():
            raise ValueError("Judul tidak boleh kosong")

        if not tahun_terbit.strip():
            raise ValueError("Tahun terbit tidak boleh kosong")

        if not penerbit.strip():
            raise ValueError("Penerbit tidak boleh kosong")

        if not pengarang.strip():
            raise ValueError("Pengarang tidak boleh kosong")
        
        buku = Buku(
            kode_koleksi,
            judul,
            tahun_terbit,
            penerbit,
            pengarang
        )
            
        self.repository.tambah(buku)

    def TambahMajalah(self, kode_koleksi, judul, tahun_terbit, penerbit, edisi):
        if self.repository.cari(kode_koleksi):
            raise ValueError("Kode koleksi sudah digunakan!")
        
        if not judul.strip():
            raise ValueError("Judul tidak boleh kosong")

        if not tahun_terbit.strip():
            raise ValueError("Tahun terbit tidak boleh kosong")

        if not penerbit.strip():
            raise ValueError("Penerbit tidak boleh kosong")

        if not edisi.strip():
            raise ValueError("Edisi tidak boleh kosong")
        
        majalah = Majalah(
            kode_koleksi,
            judul,
            tahun_terbit,
            penerbit,
            edisi
        )
            
        self.repository.tambah(majalah)

    def TambahJurnal(self, kode_koleksi, judul, tahun_terbit, penerbit, bidang_studi, impact_factor):
        if self.repository.cari(kode_koleksi):
            raise ValueError("Kode koleksi sudah digunakan!")
        
        if not judul.strip():
            raise ValueError("Judul tidak boleh kosong")

        if not tahun_terbit.strip():
            raise ValueError("Tahun terbit tidak boleh kosong")

        if not penerbit.strip():
            raise ValueError("Penerbit tidak boleh kosong")

        if not bidang_studi.strip():
            raise ValueError("Bidang Studi tidak boleh kosong")

        if not impact_factor.strip():
            raise ValueError("Impact Factor tidak boleh kosong")
        
        jurnal = Jurnal(
            kode_koleksi,
            judul,
            tahun_terbit,
            penerbit,
            bidang_studi,
            impact_factor
        )
            
        self.repository.tambah(jurnal)
            
    def hapus_koleksi(self, kode):
        if not kode.strip():
            raise ValueError("Kode tidak boleh kosong")
        
        if not self.repository.hapus(kode):
            raise ValueError("Kode tidak ditemukan")
                  
    def lihat_semua(self):
        data = self.repository.get_semua()
        
        if not data:
            raise ValueError("Data koleksi masih kosong")
    
        return data