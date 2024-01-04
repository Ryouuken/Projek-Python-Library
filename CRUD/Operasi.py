from time import time
from . import Database
from .Util import random_string
import time
import os

def delete(no_buku):
    # Buat file temporary untuk menyimpan data yang tidak akan dihapus
    try:
        with open("data_temp.txt", 'w', encoding="utf-8") as temp_file:
            with open(Database.DB_NAME, 'r') as file:
                counter = 0
                # Salin data ke file temporary kecuali data yang akan dihapus
                while True:
                    content = file.readline()
                    if len(content) == 0:
                        break
                    elif counter != no_buku - 1:
                        temp_file.write(content)
                    counter += 1
    except Exception as e:
        print(f"Error in deleting data: {e}")

    try:
        # Hapus file asli dan ganti nama file temporary menjadi file asli
        os.remove(Database.DB_NAME)
        os.rename("data_temp.txt", Database.DB_NAME)
    except Exception as e:
        print(f"Error in renaming files: {e}")

def update(no_buku,pk,data_add,tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    updated_data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        # Baca semua baris dari file
        with open(Database.DB_NAME, 'r', encoding="utf-8") as file:
            lines = file.readlines()

        # Update baris yang sesuai
        lines[no_buku - 1] = updated_data_str

        # Tulis kembali semua baris ke file
        with open(Database.DB_NAME, 'w', encoding="utf-8") as file:
            file.writelines(lines)
    except Exception as e:
        print(f"Error in updating data: {e}")

# Fungsi untuk membuat dan menambahkan data baru ke dalam database
def create(tahun, judul, penulis):
    # Salin template data dari Database
    data = Database.TEMPLATE.copy()

    # Isi data dengan informasi yang diberikan
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    # Bentuk string data untuk ditulis ke dalam file
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    try:
        # Buka file dalam mode append dan tulis data ke dalamnya
        with open(Database.DB_NAME, 'a', encoding="utf-8") as file:
            file.write(data_str)
    except Exception as e:
        print(f"Error in adding data: {e}")

# Fungsi untuk membuat data pertama kali dan menulisnya ke dalam database
def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")    
        except:
            print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")

    # Salin template data dari Database
    data = Database.TEMPLATE.copy()

    # Isi data dengan informasi yang diberikan
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    # Bentuk string data untuk ditulis ke dalam file
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    print(data_str)
    try:
        # Buka file dalam mode write dan tulis data ke dalamnya
        with open(Database.DB_NAME, 'w', encoding="utf-8") as file:
            file.write(data_str)
    except Exception as e:
        print(f"Error in creating first data: {e}")

# Fungsi untuk membaca data dari database
def read(**kwargs):
    try:
        # Buka file dalam mode read
        with open(Database.DB_NAME, 'r') as file:
            # Baca semua baris dari file
            content = file.readlines()
            jumlah_buku = len(content)
            
            # Jika parameter "index" ada, kembalikan data di index tersebut
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:    
                    return content[index_buku]
            else:
                return content
    except Exception as e:
        print(f"Error in reading database: {e}")
        return False
    