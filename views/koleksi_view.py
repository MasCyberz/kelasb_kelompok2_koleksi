class koleksiView:
    def __init__(self, service):
        self.service = service
    
    def konfirmasi(self):
        input("\nTekan [ENTER] untuk melanjutkan...")
    
    def tampilan_menu_utama(self):
        while True:
            print("\n" + "="*40)
            print("MENU PROGRAM")
            print("="*40)
            print("1. Tambah data koleksi")
            print("2. Hapus data koleksi")
            print("3. Tampil semua data koleksi")
            print("4. Keluar")
            print("-"*40)
            
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.pilih_koleksi()
            elif pilihan == "2":
                self.hapus_koleksi()
            elif pilihan == "3":
                self.lihat_semua_koleksi()
            elif pilihan == "4":
                print("Terimakasih sudah menggunakan!")
                break
            else:
                print("Pilihan tidak valid!")
                
    def tampilan_menu_jenis(self):
        print("\n" + "=" * 40)
        print("JENIS KOLEKSI YANG AKAN DITAMBAH")
        print("=" * 40)
        print("1. Buku")
        print("2. Majalah")
        print("3. Jurnal")
        print("-" * 40)

        return input("Pilih jenis koleksi: ")
    
    def pilih_koleksi(self):
        pilih_koleksi = self.tampilan_menu_jenis()

        if pilih_koleksi == "1":
            self.tambah_buku()

        elif pilih_koleksi == "2":
            self.tambah_majalah()

        elif pilih_koleksi == "3":
            self.tambah_jurnal()

        else:
            print("Pilihan tidak valid.")
    
    def tambah_buku(self):
        
        print("\n--- TAMBAH DATA BUKU ---")
        
        kode = input("Masukkan kode: ")
        judul = input("Masukkan judul: ")
        tahun_terbit = input("Masukkan tahun: ")
        pengarang = input("Masukkan pengarang: ")
        penerbit = input("Masukkan penerbit: ")
        
        self.service.TambahBuku(
            kode,
            judul,
            tahun_terbit,
            pengarang,
            penerbit
        )
        
        print("Buku berhasil ditambahkan.")
        
        self.konfirmasi()
        
        
    def tambah_majalah(self):
        print("\n--- TAMBAH DATA MAJALAH ---")
        
        kode = input("Masukkan kode: ")
        judul = input("Masukkan judul: ")
        tahun_terbit = input("Masukkan tahun: ")
        penerbit = input("Masukkan penerbit: ")
        edisi = input("Masukkan edisi: ")
        
        self.service.TambahMajalah(
            kode,
            judul,
            tahun_terbit,
            penerbit,
            edisi
        )
        
        print("Buku berhasil ditambahkan.")
        
        self.konfirmasi()
        
        
    def tambah_jurnal(self):
        print("\n--- TAMBAH DATA JURNAL ---")
        
        kode = input("Masukkan kode: ")
        judul = input("Masukkan judul: ")
        tahun_terbit = input("Masukkan tahun: ")
        penerbit = input("Masukkan penerbit: ")
        bidang_studi = input("Masukkan bidang studi: ")
        impact_factor = input("Masukkan Impact Factor: ")
        
        try:
            self.service.TambahJurnal(
                kode,
                judul,
                tahun_terbit,
                penerbit,
                bidang_studi,
                impact_factor
            )
        except ValueError as e:
            print(e)
        
        print("Buku berhasil ditambahkan.")
        self.konfirmasi()
        
    def lihat_semua_koleksi(self):
        print("\n" + "="*60)
        print("Data Koleksi")
        print("="*60)
        
        try:
            data = self.service.lihat_semua()
            
            for i, item in enumerate(data, 1):
                print(f"\n[{i}]")
                print(item.tampilkan_detail())

        except ValueError as e:
            print(e)
        
        self.konfirmasi()

        
    def hapus_koleksi(self):
        print("\n--- HAPUS DATA KOLEKSI ---")
        print(" ")
        
        kode = input("Masukkan kode: ")

        print("\n" + "-"*40)
        try:
            self.service.hapus_koleksi(kode)
            print("Hapus data koleksi berhasil.")
            self.konfirmasi()
        except ValueError as e:
            print(e)