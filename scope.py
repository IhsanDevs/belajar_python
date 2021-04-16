teks = "Hello World"

def ubah(teksUbah = "-"):
 global teks
 teks = teksUbah
 return teks

print("\n\nTeks yg belum diubah adalah =", teks)
print("\nTeks yang sudah diubah adalah =", ubah("Ihsan Devs"),"\n\n")