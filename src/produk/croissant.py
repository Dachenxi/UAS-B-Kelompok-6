from .produk_roti import ProdukRoti
from ..interfaces import BisaDikembangkan

class Croissant(ProdukRoti, BisaDikembangkan):
    inisial = "CR"
    def __init__(self, nama_produk: str, kode_produk: str, biaya_produksi: int, harga_jual: int, ukuran_batch: int):
        super().__init__(nama_produk, kode_produk, biaya_produksi, harga_jual, ukuran_batch)
        self.bahan_baku = {
            'Tepung Terigu': '250 gr',
            'Mentega': '150 gr',
            'Gula Pasir': '50 gr',
            'Garam': '1 sdt',
            'Ragi': '1 sdt',
            'Susu Cair': '100 ml',
        }

    def pengembangan(self) -> str:
        return "Adonan croissant dikembangkan dengan teknik lipatan berlapis untuk menghasilkan tekstur yang renyah."

    def pengadonan(self) -> str:
        return "Mencampurkan tepung terigu, gula, garam, dan ragi. Tambahkan susu cair, uleni hingga kalis, lalu istirahatkan selama 30 menit sebelum dilipat dengan mentega."

    def pemanggangan(self) -> str:
        return "Croissant dipanggang dalam oven pada suhu 200°C selama 15-20 menit hingga berwarna keemasan dan mengembang sempurna."