class Ongkir:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def hitung_harga(self):
        volume = self.panjang * self.lebar * self.tinggi

        berat_kg = round(self.berat)

        if volume > 50 and berat_kg >= 1:
            return 5000
        else:
            return "barang tidak memenuhi syarat pengiriman"
        
panjang = 5
lebar = 2
tinggi = 4
berat = 1

ongkos_kirim = Ongkir(panjang, lebar, tinggi, berat)
harga = ongkos_kirim.hitung_harga()

print(harga)


