from .produk_roti import ProdukRoti
from ..interfaces import BisaDikembangkan, BisaDiberiToping

class Muffin(ProdukRoti, BisaDikembangkan, BisaDiberiToping):
    inisial = "MF"
    def __init__(self, nama_produk: str, kode_produk: str, biaya_produksi: int, harga_jual: int, ukuran_batch: int, bahan_baku):
        super().__init__(nama_produk, kode_produk, biaya_produksi, harga_jual, ukuran_batch)
        self.bahan_baku = bahan_baku
        
    def pengembangan(self):
        """Metode untuk proses pengembangan pada Muffin."""
        return "Proses pengembangan pada Muffin."
    
    def toping(self):
        """Metode untuk menambahkan toping pada Muffin."""
        return "Menambahkan toping pada Muffin."
    
    def get_info(self) -> dict:
        """Mengembalikan informasi produk Muffin."""
        info = super().get_info()
        info["Pengembangan"] = "Dapat di kembangkan"
        info["Toping"] = "Dapat diberi toping"
        return info