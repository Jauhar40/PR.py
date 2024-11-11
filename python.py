nama = input("Masukkan Nama Anda:")
tahun_lahir = int(input("Masukkan Tahun Lahir Anda:"))
if 1944 >= tahun_lahir and tahun_lahir <= 1964:
  generasi = "Baby Boomer"
elif tahun_lahir >= 1965 and tahun_lahir <= 1979:
        generasi = 'Generasi X'
elif tahun_lahir >= 1980 and tahun_lahir <= 1994:
        generasi = 'Generasi Y Millennials'
elif tahun_lahir >= 1995 and tahun_lahir <= 2015:
        generasi = 'Generasi Z'
else:
        generasi = 'Tahun lahir tidak valid untuk kategori generasi yang ada';
    

print("Nama anda adalah", nama, "Anda lahir pada tahun", tahun_lahir, nama, "berdasarkan tahun lahir anda tergolong", generasi)