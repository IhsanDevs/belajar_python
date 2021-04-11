nilai = int(input("Masukkan nilai = "))
hias = 50*"="
if nilai > 100:
    print(hias)
    print("Nilai yang kamu masukkan tidak valid\nSilahkan jalankan ulang program!")
elif 80 <= nilai <= 100:
    print(hias)
    print("Nilai Anda adalah A. Selamat! Anda lulus\n")
elif 60 <= nilai <= 80:
    print(hias)
    print("Nilai Anda adalah B. Belajarlah lebih giat\n")
else:
    print(hias)
    print("Aduh! Sayang sekali. Kamu tidak lulus\n")