import sys
from src import HanariBakeryApp
from rich import print

if __name__ == "__main__":
    try:
        app = HanariBakeryApp()
        app.run()
    except KeyboardInterrupt:
        print("\n[red bold]Aplikasi dihentikan oleh pengguna.[/red bold]")
        sys.exit(0)