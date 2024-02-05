'''library argparse digunakan untuk memparsing argumen yang diberikan saat menjalankan program.'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
parser.add_argument('-t', '--TANGGALLAHIR', required=True,
                    help="Masukkan Tanggal Lahir Anda (DD-MM-YYYY)")
args = parser.parse_args()

args.TANGGALLAHIR = args.TANGGALLAHIR.split('-')
args.TANGGALLAHIR = list(map(int, args.TANGGALLAHIR))

if 2024 - args.TANGGALLAHIR[2] > 30:
    print("Halo, bapak "+args.nama)
    print("Terima kasih telah menggunakan panggildicoding.py pada tahun 2024")
else:
    print("Halo, kakak"+args.nama)
    print("Terima kasih telah menggunakan panggildicoding.py pada tahun 2024")
