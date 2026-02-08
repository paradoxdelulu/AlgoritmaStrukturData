# ========================================================== 
# TUGAS HANDS-ON MODUL 1 
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt) 
# 
# Nama  : Asma Mazaya
# NIM   : J0403251105
# Kelas : A1
# ==========================================================

# ------------------------------- 
# Konstanta nama file 
# ------------------------------- 
NAMA_FILE = "stok_barang.txt" 

# ------------------------------- 
# Fungsi: Membaca data dari file 
# ------------------------------- 
def baca_stok(nama_file):
    """ 
    Membaca data stok dari file teks. 
    Format per baris: KodeBarang,NamaBarang,Stok 

    Output: - stok_dict (dictionary) 
    key   = kode_barang 
    value = {"nama": nama_barang, "stok": stok_int}     
    """
    stock_dict = {}
    with open 
