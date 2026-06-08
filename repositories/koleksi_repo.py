# Analisis:
# Nama : Ken Gayuh Nusa Islami
# NIM  : K3525031
# Bagian tugas : koleksi_repo


from repositories.interface import KoleksiRepository
from models.koleksi import Koleksi


class KoleksiRepositoryImpl(KoleksiRepository):
    def __init__(self):
        self._data = []

    def tambah(self, koleksi: Koleksi):
        for existing in self._data:
            if existing.kode_koleksi == koleksi.kode_koleksi:
                print("Error: Kode {} sudah ada!".format(koleksi.kode_koleksi))
                return False
            
        self._data.append(koleksi)
        return True

    def hapus(self, kode: str):
        for i, koleksi in enumerate(self._data):
            if koleksi.kode_koleksi == kode:
                self._data.pop(i)
                return True
            
        print("Error: Kode {} tidak ditemukan!".format(kode))
        return False


    def get_semua(self):
        return self._data[:]
