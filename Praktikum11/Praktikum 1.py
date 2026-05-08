#=============================================================
# Nama  : Asma Mazaya
# NIM   : J0403251105
# Kelas : A1
# Praktikum 1 : Adjacency Matrix
#===============================================
adjacency_matrix = [
    [0, 1, 1, 0],  # Baris 0: Node 0 terhubung ke Node 1 dan Node 2
    [1, 0, 1, 1],  # Baris 1: Node 1 terhubung ke Node 0, Node 2, dan Node 3
    [1, 1, 0, 1],  # Baris 2: Node 2 terhubung ke Node 0, Node 1, dan Node 3
    [0, 1, 1, 0]   # Baris 3: Node 3 terhubung ke Node 1 dan Node 2
]
# Menampilkan adjacency matrix
print("Adjacency Matrix:")
for row in adjacency_matrix:
    print(row)
# Penjelasan arti setiap baris:
# Baris 0: Node 0 terhubung ke Node 1 dan Node
# Baris 1: Node 1 terhubung ke Node 0, Node 2, dan Node 3
# Baris 2: Node 2 terhubung ke Node 0, Node 1, dan Node 3
# Baris 3: Node 3 terhubung ke Node 1 dan Node 2

