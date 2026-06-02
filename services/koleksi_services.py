# service.py
# Nama: Sekar Hanny Keisha Azahra
# NIM: K3525041
# Bagian: Service - operasi tambah, hapus, tampil koleksi

from abc import ABC, abstractmethod


# Abstract class Koleksi (superclass)
class Koleksi(ABC):
    def __init__(self, kode, judul, tahun):
        self.kode = kode
        self.judul = judul
        self.tahun = tahun

    @abstractmethod
    def tampil(self):
        pass


# Subclass Buku
class Buku(Koleksi):
    def __init__(self, kode, judul, tahun, pengarang, penerbit):
        super().__init__(kode, judul, tahun)
        self.pengarang = pengarang
        self.penerbit = penerbit

    def tampil(self):
        print("\nJenis    : Buku")
        print("Kode     :", self.kode)
        print("Judul    :", self.judul)
        print("Tahun    :", self.tahun)
        print("Pengarang:", self.pengarang)
        print("Penerbit :", self.penerbit)


# Subclass Majalah
class Majalah(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, edisi):
        super().__init__(kode, judul, tahun)
        self.penerbit = penerbit
        self.edisi = edisi

    def tampil(self):
        print("\nJenis    : Majalah")
        print("Kode     :", self.kode)
        print("Judul    :", self.judul)
        print("Tahun    :", self.tahun)
        print("Penerbit :", self.penerbit)
        print("Edisi    :", self.edisi)


# Subclass Jurnal
class Jurnal(Koleksi):
    def __init__(self, kode, judul, tahun, penerbit, bidang, impact):
        super().__init__(kode, judul, tahun)
        self.penerbit = penerbit
        self.bidang = bidang
        self.impact = impact

    def tampil(self):
        print("\nJenis    : Jurnal")
        print("Kode     :", self.kode)
        print("Judul    :", self.judul)
        print("Tahun    :", self.tahun)
        print("Penerbit :", self.penerbit)
        print("Bidang   :", self.bidang)
        print("Impact   :", self.impact)


# -----------------------------------------------
# Interface service (ISP - dipisah sesuai fungsi)
# -----------------------------------------------

class ITambahService(ABC):
    @abstractmethod
    def tambah(self, koleksi: Koleksi):
        pass

class IHapusService(ABC):
    @abstractmethod
    def hapus(self, kode: str):
        pass

class ITampilService(ABC):
    @abstractmethod
    def tampil_semua(self):
        pass


# -----------------------------------------------
# Implementasi service (SRP - satu class satu tugas)
# -----------------------------------------------

class TambahService(ITambahService):
    def __init__(self, data_koleksi: list):
        self.data = data_koleksi

    def tambah(self, koleksi: Koleksi):
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


# -----------------------------------------------
# Main program
# -----------------------------------------------

data_koleksi = []
tambah_service = TambahService(data_koleksi)
hapus_service  = HapusService(data_koleksi)
tampil_service = TampilService(data_koleksi)


def tambah_data():
    print("\n1. Buku\n2. Majalah\n3. Jurnal")
    jenis = input("Pilih jenis: ")
    kode  = input("Kode: ")
    judul = input("Judul: ")
    tahun = input("Tahun: ")

    if jenis == "1":
        pengarang = input("Pengarang: ")
        penerbit  = input("Penerbit: ")
        tambah_service.tambah(Buku(kode, judul, tahun, pengarang, penerbit))
    elif jenis == "2":
        penerbit = input("Penerbit: ")
        edisi    = input("Edisi: ")
        tambah_service.tambah(Majalah(kode, judul, tahun, penerbit, edisi))
    elif jenis == "3":
        penerbit = input("Penerbit: ")
        bidang   = input("Bidang: ")
        impact   = input("Impact Factor: ")
        tambah_service.tambah(Jurnal(kode, judul, tahun, penerbit, bidang, impact))
    else:
        print("Jenis tidak valid!")


def hapus_data():
    kode = input("Masukkan kode: ")
    hapus_service.hapus(kode)


def tampil_data():
    tampil_service.tampil_semua()


def menu():
    while True:
        print("\n=== MENU PROGRAM ===")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Tampilkan Data")
        print("4. Keluar")
        pilih = input("Pilih: ")

        if pilih == "1":
            tambah_data()
        elif pilih == "2":
            hapus_data()
        elif pilih == "3":
            tampil_data()
        elif pilih == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan salah!")

menu()