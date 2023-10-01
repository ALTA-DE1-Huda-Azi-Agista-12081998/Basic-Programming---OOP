class Volume:
    def hitung_volume_kubus(self, sisi):
        print( sisi ** 3)

    def hitung_volume_balok(self, panjang, lebar, tinggi):
        print( panjang * lebar * tinggi)

    def hitung_volume_tabung(self, jari_jari, tinggi):
        pi = 3.14159  
        print( pi * jari_jari ** 2 * tinggi)

vlm = Volume()
vlm.hitung_volume_kubus(10)
vlm.hitung_volume_balok(3, 6, 10)
vlm.hitung_volume_tabung(7,10)

