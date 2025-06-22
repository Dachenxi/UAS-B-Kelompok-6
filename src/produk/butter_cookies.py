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
        
    def toping(self):
        return "Menambahkan toping pada Butter Cookies."
    
    def get_info(self) -> dict:
        info = super().get_info()
        info["Toping"] = "Dapat diberi toping"
        return info