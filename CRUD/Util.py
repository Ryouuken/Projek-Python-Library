import random
import string

# Fungsi untuk menghasilkan string acak dengan panjang tertentu
def random_string(panjang: int) -> str:
    # Menggabungkan karakter acak dari string ASCII uppercase dan lowercase
    hasil_string = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasil_string
