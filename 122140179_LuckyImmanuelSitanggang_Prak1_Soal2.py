jari2 = int(input("Masukkan jari - jari : "))
phi = 3.14

if(jari2 < 0):
    print ("jari-jari lingkaran tidak boleh negatif")
else:
    Keliling = phi * jari2 * 2
    Luas = phi * jari2 * jari2
    print ("Keliling lingkaran = " + str(Keliling))
    print ("Luas lingkaran = " + str(Luas))
