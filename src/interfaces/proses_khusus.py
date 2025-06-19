from abc import ABC, abstractmethod

class BisaDikembangkan(ABC):
    @abstractmethod
    def pengembangan(self):
        """Metode untuk mengembangkan produk."""
        pass

class BisaDiberiToping(ABC):
    @abstractmethod
    def toping(self):
        """Metode untuk menambahkan toping pada produk."""
        pass