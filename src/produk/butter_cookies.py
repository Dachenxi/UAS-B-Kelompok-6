from .produk_roti import ProdukRoti
from ..interfaces import BisaDiberiToping

class ButterCookies(ProdukRoti, BisaDiberiToping):
    inisial = "BC"
    def __init__(self, nama_produk: str, kode_produk: str, biaya_produksi: int, harga_jual: int, ukuran_batch: int, bahan_baku):
        super().__init__(nama_produk, kode_produk, biaya_produksi, harga_jual, ukuran_batch)
        self.bahan_baku = bahan_baku
        
    def toping(self):
        """Metode untuk menambahkan toping pada Butter Cookies."""
        return "Menambahkan toping pada Butter Cookies."
    
    def get_info(self) -> dict:
        """Mengembalikan informasi produk Butter Cookies."""
        info = super().get_info()
        info["Toping"] = "Dapat diberi toping"
        return info