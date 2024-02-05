'''library pickle digunakan untuk menyimpan dictionary ke dalam file 
dan membaca kembali dictionary dari file tersebut'''
import pickle

contoh_dictionary = {1: "6", 2: "2", 3: "f"}
#wb = mode write binary
pickle_keluar = open("dict.pickle", "wb")
pickle.dump(contoh_dictionary, pickle_keluar)
pickle_keluar.close()

#rb = mode read binary
pickle_masuk = open("dict.pickle", "rb")
#load dictionary dari file
contohDictionary = pickle.load(pickle_masuk)
pickle_masuk.close()

print(contohDictionary, pickle_masuk, pickle_keluar)
