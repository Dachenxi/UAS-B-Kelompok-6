from .produk_roti import ProdukRoti
from ..interfaces import BisaDiberiToping

class ButterCookies(ProdukRoti, BisaDiberiToping):
    inisial = "BC"
    def __init__(self, nama_produk: str, kode_produk: str, biaya_produksi: int, harga_jual: int, ukuran_batch: int):
        super().__init__(nama_produk, kode_produk, biaya_produksi, harga_jual, ukuran_batch)
        self.bahan_baku = {
            'Tepung Terigu': '200 gr',
            'Mentega': '100 gr',
            'Gula Pasir': '50 gr',
            'Telur': '1 butir',
            'Vanili': '1 sdt',
        }

    def toping(self) -> str:
        return "Menambahkan toping pada Butter Cookies."

    def pengadonan(self) -> str:
        return "Mencampurkan mentega dan gula, masukkan telur dan vanili, aduk dengan tepung hingga kalis, lalu bentuk dan panggang hingga keemasan untuk membuat butter cookies yang lezat."

    def pemanggangan(self) -> str:
        return "Memanggang butter cookies dalam oven pada suhu 180°C selama 15-20 menit hingga berwarna keemasan dan teksturnya renyah."