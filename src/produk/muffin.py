from .produk_roti import ProdukRoti
from ..interfaces import BisaDikembangkan, BisaDiberiToping

class Muffin(ProdukRoti, BisaDikembangkan, BisaDiberiToping):
    inisial = "MF"
    def __init__(self, nama_produk: str, kode_produk: str, biaya_produksi: int, harga_jual: int, ukuran_batch: int):
        super().__init__(nama_produk, kode_produk, biaya_produksi, harga_jual, ukuran_batch)
        self.bahan_baku = {
            'Telur': '4 butir',
            'Gula': '200 gr',
            'Susu cair': '200 ml',
            'Minyak': '200 ml',
            'Terigu': '625 gram',
            'Vanili': '1 sachet',
            'Backing powder': '15 gram',
        }
    
    def pengadonan(self) -> str:
        return "campurkan bahan seperti telur gula susu cair minyak terigu vanili dan backing powder, aduk dengan mixer hingga tidak ada yang menggumpal"
    
    def pengembangan(self):
        return "setelah di aduk diamkan sejenak, lalu masukkan kedalam loyang kecil"
    
    def pemanggangan(self):
        return "kemudian oven di suhu 180 derajat celcius selama 20 menit"
    
    def toping(self):
        return "beri hiasan toping bisa sebelum dimasukkan ke oven atau setelah proses oven"
    
    def get_info(self) -> dict:
        """Mengembalikan informasi produk Muffin."""
        info = super().get_info()
        info["Pengembangan"] = "Dapat di kembangkan"
        info["Toping"] = "beri toping sesuai selera"
        return info