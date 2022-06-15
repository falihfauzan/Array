import numpy as np
warga = ["Rudi","Bambang","Iman","Asep"]
print("====================")

# MENAMPILKAN SEMUA NILAI ARRAY
for data in warga:
    print (data)
print("====================")

# MENGHITUNG TOTAL PANJANG ARRAY
total = len(warga)
print (total)
print("====================")

# MENGAMBIL NILAI DALAM ARRAY
print (warga[1])
print("====================")

# MENAMBAHKAN NILAI ARRAY
warga.append("Rizal")
print(warga)
print("====================")

# MENGHAPUS NILAI ARRAY
del warga[0]
print(warga)
print("====================")

# ARRAY 2 DIMENSI
siswa =np.array([["Rani","Adit","Riko","Dodi"], [1,2,3,4]])
print (siswa)

#ARRAY 3 DIMENSI
a=np.arange(1,100,1)
print(a)