from typing import List, Optional
import sys, os, time

from rich import box
from rich.align import Align
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, Confirm

from .produk import *
from .interfaces import *

class HanariBakeryApp:
    """Class utama yang mengelola interface Hanari Bakery."""
    def __init__(self):
        self.console = Console()
        self.daftar_produk: List[ProdukRoti] = []
        self.produk_tersedia: dict = {
            "1": RotiManis,
            "2": Croissant,
            "3": ButterCookies,
            "4": Muffin
        }
        self.ukuran_batch: int = 20

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

    def generate_kode(self, kelas_produk: ProdukRoti) -> str:
        inisial = kelas_produk.inisial
        # Ambil counter terakhir untuk inisial ini, jika tidak ada, mulai dari 0
        count_terakhir = self.counters.get(inisial, 0)

        count_baru = count_terakhir + 1

        self.counters[inisial] = count_baru

        # Format kode (misal: RM01, CR12). :02d berarti format sebagai integer 2 digit dengan nol di depan.
        kode_baru = f"{inisial}{count_baru:02d}"

        return kode_baru


    def run(self):
        """Menjalankan aplikasi Hanari Bakery."""
        self.console.print("[bold][green]Selamat datang[/green] di Hanari Bakery!. [red]Enter[/red] untuk memulai.[/bold]", end="")
        time.sleep(1)
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
                self.console.print("[bold][green]Terima kasih[/green] telah menggunakan Hanari Bakery![/bold]")
                sys.exit(0)
            else:
                self.console.print("[bold]Pilihan [red]tidak valid[/red]. Silakan coba lagi.[/bold]")

            self.clean_screen()

    def tambah_produk(self):
        time.sleep(1)

        tambah_produk_table = Table(title="Tambah Produk Roti", box=box.ROUNDED)
        tambah_produk_table.add_column("Nomor", justify="left", style="bold")
        tambah_produk_table.add_column("Jenis Produk", justify="left", style="bold")

        for nomor, produk in self.produk_tersedia.items():
            tambah_produk_table.add_row(nomor, produk.__name__)

        while True:
            self.clean_screen()
            self.console.print(tambah_produk_table)
            pilihan = Prompt.ask("Pilih [blue]jenis[/blue] produk (1-4)", choices=["1", "2", "3", "4"], show_choices=False)
            ulang = Confirm.ask(f"Apakah [red]Anda yakin[/red] ingin menambahkan produk {self.produk_tersedia[pilihan].__name__}?", default=True)
            if ulang:
                produk_terpilih = self.produk_tersedia[pilihan]
                time.sleep(1)
                break

        while True:
            self.clean_screen()
            self.console.print(f"[blue bold]Masukan detail data untuk produk {produk_terpilih.__name__}[/blue bold]")

            nama_produk = Prompt.ask("Masukkan [blue]nama[/blue] produk")
            biaya_produksi = IntPrompt.ask(f"Masukkan [blue]biaya produksi[/blue] untuk {self.ukuran_batch} pcs", default=0, min_allowed=0)
            harga_jual = IntPrompt.ask(f"Masukkan [blue]harga jual[/blue] per {self.ukuran_batch} pcs", default=0, min_allowed=0)
            kode_otomatis = self._generate_kode_produk(produk_terpilih)

            tabel_konfirmasi = Table(title="Konfirmasi Data Produk", box=box.ROUNDED)

            tabel_konfirmasi.add_column("Attribut", justify="left", style="bold")
            tabel_konfirmasi.add_column("Nilai", justify="left")

            tabel_konfirmasi.add_row("Nama Produk", nama_produk)
            tabel_konfirmasi.add_row("Jenis Produk", produk_terpilih.__name__)
            tabel_konfirmasi.add_row("Kode Produk", kode_otomatis)
            tabel_konfirmasi.add_row("Biaya Produksi", f"Rp {biaya_produksi:,} per {self.ukuran_batch} pcs")
            tabel_konfirmasi.add_row("Harga Jual", f"Rp {harga_jual:,} per {self.ukuran_batch} pcs")

            self.console.print(tabel_konfirmasi)
            konfirmasi = Confirm.ask("Apakah data sudah [green]benar[/green]?", default=True)
            if konfirmasi:
                break
            else:
                self.console.print("[red bold]Silakan masukkan ulang data produk.[/red bold]")
                time.sleep(1)
                self.clean_screen()

        produk_baru = produk_terpilih(nama_produk,
                                      kode_otomatis,
                                      biaya_produksi,
                                      harga_jual)
        self.daftar_produk.append(produk_baru)
        self.console.print(f"[green bold]Produk {nama_produk} berhasil ditambahkan![/green bold]")

    def lihat_produk(self):
        self.console.print("Daftar Produk Roti", style="bold blue")
        input()

    def estimasi_profit(self):
        self.console.print("Estimasi Profit Produk Roti", style="bold blue")
        input()

    def simulasi_produksi(self):
        self.console.print("Simulasi Proses Produksi Roti", style="bold blue")
        input()