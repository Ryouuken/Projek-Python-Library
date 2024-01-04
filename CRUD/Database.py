from . import Operasi

# Nama file database
DB_NAME = "data.txt"

# Template untuk data buku
TEMPLATE = {
    "pk": "XXXXXX",
    "date_add": "yyyy-mm-dd",
    "judul": 255 * " ",  # Judul dengan panjang maksimum 255 karakter
    "penulis": 255 * " ",  # Penulis dengan panjang maksimum 255 karakter
    "tahun": "yyyy"
}

# Fungsi untuk inisialisasi konsol, memeriksa apakah database sudah ada
def init_console():
    try:
        # Mencoba membuka file database dalam mode baca ("r")
        with open(DB_NAME, "r"):
            print("Database tersedia, inisialisasi selesai!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        Operasi.create_first_data()
