class mahasiswa():
    nama = "Ini adalah nama"
    
    def belajar(self):
        print(self.nama, "sedang belajar")
nama_1 = mahasiswa()
nama_2 = mahasiswa()
nama_1.nama = 'Nanda'
nama_2.nama = 'Budi'
print(nama_1.nama)
print(nama_2.nama)
nama_1.belajar()
