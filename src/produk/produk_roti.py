from abc import ABC, abstractmethod

class ProdukRoti(ABC):
    """
    Kelas abstrak untuk produk roti.

    Atribut:
        nama_produk (str): Nama produk roti.
        kode_produk (str): Kode unik untuk produk roti.
        biaya_produksi (int): Biaya produksi per unit produk.
        harga_jual (int): Harga jual per unit produk.
        bahan_baku (dict): Bahan baku yang digunakan dalam produk roti.

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
                 harga_jual: int):
        self.nama_produk = nama_produk
        self.kode_produk = kode_produk
        self.biaya_produksi = biaya_produksi
        self.harga_jual = harga_jual
        self.bahan_baku = {} # nanti di ganti di setiap subclass
