
# Program Sewa Penginapan Danisha
print("="*45)
print("     SISTEM ADMINISTRASI PENGINAPAN Danisha     ")
print("="*45)

nama_penyewa = input("Nama Lengkap Penyewa     : ").title()
print("\nKategori Kamar: ")
print(" - Standar (Rp 200.000)")
print(" - Deluxe  (Rp 450.000)")
print(" - Suite   (Rp 800.000)")

tipe_kamar   = input("Tulis Tipe Kamar         : ")
harga_satuan = int(input("Masukkan Harga Satuan    : "))
durasi       = int(input("Durasi Menginap (Hari)   : "))

total = harga_satuan * durasi

print("\n" + "~"*45)
print("            STRUK PEMBAYARAN               ")
print("~"*45)
print(f"Penyewa         : {nama_penyewa}")
print(f"Kamar           : {tipe_kamar}")
print(f"Lama Inap       : {durasi} Hari")
print(f"Harga/Malam     : Rp {harga_satuan:,}")
print("-" * 45)
print(f"TOTAL TAGIHAN   : Rp {total:,}")
print("="*45)
print("       Harap simpan struk ini digital      ")