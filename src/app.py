from typing import List, Optional
import sys, os

from rich import box
from rich.align import Align
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt

from .produk import *
from .interfaces import *

class HanariBakeryApp:
    """Class utama yang mengelola interface Hanari Bakery."""
    def __init__(self):
        self.console = Console()
        self.produk_list: List[ProdukRoti] = []

    def menu(self):
        """Menampilkan main menu"""
        table_menu = Table(title="Aplikasi Hanari Bakery", box=box.ROUNDED)
        header = ["Nomor", "Nama Menu", "Deskripsi"]
        for head in header:
            table_menu.add_column(head, justify="left", no_wrap=True, style="bold")

        table_menu.add_row("1", "Tambah Produk", "Menambahkan produk roti baru")
        table_menu.add_row("2", "Lihat Produk", "Melihat daftar produk roti")
        table_menu.add_row("3", "Estimasi Profit", "Menghitung estimasi profit dari produk")
        table_menu.add_row("4", "Simulasi Proses Produksi", "Mensimulasikan proses produksi roti")
        table_menu.add_row("5", "Keluar", "Keluar dari aplikasi")

        self.console.print(table_menu)

    def clean_screen(self):
        """Membersihkan layar terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        """Menjalankan aplikasi Hanari Bakery."""
        self.console.print("[green]Selamat datang[/green] di Hanari Bakery!. [red]Enter[/red] untuk memulai.", end="", style="bold")
        input()
        self.clean_screen()
        while True:
            self.menu()
            choice = IntPrompt.ask("Pilih menu (1-5)",
                                   choices=["1", "2", "3", "4", "5"],
                                   show_choices=False)

            if choice == 1:
                self.tambah_produk()
            elif choice == 2:
                self.lihat_produk()
            elif choice == 3:
                self.estimasi_profit()
            elif choice == 4:
                self.simulasi_produksi()
            elif choice == 5:
                self.console.print("[green]Terima kasih[/green] telah menggunakan Hanari Bakery!", style="bold")
                sys.exit(0)
            else:
                self.console.print("Pilihan [red]tidak valid[/red]. Silakan coba lagi.", style="bold")

            self.clean_screen()

    def tambah_produk(self):
        self.console.print("Menambahkan Produk Roti Baru", style="bold blue")
        input()

    def lihat_produk(self):
        self.console.print("Daftar Produk Roti", style="bold blue")
        input()

    def estimasi_profit(self):
        self.console.print("Estimasi Profit Produk Roti", style="bold blue")
        input()
        
    def simulasi_produksi(self):
        self.console.print("Simulasi Proses Produksi Roti", style="bold blue")
        input()