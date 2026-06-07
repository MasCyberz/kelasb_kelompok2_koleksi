# service.py
# Nama: Sekar Hanny Keisha Azahra
# NIM: K3525041
# Bagian: Service - operasi tambah, hapus, tampil koleksi

from abc import ABC, abstractmethod


# Interface service (ISP - dipisah sesuai fungsi)

class ITambahService(ABC):
    @abstractmethod
    def tambah(self, koleksi):
        pass

class IHapusService(ABC):
    @abstractmethod
    def hapus(self, kode: str):
        pass

class ITampilService(ABC):
    @abstractmethod
    def tampil_semua(self):
        pass


# Implementasi service (SRP - satu class satu tugas)
# (DIP - data diterima dari luar, tidak dibuat sendiri)

class TambahService(ITambahService):
    def __init__(self, data_koleksi: list):
        self.data = data_koleksi

    def tambah(self, koleksi):
        self.data.append(koleksi)
        print("Data berhasil ditambahkan!")


class HapusService(IHapusService):
    def __init__(self, data_koleksi: list):
        self.data = data_koleksi

    def hapus(self, kode: str):
        sebelum = len(self.data)
        self.data[:] = [k for k in self.data if k.kode != kode]
        if len(self.data) < sebelum:
            print("Data berhasil dihapus!")
        else:
            print("Kode tidak ditemukan!")


class TampilService(ITampilService):
    def __init__(self, data_koleksi: list):
        self.data = data_koleksi

    def tampil_semua(self):
        if not self.data:
            print("Data kosong!")
            return
        for i, k in enumerate(self.data, 1):
            print(f"\nKoleksi {i}")
            k.tampil()
            
