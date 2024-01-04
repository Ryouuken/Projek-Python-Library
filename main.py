import os
import CRUD as CRUD

if __name__ == "__main__":
    # Mendapatkan nama sistem operasi
    sistem_operasi = os.name

    # Membersihkan layar konsol berdasarkan sistem operasi
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("=========================")

    # Memeriksa apakah database sudah ada atau belum
    CRUD.init_console()

    while True:
        # Membersihkan layar konsol berdasarkan sistem operasi
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")

        # Menampilkan menu utama
        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        # Meminta input dari pengguna
        user_option = input("Masukkan opsi: ")

        # Melakukan operasi sesuai dengan pilihan pengguna
        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()

        # Meminta konfirmasi untuk keluar dari program
        is_done = input("Apakah Selesai (y/n)? ")
        if is_done.lower() == "y":
            break

    print("Program Berakhir, Terima Kasih KAKAAAAA")
