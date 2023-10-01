class Kalkulator:
    def __init__(self, input_number1, input_number2):
        self.number1 = input_number1
        self.number2 = input_number2

    def jumlah(self):
        print(self.number1 + self.number2)

    def kurang(self):
        print(self.number1 - self.number2)

    def kali(self):
        print(self.number1 * self.number2)

    def bagi(self):
        print(self.number1 / self.number2)

penjumlahan = Kalkulator(3, 4)
pengurangan = Kalkulator(15,4)
perkalian = Kalkulator(10, 10)
pembagian = Kalkulator(12, 3)

penjumlahan.jumlah()
pengurangan.kurang()
perkalian.kali()
pembagian.bagi()