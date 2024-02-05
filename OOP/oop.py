'''OOP'''
class Mobil:
    '''model mobil'''
    # Atribut Instance
    def __init__(self):
        self.warna = 'Merah'


mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# Mengubah atribut instance
mobil_1.warna = "Hitam"
mobil_2.warna = "Pink"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)
