import os
import datetime
import django
import pandas as pd

# setting django orm environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pmoWa.settings")
django.setup()

# import database model yg diperlukan
from penggunaanobat.models import Resep

def grab_data(tglbwh, tglatas):
    q = Resep.objects.filter(kunjungan_pasien__tanggal_kunjungan__gte=datetime.date(int(tglbwh[6:11]),int(tglbwh[3:5]),int(tglbwh[0:2]))).filter(kunjungan_pasien__tanggal_kunjungan__lte=datetime.date(int(tglatas[6:11]),int(tglatas[3:5]),int(tglatas[0:2]))).order_by('obat')
    return q
    
def hitung_jenis(query):
    daftar_obat = []
    for i in query:
        if i.obat.nama_obat in daftar_obat:
            pass
        else:
            daftar_obat.append(i.obat.nama_obat)
    return daftar_obat
    
def generate_excel(daftar_obat, query, tglbwh, tglatas):
    key_pair = {}
    for i in daftar_obat:
        key_pair[i] = 0
    for i in query:
        key_pair[i.obat.nama_obat] += i.jumlah_obat
    df = pd.DataFrame({"Nama Obat": [ obat for obat in key_pair.keys() ], "Penggunaan Total": [ jumlah for jumlah in key_pair.values()]})
    df.to_excel("Pemakain_BMHP__{}-{}.xlsx".format(tglbwh, tglatas))

def main():
    tglbwh = input("""
    Masukkan tanggal awal, dengan format DD-MM-YYYY
    Contoh: 01-12-2020

    Tanggal awal: """)

    tglatas = input("""
    Masukkan tanggal akhir, dengan format DD-MM-YYYY
    Contoh: 30-12-2020
        
    Tanggal akhir: """)
    
    query = grab_data(tglbwh, tglatas)
    daftar_obat = hitung_jenis(query)
    jumlahnya = generate_excel(daftar_obat, query, tglbwh, tglatas)
    
    print("Selesai..")
    
    exit()