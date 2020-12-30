from pengingat.models import DataPasien, DataObat
import csv
import datetime

def menginput_pasien():
    with open('data_pasien.csv', 'r') as f:
        rd = csv.reader(f)
        for i in rd:
            a = DataPasien(no_kartu=i[1], nama_pasien=i[0], alamat=i[3], usia=datetime.datetime.strptime(i[2], '%d-%m-%Y'), no_whatsapp=00000)
            a.save()
            print(i[0], i[1], i[2], i[3])
            
            
def menginput_obat():
    with open('daftar_obat.csv', 'r') as f:
        rd = csv.reader(f)
        for i in rd:
            a = DataObat(nama_obat=i[0], satuan=i[1], ab=i[2])
            a.save()
            print(i[0], i[1], i[2])