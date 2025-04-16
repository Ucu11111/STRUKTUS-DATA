# while loop 
"""
 syntax :
  while kondisi (true) : = selama bernilai true aksi

"""
angka = 0
print(f"angka awal -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")
print("keluar dari looping")

jawab = 'ya'
hitung = 0

while(jawab == 'ya'):
    hitung += 1
    jawab = input ("ulangi lagi atau tidak ?")
print(f"jumlah perulangan = {hitung}")