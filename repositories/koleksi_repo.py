# Analisis:
# Nama : Ken Gayuh Nusa Islami
# NIM  : K3525031

from .interface import KoleksiRepository
from models.koleksi import 


class KoleksiRepositoryImpl(KoleksiRepository):
    def __init__(self):
        self._data = []

    def tambah(self, koleksi):
        for existing in self._data:
            if existing.kode == koleksi.kode:
                print("Error: Kode {} sudah ada!".format(koleksi.kode))
                return False
        self._data.append(koleksi)
        return True

    def hapus(self, kode):
        for i, koleksi in enumerate(self._data):
            if koleksi.kode == kode:
                self._data.pop(i)
                return True
        print("Error: Kode {} tidak ditemukan!".format(kode))
        return False

    def get_semua(self):
        return self._data[:]
