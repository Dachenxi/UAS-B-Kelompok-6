from .produk_roti import ProdukRoti
from ..interfaces import BisaDikembangkan

class RotiManis(ProdukRoti, BisaDikembangkan):
    inisial = "RM"
    def __init__(self, nama_produk: str, kode_produk: str, biaya_produksi: int, harga_jual: int, ukuran_batch: int, bahan_baku):
        super().__init__(nama_produk, kode_produk, biaya_produksi, harga_jual, ukuran_batch)
        self.bahan_baku = {
            'Tepung terigu': '500 gram',
            'Gula pasir': '100 gram',
            'Susu bubuk': '25 gram',
            'Kuning telur': '4 butir',
            'Ragi instant': '11 gram',
            'Susu cair': '130 ml',
            'Air es': '100 ml',
            'Mentega': '100 gram',
            'Garam': '1 sdt',
        }
    
    def pengadonan(self):
        """Metode untuk proses pengadonan pada Roti Manis"""
        return "Proses Pengadonan pada bahan Roti Manis"
    
    def pengembangan(self):
        """Metode untuk proses pengembangan pada Roti Manis."""
        return "Proses pengembangan pada Roti Manis."
    
    def pemanggangan(self):
        """Metode untuk proses pemanggangan pada Roti Manis"""
        return "Proses pemanggangan pada Roti Manis"
    
    def get_info(self) -> dict:
        """Mengembalikan informasi produk Roti Manis."""
        info = super().get_info()
        info["Pengembangan"] = "Dapat di kembangkan"
        return info
