"""numpy adik2"""
# import sys
# import numpy as np

# var_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# var_array = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print("Ukuran keseluruhan elemen list dalam bytes = ",
#       sys.getsizeof(var_list)*len(var_list))
# print("Ukuran keseluruhan elemen NumPy dalam bytes = ",
#       var_array.size*var_array.itemsize)

# matriks = [[0 for j in range(4)] for i in range(3)]

# print(matriks)

# Membuat matriks 2x2
# var_mat = [[5, 0],
#            [1, -2]]
# def_mat = [[0 for j in range(2)] for i in range(2)]

# for i, row in enumerate(var_mat):
#     for j, value in enumerate(row):
#         def_mat[i][j] = value * 2

# print(def_mat)

# # pake numpy
# var_mat = np.array([[5, 0],
#                     [1, -2]])

# result = var_mat * 2

# print(result)


# def cetak_info(**kwargs):
#     """cetak info"""
#     info = ""
#     for key, value in kwargs.items():
#         info += key + ': ' + value + ", "
#     return info

def minimal(a, b):
    '''mencari nilai minimal'''
    if a == b:
        return a
    elif a < b:
        return a
    else:
        return b
