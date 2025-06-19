from .produk_roti import ProdukRoti
from ..interfaces import BisaDikembangkan, BisaDiberiToping

class Muffin(ProdukRoti, BisaDikembangkan, BisaDiberiToping):
    pass