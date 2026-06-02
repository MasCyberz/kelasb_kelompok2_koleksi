class KoleksiRepository(ABC):
    @abstractmethod
    def tambah(self, koleksi: Koleksi) -> bool:
        pass

    @abstractmethod
    def hapus(self, kode: str) -> bool:
        pass

    @abstractmethod
    def get_semua(self) -> list:
        pass