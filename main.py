from repositories.koleksi_repo import KoleksiRepositoryImpl
from services.koleksi_services import KoleksiService
from views.koleksi_view import koleksiView

def main():
    repo = KoleksiRepositoryImpl()
    service = KoleksiService(repo)
    view = koleksiView(service)

    view.tampilan_menu_utama()

if __name__ == "__main__":
    main()