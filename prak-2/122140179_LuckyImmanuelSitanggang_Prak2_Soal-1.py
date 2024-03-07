class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, new_nama):
        self.__nama = new_nama

    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, new_nim):
        self.__nim = new_nim

    def kondisi(self, semester_sekarang , ipk):
        if semester_sekarang <= 2 :
            if ipk < 2.0:
                return f"Mengulang TPB"
            else :
                return f"Lulus Masa TPB"
        else :
            return f"TPB dah lulus,lulus kuliahnya kapan"

    def hitung_ipk(self, nilai_sks, sks_tempuh):
        if sks_tempuh == 0:
            return 0
        return round(nilai_sks / sks_tempuh, 2)

    def cek_status_aktif(self, semester_sekarang):
        if semester_sekarang <= self.angkatan + 4:
            return "Aktif"
        return "Tidak Aktif"

    
mahasiswa1 = Mahasiswa("122140179", "Lucky" , 2022)

mahasiswa2 = Mahasiswa("122140181" , "Rachel", 2022)

mahasiswa1.nama = "Untung"

ipk_mhs1 = mahasiswa1.hitung_ipk(82.8, 23)

kondisi_mhs1 = mahasiswa1.kondisi(3,3.0)
kondisi_mhs2 = mahasiswa2.kondisi(2,1.9)

status_mhs1 = mahasiswa1.cek_status_aktif(4)
status_mhs2 = mahasiswa2.cek_status_aktif(4)

print(f"IPK {mahasiswa1.nama}: {ipk_mhs1}")
print(f"{mahasiswa1.nama} - Angkatan {mahasiswa1.angkatan } : {status_mhs1} - Kondisi TPB : {kondisi_mhs1}")
print(f"{mahasiswa2.nama} - Angkatan {mahasiswa2.angkatan} : {status_mhs2} - Kondisi TPB : {kondisi_mhs2}")
