from typing import List, Optional
import sys, os, time

from rich import box
from rich.align import Align
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, Confirm

from .produk import ProdukRoti, RotiManis, Croissant, ButterCookies, Muffin
from .interfaces import BisaDiberiToping, BisaDikembangkan

class HanariBakeryApp:
    """Class utama yang mengelola interface Hanari Bakery."""
    def __init__(self):
        self.console = Console()
        self.daftar_produk: List[ProdukRoti] = []
        self.counters: dict = {}
        self.produk_tersedia: dict = {
            "1": RotiManis,
            "2": Croissant,
            "3": ButterCookies,
            "4": Muffin
        }

    def _menu(self):
        """Menampilkan main menu"""
        table_menu = Table(title="Aplikasi Hanari Bakery", box=box.HEAVY_HEAD)
        header = ["Nomor", "Nama Menu", "Deskripsi"]
        for head in header:
            table_menu.add_column(head, justify="left", no_wrap=True, style="bold")

        table_menu.add_row("1", "Tambah Produk", "Menambahkan produk roti baru")
        table_menu.add_row("2", "Lihat Produk", "Melihat daftar produk roti")
        table_menu.add_row("3", "Estimasi Profit", "Menghitung estimasi profit dari produk")
        table_menu.add_row("4", "Simulasi Proses Produksi", "Mensimulasikan proses produksi roti")
        table_menu.add_row("5", "Keluar", "Keluar dari aplikasi")

        self.console.print(table_menu)

    def _clean_screen(self):
        """Membersihkan layar terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def _generate_kode(self, kelas_produk: ProdukRoti) -> str:
        inisial = kelas_produk.inisial
        # Ambil counter terakhir untuk inisial ini, jika tidak ada, mulai dari 0
        count_terakhir = self.counters.get(inisial, 0)

        count_baru = count_terakhir + 1

        self.counters[inisial] = count_baru

        # Format kode (misal: RM01, CR12). :02d berarti format sebagai integer 2 digit dengan nol di depan.
        kode_baru = f"{inisial}{count_baru:02d}"

        return kode_baru

    def _jeda_untuk_lanjut(self):
        """
        Mencetak pesan dan menjeda program hingga pengguna menekan Enter.
        """
        self.console.print("\n[bold yellow]Tekan Enter untuk kembali ke menu utama...[/bold yellow]", end="")
        input()

    def run(self):
        """Menjalankan aplikasi Hanari Bakery."""
        self.console.print("[bold][green]Selamat datang[/green] di Hanari Bakery!. [red]Enter[/red] untuk memulai.[/bold]", end="")
        time.sleep(0.5)
        input()
        self._clean_screen()
        while True:
            self._menu()
            choice = IntPrompt.ask("Pilih [blue bold]menu[/blue bold] (1-5)",
                                   choices=["1", "2", "3", "4", "5"],
                                   show_choices=False)

            if choice == 1:
                self.console.print("[bold]Anda memilih untuk menambahkan produk roti.[/bold]")
                self.tambah_produk()
            elif choice == 2:
                self.console.print("[bold]Anda memilih untuk melihat daftar produk roti.[/bold]")
                self.lihat_produk()
            elif choice == 3:
                self.console.print("[bold]Anda memilih untuk menghitung estimasi profit dari produk roti.[/bold]")
                self.estimasi_profit()
            elif choice == 4:
                self.console.print("[bold]Anda memilih untuk mensimulasikan proses produksi roti.[/bold]")
                self.simulasi_produksi()
            elif choice == 5:
                self.console.print("[bold][green]Terima kasih[/green] telah menggunakan Hanari Bakery![/bold]")
                sys.exit(0)
            else:
                self.console.print("[bold]Pilihan [red]tidak valid[/red]. Silakan coba lagi.[/bold]")

    def tambah_produk(self):
        tambah_produk_table = Table(title="Tambah Produk Roti", box=box.HEAVY_HEAD)
        tambah_produk_table.add_column("Nomor", justify="left", style="bold")
        tambah_produk_table.add_column("Jenis Produk", justify="left", style="bold")

        for nomor, produk in self.produk_tersedia.items():
            tambah_produk_table.add_row(nomor, produk.__name__)

        time.sleep(1)

        while True:
            self._clean_screen()
            self.console.print(tambah_produk_table)
            pilihan = Prompt.ask("Pilih [blue]jenis[/blue] produk (1-4)", choices=["1", "2", "3", "4"], show_choices=False)
            ulang = Confirm.ask(f"Apakah [red]Anda yakin[/red] ingin menambahkan produk {self.produk_tersedia[pilihan].__name__}?", default=True, show_default=False)
            if ulang:
                produk_terpilih = self.produk_tersedia[pilihan]
                time.sleep(1)
                break

        kode_otomatis = self._generate_kode(produk_terpilih)

        while True:
            self._clean_screen()
            self.console.print(f"[blue bold]Masukan detail data untuk produk {produk_terpilih.__name__}[/blue bold]")

            nama_produk = Prompt.ask("Masukkan [blue]nama[/blue] produk")
            ukuran_batch = IntPrompt.ask("Masukan [blue bold]ukuran batch[/blue bold]", default=5, show_default=False)
            biaya_produksi = IntPrompt.ask(f"Masukkan [blue bold]biaya produksi[/blue bold] untuk {ukuran_batch} pcs", default=0, show_default=False)
            harga_jual = IntPrompt.ask(f"Masukkan [blue]harga jual[/blue] per {ukuran_batch} pcs", default=0, show_default=False)

            tabel_konfirmasi = Table(title="Konfirmasi Data Produk", box=box.HEAVY_HEAD)

            tabel_konfirmasi.add_column("Attribut", justify="left", style="bold")
            tabel_konfirmasi.add_column("Nilai", justify="left")

            tabel_konfirmasi.add_row("Nama Produk", nama_produk)
            tabel_konfirmasi.add_row("Jenis Produk", produk_terpilih.__name__)
            tabel_konfirmasi.add_row("Kode Produk", kode_otomatis)
            tabel_konfirmasi.add_row("Ukuran Batch", f"{ukuran_batch}")
            tabel_konfirmasi.add_row("Biaya Produksi", f"Rp {biaya_produksi:,} per {ukuran_batch} pcs")
            tabel_konfirmasi.add_row("Harga Jual", f"Rp {harga_jual:,} per {ukuran_batch} pcs")

            self._clean_screen()
            self.console.print(tabel_konfirmasi)
            konfirmasi = Confirm.ask("Apakah data sudah [green]benar[/green]?", default=True, show_default=False)
            if konfirmasi:
                break
            else:
                self.console.print("[red bold]Silakan masukkan ulang data produk.[/red bold]")
                time.sleep(1)
                self._clean_screen()

        produk_baru = produk_terpilih(nama_produk,
                                      kode_otomatis,
                                      biaya_produksi,
                                      harga_jual,
                                      ukuran_batch)
        
        self.daftar_produk.append(produk_baru)
        self.console.print(f"[green bold]Produk {nama_produk} berhasil ditambahkan![/green bold]")

        self._jeda_untuk_lanjut()
        self._clean_screen()

    def lihat_produk(self):
        self._clean_screen()
        if not self.daftar_produk:
            self.console.print("[red bold]Belum ada produk roti yang ditambahkan.[/red bold]")
            self._jeda_untuk_lanjut()
            self._clean_screen()
            return

        produk_table = Table(title="Daftar Produk Roti", box=box.HEAVY_HEAD)
        produk_table.add_column("No", justify="left", style="bold")

        info_pertama = self.daftar_produk[0].get_info()
        headers = list(info_pertama.keys())

        for header in headers:
            produk_table.add_column(header, justify="left", style="bold")

        produk_table.add_column("Fitur Khusus", justify="left", style="yellow")

        for idx, produk in enumerate(self.daftar_produk, start=1):
            produk_info = produk.get_info()

            # 3. Cek kemampuan produk menggunakan isinstance
            fitur_list = []
            if isinstance(produk, BisaDikembangkan):
                fitur_list.append("Pengembangan")
            if isinstance(produk, BisaDiberiToping):
                fitur_list.append("Topping")

            # Gabungkan daftar fitur menjadi satu string yang rapi
            fitur_str = ", ".join(fitur_list) if fitur_list else "-"

            # 4. Tambahkan baris ke tabel, termasuk kolom fitur baru
            produk_table.add_row(
                str(idx),
                *produk_info.values(), # Gunakan '*' untuk memasukkan semua value dari dict
                fitur_str
            )

        self.console.print(produk_table)
        self._jeda_untuk_lanjut()
        self._clean_screen()

    def estimasi_profit(self):
        self._clean_screen()
        if not self.daftar_produk:
            self.console.print("[red bold]Belum ada produk roti yang ditambahkan.[/red bold]")
            self._jeda_untuk_lanjut()
            self._clean_screen()
            return

        # Menampilkan produk yang tersedia
        produk_table = Table(title="Daftar Produk Roti untuk Estimasi Profit", box=box.HEAVY_HEAD)
        produk_table.add_column("No", justify="left", style="bold")
        produk_table.add_column("Nama Produk", justify="left", style="bold")
        produk_table.add_column("Kode Produk", justify="left", style="bold")

        for idx, produk in enumerate(self.daftar_produk, start=1):
            produk_table.add_row(
                str(idx),
                produk.nama_produk,
                produk.kode_produk
            )

        self.console.print(produk_table)

        # Memilih produk untuk estimasi profit
        pilihan = IntPrompt.ask("Pilih [blue]nomor[/blue] produk untuk estimasi profit",
                                choices=[str(i) for i in range(1, len(self.daftar_produk) + 1)],
                                show_choices=False)

        produk_terpilih = self.daftar_produk[pilihan - 1]

        # Minta jumlah produksi
        jumlah_produksi = IntPrompt.ask(f"Masukkan [blue]jumlah[/blue] pcs untuk {produk_terpilih.nama_produk}",
                                        default=1)

        # Perhitungan estimasi profit
        profit_per_batch = produk_terpilih.harga_jual - produk_terpilih.biaya_produksi

        # Profit untuk 1 pcs
        if produk_terpilih.ukuran_batch > 0:
            profit_per_pcs = profit_per_batch / produk_terpilih.ukuran_batch
        else:
            profit_per_pcs = 0

        total_estimasi_profit = profit_per_pcs * jumlah_produksi

        # Tabel estimasi profit
        estimasi_table = Table(title=f"Estimasi Profit untuk {produk_terpilih.nama_produk}", box=box.HEAVY_HEAD)
        estimasi_table.add_column("Deskripsi", style="bold")
        estimasi_table.add_column("Nilai", style="bold green")

        estimasi_table.add_row("Jumlah Produksi", f"{jumlah_produksi} pcs")
        estimasi_table.add_row("Biaya Produksi per Batch", f"Rp {produk_terpilih.biaya_produksi:,}")
        estimasi_table.add_row("Harga Jual per Batch", f"Rp {produk_terpilih.harga_jual:,}")
        estimasi_table.add_row("Profit per Batch", f"Rp {profit_per_batch:,}")
        estimasi_table.add_row("Profit per Pcs", f"Rp {profit_per_pcs:,.0f}")
        estimasi_table.add_row("Total Estimasi Profit", f"Rp {total_estimasi_profit:,.0f}")

        self._clean_screen()
        self.console.print(estimasi_table)

        self._jeda_untuk_lanjut()
        self._clean_screen()

    def simulasi_produksi(self):
        self._clean_screen()

        # Langkah 1: Pilih Produk (logika ini sama persis dengan di estimasi_profit)
        if not self.daftar_produk:
            self.console.print("[bold red]Belum ada produk roti yang ditambahkan.[/bold red]")
            self._jeda_untuk_lanjut()
            self._clean_screen()
            return

        pilihan_produk_table = Table(title="Pilih Produk untuk Disimulasikan")
        pilihan_produk_table.add_column("No", style="bold")
        pilihan_produk_table.add_column("Kode", style="cyan")
        pilihan_produk_table.add_column("Nama Produk", style="magenta")

        for idx, produk in enumerate(self.daftar_produk, start=1):
            pilihan_produk_table.add_row(str(idx), produk.kode_produk, produk.nama_produk)

        self.console.print(pilihan_produk_table)

        choices = [str(i) for i in range(1, len(self.daftar_produk) + 1)]
        pilihan_idx = IntPrompt.ask(
            "\nMasukkan [blue]nomor[/blue] produk",
            choices=choices,
            show_choices=False
        ) - 1

        produk_terpilih = self.daftar_produk[pilihan_idx]

        # Langkah 2: Jalankan Simulasi dengan Urutan yang Benar
        self.console.print(f"\n[bold]--- Memulai Simulasi untuk [yellow]{produk_terpilih.nama_produk}[/yellow] ---[/bold]\n")
        time.sleep(1)

        # Memanggil metode proses wajib dari superclass ProdukRoti
        self.console.print("> ", produk_terpilih.pengadonan())
        time.sleep(1)

        # Memeriksa apakah produk ini punya kemampuan 'BisaDikembangkan'
        if isinstance(produk_terpilih, BisaDikembangkan):
            self.console.print("> ", produk_terpilih.pengembangan())
            time.sleep(1)

        # Memanggil metode proses wajib dari superclass ProdukRoti
        self.console.print("> ", produk_terpilih.pemanggangan())
        time.sleep(1)

        # Memeriksa apakah produk ini punya kemampuan 'BisaDiberiToping'
        if isinstance(produk_terpilih, BisaDiberiToping):
            self.console.print("> ", produk_terpilih.toping())
            time.sleep(1)

        self.console.print("\n[bold green]--- Simulasi Selesai ---[/bold green]")

        # Langkah 3: Jeda Layar
        self._jeda_untuk_lanjut()
        self._clean_screen()