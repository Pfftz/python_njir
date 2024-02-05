'''library file management'''
import json

# contoh JSON:
X = '{ "nama":"Buchori", "umur":22, "Kota":"New York"}'

# parse  x:
Y = json.loads(X)

print(Y["umur"], Y["Kota"], Y["nama"])
