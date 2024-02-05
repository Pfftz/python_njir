import re     # Import modul regex

# Mencari pola kata yang diawali (^) dengan huruf 'j' dan diakhiri ($) dengan huruf 'r'
pola= '^j...r$'
string_tes= 'jawir'
hasil= re.match(pola, string_tes)
 
if hasil:
    print("Pencarian berhasil.")
else:
    print("Pencarian gagal.")
