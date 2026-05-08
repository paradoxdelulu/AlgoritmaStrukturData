#=============================================================
# Nama  : Asma Mazaya
# NIM   : J0403251105
# Kelas : A1
# Praktikum 2 : # Adjacency List
#===============================================
adjacency_list = {
    'A': ['B', 'C'],  # Node A terhubung ke Node B dan Node C
    'B': ['A', 'D'],  # Node B terhubung ke Node A dan Node D
    'C': ['A', 'D'],  # Node C terhubung ke Node A dan Node D
    'D': ['B', 'C']   # Node D terhubung ke Node B dan Node C
}
# Menampilkan adjacency list
print("Adjacency List:")
for node, neighbors in adjacency_list.items():
    print(f"{node}: {neighbors}")
# Penjelasan arti setiap baris:
# Baris A: Node A terhubung ke Node B dan Node C
# Baris B: Node B terhubung ke Node A dan Node D
# Baris C: Node C terhubung ke Node A dan Node D
# Baris D: Node D terhubung ke Node B dan Node C
