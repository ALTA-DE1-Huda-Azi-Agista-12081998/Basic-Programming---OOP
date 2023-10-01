class Persegi:
    def __init__(self, input_number):
        self.number = input_number

    def luas(self):
        print(self.number * self.number)
    
    def keliling(self):
        print( self.number * self.number)
    
persegi = Persegi(4)
persegi.luas()
persegi.keliling()

class Segitiga:
    def __init__(self, input_number_1, input_number_2):
        self.alas = input_number_1
        self.tinggi = input_number_2

    def luas(self):
        print(0.5 * (self.alas * self.tinggi))

    def keliling(self):
        print(self.alas + self.tinggi + ((self.alas ** 2 + self.tinggi ** 2) ** 0.5))

segitiga = Segitiga(3, 4)
segitiga.luas()
segitiga.keliling()

class PersegiPanjang:
    def __init__(self, input_number1, input_number2):
        self.lebar = input_number1
        self.panjang = input_number2

    def luas(self):
        print(self.lebar * self.panjang)

    def keliling(self):
        print(2 * (self.lebar + self.panjang))

persegi_panjang = PersegiPanjang(7,8)
persegi_panjang.luas()
persegi_panjang.keliling()