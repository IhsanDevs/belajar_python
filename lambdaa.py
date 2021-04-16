def jumlah(nilai1 = 1, nilai2 = 1):
    hasil = nilai1 + nilai2
    return hasil

panggil = jumlah(10,2)
print(panggil)



# Membuat anonymous function dengan lambda
test = lambda arguments : print(arguments)

test("halo")