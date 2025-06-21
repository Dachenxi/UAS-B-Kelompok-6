from abc import ABC, abstractmethod

class ProdukRoti(ABC):
    """
    Kelas abstrak untuk produk roti.

    >>> bahan_baku: { # Contoh bahan baku
        'Tepung Terigu': '250 gr',
        'Gula Pasir': '50 gr',
        'Baking Powder': '1 sdt',
    }
    """

    def __init__(self,
                 nama_produk: str,
                 kode_produk: str,
                 biaya_produksi: int,
                 harga_jual: int,
                 ukuran_batch: int):
        self.nama_produk = nama_produk
        self.kode_produk = kode_produk
        self.biaya_produksi = biaya_produksi
        self.harga_jual = harga_jual
        self.ukuran_batch = ukuran_batch
        self.bahan_baku = {} # nanti di ganti di setiap subclass

    def get_info(self) -> dict:
        """Mengembalikan informasi produk roti.

        Returns:
            dict: Informasi produk roti yang berisi nama, kode, biaya produksi, harga jual, dan bahan baku.
        """
        return {
            "Nama Produk": self.nama_produk,
            "Kode Produksi": self.kode_produk,
            "Biaya Produksi": f"Rp {self.biaya_produksi:,}",
            "Harga Jual": f"Rp {self.harga_jual:,}",
            "Jenis": self.__class__.__name__,
        }