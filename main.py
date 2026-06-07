from repositories.koleksi_repo import KoleksiRepositoryImpl
from services.koleksi_services import KoleksiService
from views.koleksi_viiew import KoleksiView

def main():
    repo = KoleksiRepositoryImpl()
    service = KoleksiService(repo)
    view = KoleksiView(service)

    view.tampilkan_menu_utama()

if __name__ == "__main__":
    main()