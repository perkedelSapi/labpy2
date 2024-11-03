tipe_tiket=input("Masukkan tipe tiket(reguler/vip): ")
if tipe_tiket=="reguler":
    harga=50000
elif tipe_tiket=="vip":
    harga=100000
else:
    print("Tiket tidak valid")
    exit()
member=input("Punya kartu member? ya/tidak:")

diskon = 0.8 * harga if member == 'ya' else 1 *harga
totalharga = diskon

print("Total harga:", totalharga)