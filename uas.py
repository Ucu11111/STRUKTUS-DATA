# 1. Input nama customer dan tanggal belanja, simpan dalam tuple
nama = input("Masukkan nama customer: ")                # Meminta mengetikkan nama orang yang belanja
tanggal = input("Masukkan tanggal belanja (contoh: 14-07-2025): ")  # Meminta anak mengetikkan tanggal belanja
data_customer = (nama, tanggal)                         # Menyimpan nama dan tanggal dalam satu tempat (tuple)

# 2. Input jumlah barang yang akan dibeli
jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))  # Menanyakan berapa banyak barang yang dibeli

# 3. Input data tiap barang, simpan dalam dictionary
daftar_belanja = []                                     # Menyediakan tempat kosong untuk menyimpan semua barang

for i in range(jumlah_barang):                          # Mengulang sesuai jumlah barang
    print(f"\nBarang ke-{i+1}")                         # Memberitahu barang ke berapa yang sedang diisi
    nama_barang = input("Nama barang: ")                # Meminta nama barang, misalnya "Pensil"
    harga_satuan = float(input("Harga satuan: "))       # Meminta harga satuannya, misalnya "2000"
    qty = int(input("Jumlah (QTY): "))                  # Meminta jumlah barang yang dibeli, misalnya "3"
    
    # Membuat dictionary untuk barang ini
    barang = {
        "nama_barang": nama_barang,                     # Menyimpan nama barang
        "harga_satuan": harga_satuan,                   # Menyimpan harga satuan barang
        "qty": qty,                                     # Menyimpan berapa banyak yang dibeli
        "total": harga_satuan * qty                     # Menghitung total harga = harga satuan x jumlah
    }
    
    daftar_belanja.append(barang)                       # Menambahkan barang ini ke daftar belanja

# 5. Tampilkan data customer, daftar belanja, dan total bayar
print("\n===== STRUK BELANJA =====")                     # Menampilkan garis judul struk
print(f"Nama Customer : {data_customer[0]}")            # Menampilkan nama orang yang belanja
print(f"Tanggal       : {data_customer[1]}")            # Menampilkan tanggal belanja
print("\nDaftar Belanja:")                              # Menampilkan daftar semua barang yang dibeli

total_bayar = 0                                         # Menyimpan jumlah semua harga barang, dimulai dari 0
for i, item in enumerate(daftar_belanja, start=1):      # Mengambil semua barang satu per satu
    print(f"{i}. {item['nama_barang']} - {item['qty']} x {item['harga_satuan']} = {item['total']}")  # Menampilkan info barang
    total_bayar += item["total"]                        # Menambahkan total harga barang ke total bayar

print(f"\nTotal Bayar: Rp {total_bayar:,.2f}")          # Menampilkan jumlah yang harus dibayar semuanya


# penjelasan singkat
# Tuple seperti data_customer digunakan untuk menyimpan dua hal dalam satu wadah, misalnya nama dan tanggal.
# List seperti daftar_belanja adalah tempat menyimpan banyak barang.
# Dictionary seperti barang = {...} dipakai untuk menyimpan informasi satu barang (nama, harga, jumlah, total).
# Kita pakai perulangan for untuk mengulang sesuai jumlah barang.
# Di akhir, kita jumlahkan semua harga dan tampilkan struk belanja.