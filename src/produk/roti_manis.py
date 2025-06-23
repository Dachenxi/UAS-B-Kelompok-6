from .produk_roti import ProdukRoti
from ..interfaces import BisaDikembangkan

class RotiManis(ProdukRoti, BisaDikembangkan):
    inisial = "RM"
    def __init__(self, nama_produk: str, kode_produk: str, biaya_produksi: int, harga_jual: int, ukuran_batch: int):
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
        return "campur semua bahan kering kecuali garam aduk menggunakan spatula, lalu masukkan susu air dan telur aduk dan uleni sampai rata atau kalis. terakhir masukkan mentega dan garam aduk hingga rata"
    
    def pengembangan(self):
        return "setelah adonan kalis, diamkan selama 30 menit, jika sudah potong dan bulatkan dengan berat 40gr lalu diamkan kembali selama 15-20 menit. kemudian bentuk sesuai selera dan diamkan kembali selama 20-30 menit/sampai mengembang"
    
    def pemanggangan(self):
        return "kemudian oleskan margarin, dan oven di suhu 170 derajat celcius selama 15-20menit, setelah itu keluarkan dan olesi kembali dengan mentega lalu oven selama 20-25 menit"
    
    def get_info(self) -> dict:
        info = super().get_info()
        info["Pengembangan"] = "Dapat dilakukan dengan mendiamkan terlebih dahulu ataupun dipotong dahulu"
        return info
