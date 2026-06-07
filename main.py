from repositories.koleksi_repo import KoleksiRepositoryImpl
from services.koleksi_services import ...
from views.koleksi_view import .....

def main():
    repo = KoleksiRepositoryImpl()
    service = KoleksiService(repo)
    view = KoleksiView(service)

    view.tampilkan_menu_utama()

if __name__ == "__main__":
    main()