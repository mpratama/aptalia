# coding: utf-8

# Import lib yg diperlukan
import os
import datetime
import django
import pandas as pd
import re

# setting django orm environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pmoWa.settings")
django.setup()

# import database model yg diperlukan
from penggunaanobat.models import Resep
from pengingat.models import DataObat

# prompt user
tglbwh = input("Masukkan tanggal awal: ")
tglatas = input("Masukkan batas atas: ")

# query obat golongan antibiotik
antibiotik = DataObat.objects.filter(ab=True)

# query data kunjungan beserta atribut2 dan filternya
data = Resep.objects.filter(kunjungan_pasien__tanggal_kunjungan__gte=datetime.date(int(tglbwh[6:11]),int(tglbwh[3:5]),int(tglbwh[0:2]))).filter(kunjungan_pasien__tanggal_kunjungan__lt=datetime.date(int(tglatas[6:11]),int(tglatas[3:5]),int(tglatas[0:2]))).filter(kunjungan_pasien__diagnosa__diagnosa="ISPA")

# mulai ke bawah sini hoream dokumentasi, baca weh olangan
# terutama konsep enumerate list
# dan DataFrame / Series pada library pandas

def namapas(data):
    nama = []
    nama_cleaned = []
	
    for i in data:
        nama.append(i.kunjungan_pasien.nama_pasien)
    for idx, item in enumerate(nama):
        if not idx:
            nama_cleaned.append(item)
        elif item == nama[idx-1]:
            nama_cleaned.append("")
        else:
            nama_cleaned.append(item)
    return nama_cleaned
	
def koltgl(data, nm_pasien):
    tgl = []
    tgl_cleaned = []
    
    for i in data:
        tgl.append(i.kunjungan_pasien.tanggal_kunjungan)
    for idx, item in enumerate(tgl):
        if nm_pasien[idx] != "":
            tgl_cleaned.append(item)
        else:
            tgl_cleaned.append("")
    return tgl_cleaned

def kolno(kol_tgl):
    nomor = 1
    num_cleaned = []
    
    for i in kol_tgl:
        if i != "":
            num_cleaned.append(nomor)
            nomor += 1
        else:
            num_cleaned.append("")
    return num_cleaned

def regex_usia(nm_pasien):
    usia_cleaned = []
    pola_regex = "[0-9]{1,2} tahun"
    for idx, item in enumerate(nm_pasien):
        grabber = re.search(pola_regex, str(item))
        if item != "":
            usia_cleaned.append(grabber.group())
        else:
            usia_cleaned.append("")
    return usia_cleaned
    
def isAntibiotik(nm_obat):
    list_antibiotik = []
    ab_cleaned = []
    for i in antibiotik:
        list_antibiotik.append(i.nama_obat)
    for idx, item in enumerate(nm_obat):
        if item in list_antibiotik:
            ab_cleaned.append("Ya")
        else:
            ab_cleaned.append("")
    return ab_cleaned
    
def hitung_jml(data):
    list_nama = []
    jml_cleaned = []
    counter = 1
    for i in data:
        list_nama.append(i.kunjungan_pasien.nama_pasien.nama_pasien)
    for idx, item in enumerate(list_nama):
        #print(idx, item)
        if not idx:
            pass
        elif (len(list_nama))-1 == idx:
            counter += 1
            jml_cleaned.append(counter)
        elif item == list_nama[idx-1]:
            counter += 1
            jml_cleaned.append("")
        else:
            jml_cleaned.append(counter)
            counter = 1
    return jml_cleaned
    
    
nm_obat = pd.Series([x.obat.nama_obat for x in data])
nm_pasien = pd.Series(namapas(data))
kol_tgl = pd.Series(koltgl(data, nm_pasien))
kol_usia = pd.Series(regex_usia(nm_pasien))
kol_num = pd.Series(kolno(kol_tgl))
kol_aturan = pd.Series([x.aturan_minum for x in data])
kol_lama_pengobatan = pd.Series([x.lama_pengobatan for x in data])
kol_antibiotik = pd.Series(isAntibiotik(nm_obat))

df = pd.DataFrame({"Tanggal": kol_tgl})
df = df.join(pd.DataFrame({"Nomor": kol_num})).join(pd.DataFrame({"Nama Pasien": nm_pasien})).join(pd.DataFrame({"Umur": kol_usia})).join(pd.DataFrame({"Obat": nm_obat})).join(pd.DataFrame({"Antibiotik?": kol_antibiotik})).join(pd.DataFrame({"Aturan Pakai": kol_aturan})).join(pd.DataFrame({"Lama Pengobatan (hari)": kol_lama_pengobatan})).join(pd.DataFrame({"Jumlah Item": hitung_jml(data)}))
df.to_excel("POR-ISPA__{}_{}.xlsx".format(tglbwh, tglatas))