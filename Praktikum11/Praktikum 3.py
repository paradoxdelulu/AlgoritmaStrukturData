#=============================================================
# Nama  : Asma Mazaya
# NIM   : J0403251105
# Kelas : A1
# Praktikum 3 : Adjacency Matrix to Adjacency List
#=============================================================
# Adjacency Matrix to Adjacency List
adjacency_matrix = [
    [0, 1, 1, 0],  # Baris 0: Node 0 terhubung ke Node 1 dan Node 2
    [1, 0, 1, 0],  # Baris 1
    [1, 1, 0, 1],  # Baris 2
    [0, 0, 1, 0]   # Baris 3
]
# Mengubah adjacency matrix menjadi adjacency list
adjacency_list = {}
for i in range(len(adjacency_matrix)):
    adjacency_list[i] = []
    for j in range(len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] == 1:
            adjacency_list[i].append(j)
# Menampilkan adjacency list
print("Adjacency List:")
for node, neighbors in adjacency_list.items():
    print(f"{node}: {neighbors}")
# Penjelasan arti setiap baris:
# Baris 0: Node 0 terhubung ke Node 1 dan Node 2
# Baris 1: Node 1 terhubung ke Node 0 dan Node 2
# Baris 2: Node 2 terhubung ke Node 0, Node 1, dan Node 3
# Baris 3: Node 3 terhubung ke Node 2
