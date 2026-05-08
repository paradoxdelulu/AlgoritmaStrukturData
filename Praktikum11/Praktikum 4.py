#=============================================================
# Nama  : Asma Mazaya
# NIM   : J0403251105
# Kelas : A1
# Praktikum 4 : Studi Kasus Dunia Nyata
# Digit akhir NIM : 5
# Studi Kasus : Jaringan Komputer
#===================================================
graph = {
    "Router": ["Switch"],
    "Switch": ["Router", "PC1", "PC2", "Server", "Printer"],
    "PC1": ["Switch", "Server"],
    "PC2": ["Switch"],
    "Server": ["Switch", "PC1"],
    "Printer": ["Switch"]
}


print("Adjacency List:")
for node in graph:
    print(node, "->", graph[node])

nodes = ["Router", "Switch", "PC1", "PC2", "Server", "Printer"]

matrix = [
    [0,1,0,0,0,0],
    [1,0,1,1,1,1],
    [0,1,0,0,1,0],
    [0,1,0,0,0,0],
    [0,1,1,0,0,0],
    [0,1,0,0,0,0]
]

print("Node:")
print(nodes)

print("\nAdjacency Matrix:")
for row in matrix:
    print(row)