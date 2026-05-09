from abc import ABC, abstractmethod


class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__stok = 0                      
        self.__harga_dasar = harga_dasar     

    
    def get_stok(self):
        return self.__stok

    def get_harga_dasar(self):
        return self.__harga_dasar

    
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    
    @abstractmethod
    def tampilkan_detail(self, jumlah_beli):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor


    def tampilkan_detail(self, jumlah_beli):
        harga_dasar = self.get_harga_dasar()
        pajak = harga_dasar * 0.10           
        subtotal = (harga_dasar + pajak) * jumlah_beli
        print(f"1. [LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f"   Harga Dasar: Rp {harga_dasar:,.0f} | Pajak(10%): Rp {pajak:,.0f}")
        print(f"   Beli: {jumlah_beli} unit | Subtotal: Rp {subtotal:,.0f}")

    def hitung_harga_total(self, jumlah):
        harga_dasar = self.get_harga_dasar()
        pajak = harga_dasar * 0.10
        return (harga_dasar + pajak) * jumlah


class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera


    def tampilkan_detail(self, jumlah_beli):
        harga_dasar = self.get_harga_dasar()
        pajak = harga_dasar * 0.05           
        subtotal = (harga_dasar + pajak) * jumlah_beli
        print(f"2. [SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f"   Harga Dasar: Rp {harga_dasar:,.0f} | Pajak(5%): Rp {pajak:,.0f}")
        print(f"   Beli: {jumlah_beli} unit | Subtotal: Rp {subtotal:,.0f}")

  
    def hitung_harga_total(self, jumlah):
        harga_dasar = self.get_harga_dasar()
        pajak = harga_dasar * 0.05
        return (harga_dasar + pajak) * jumlah


def proses_transaksi(daftar_barang):
    """
    Menerima list berupa tuple: (objek_barang, jumlah_beli)
    Menampilkan struk dan total tagihan.
    """
    print("\n--- STRUK TRANSAKSI ---")
    total = 0
    for barang, jumlah in daftar_barang:
        barang.tampilkan_detail(jumlah)    
        total += barang.hitung_harga_total(jumlah)
    print("-" * 40)
    print(f"TOTAL TAGIHAN: Rp {total:,.0f}")
    print("-" * 40)




print("--- SETUP DATA ---")


laptop1 = Laptop("ROG Zephyrus", 20_000_000, "Ryzen 9")
hp1 = Smartphone("iPhone 13", 15_000_000, "12MP")

laptop1.tambah_stok(10)

hp1.tambah_stok(-5)

hp1.tambah_stok(20)

keranjang = [
    (laptop1, 2),
    (hp1, 1),
]

proses_transaksi(keranjang)