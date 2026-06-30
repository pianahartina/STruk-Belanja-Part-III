# 1. siapkan data / variabel 
# Data toko
nama_toko = "RIFATH BABY STORE"
alamat1 = " JL. BINTARO PUSAT "
alamat2 = " BLK. RI NO 321, TGR "

# Data transaksi
term_id = "A3245789"
merch_id = "000000674321"
nama_kasir = "PIANA HARTINA"
issuer = "BRI"
pan = "987123456789"
metode = "PAYMENT QR"
tanggal = "30 JUN, 26"
jam = "18:01"
batch = "000987"
trace_no = "023467"
ref_no = "78172939849"
rrrn_qris = "1345673890"
appr_code = "650973"
total_bayar = 92900 # pakai int biar gampang dihitung
total_lengkap = f"Rp. {total_bayar:,}"

#2. print struk / load
print("-" * 27)
print(" " * 10 + "BCA") #spasi biar ke tengah
print(f"{nama_toko}")
print(f"{alamat1}")
print(f"{alamat2}")
print("-" * 27)

print(f"TERM# {term_id:<12} MERCH# {merch_id}")
print("SWITCHING")
print(f"CARDHOLDER: {nama_kasir}")
print(f"Issuer: {issuer}")
print(f"PAN#{pan}")
print(f"{metode:<15} DATE/TIME {tanggal} {jam}")
print(f"BATCH : {batch:<8} TRACE NO: {trace_no}")
print(f"REF.NO. {ref_no:<10} APPR.CODE {appr_code}")
print(f"RRRN QRIS {rrrn_qris}")
print("-" * 27)
print(f"TOTAL {total_lengkap:>21}") 
print(" *** SIGNATURE NOT REQUIRED ***")
print("=" * 27)
print(" **Cardholder Copy**")

#<12 = Rata kiri 12 karakter. 
# >18 = Rata kanan 18 karakter. 
# Ini f-string formatting.f'{total_bayar:,}' = Koma otomatis. 
# 92900 -> 92,900print("=" * 32) = Garis cepat tanpa ngetik = 32x.

 