class BangunDatar:
    def hitungLuas(self):
        pass

class Persegi (BangunDatar):
    def __init__(self,sisi):
        self.sisi = sisi

    def hitungLuas(self):
        return self.sisi ** 2

class Lingkaran(BangunDatar):
    def __init__(self,jarijari):
        self.jarijari = jarijari

    def hitungLuas(self):
        return self.jarijari ** 2 * 3.14 
    
lingkaran = Lingkaran(3)
persegi = Persegi(5)

print(f"Luas Persegi : {persegi.hitungLuas()}")
print(f"Luas Lingkaran : {lingkaran.hitungLuas()}")