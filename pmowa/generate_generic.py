import os
import datetime
import django
import pandas as pd

# setting django orm environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pmoWa.settings")
django.setup()

# import database model yg diperlukan
from penggunaanobat.models import Resep, DataKunjungan

# prompt user
tglbwh = input("""
Masukkan tanggal awal, dengan format DD-MM-YYYY
Contoh: 01-12-2020

Tanggal awal: """)

tglatas = input("""
Masukkan tanggal akhir, dengan format DD-MM-YYYY
Contoh: 30-12-2020
    
Tanggal akhir: """)

non_generic = ["Scabimite (Permetrin) 5% krim 10 gr", "Carboxymetyhlcelulose (Cendo Cenfresh) eye drop 5 ml", "Cendo Lyteers 15 ml", "Cendo Xitrol eye drop 5 ml", "Lactobacillus", "Multivitamin dan mineral tetes sirup@ 15 ml", "Pehavral vitamin", "Anvomer B6", "Tremenza", "Thrombopob gel", "Bioplacenton Neocenta"]

# method pengambil data utama
def grabdata():
    q1 = DataKunjungan.objects.filter(tanggal_kunjungan__gte=datetime.date(int(tglbwh[6:11]),int(tglbwh[3:5]),int(tglbwh[0:2]))).filter(tanggal_kunjungan__lt=datetime.date(int(tglatas[6:11]),int(tglatas[3:5]),int(tglatas[0:2])))
    q2 = Resep.objects.filter(kunjungan_pasien__tanggal_kunjungan__gte=datetime.date(int(tglbwh[6:11]),int(tglbwh[3:5]),int(tglbwh[0:2]))).filter(kunjungan_pasien__tanggal_kunjungan__lte=datetime.date(int(tglatas[6:11]),int(tglatas[3:5]),int(tglatas[0:2])))
    return q1, q2
print("Tunggu sebentar: Mengambil data .....")

# grab data kunjungan dan data resep
data_kunjungan, data_resep = grabdata()
    
def generate_pandas():
    score_dr_suzi = 0
    score_dr_nurul = 0
    score_dr_dwi = 0
    score_dr_internship = 0
    score_non_dr = 0
    for i in data_kunjungan:
        if i.nama_dokter == "suz":
            score_dr_suzi += 1
            print("Hitung lembar dr Suzi: {}".format(score_dr_suzi))
        elif i.nama_dokter == "nur":
            score_dr_nurul += 1
            print("Hitung lembar dr Nurul: {}".format(score_dr_nurul))
        elif i.nama_dokter == "dwi":
            score_dr_dwi += 1
            print("Hitung lembar dr Dwi: {}".format(score_dr_dwi))
        elif i.nama_dokter == "int":
            score_dr_internship += 1
            print("Hitung lembar dr Internship: {}".format(score_dr_internship))
        else:
            score_non_dr += 1
            print("Hitung lembar non dokter {}".format(score_non_dr))
    tot_lembar = score_dr_suzi + score_dr_nurul + score_dr_dwi + score_dr_internship
            
    score_r_dr_suzi = 0
    score_r_dr_nurul = 0
    score_r_dr_dwi = 0
    score_r_dr_internship = 0
    score_r_non_dr = 0
    for i in data_resep:
        if i.kunjungan_pasien.nama_dokter == "suz":
            score_r_dr_suzi += 1
            print("Hitung jumlah R/ total dr Suzi: {}".format(score_r_dr_suzi))
        elif i.kunjungan_pasien.nama_dokter == "nur":
            score_r_dr_nurul += 1
            print("Hitung jumlah R/ total dr Nurul: {}".format(score_r_dr_nurul))
        elif i.kunjungan_pasien.nama_dokter == "dwi":
            score_r_dr_dwi += 1
            print("Hitung jumlah R/ total dr Dwi: {}".format(score_r_dr_dwi))
        elif i.kunjungan_pasien.nama_dokter == "int":
            score_r_dr_internship += 1
            print("Hitung jumlah R/ total dr Internship: {}".format(score_r_dr_internship))
        else:
            score_r_non_dr += 1
            print("Hitung jumlah R/ total non dokter {}".format(score_r_non_dr))
    tot_r = score_r_dr_suzi + score_r_dr_nurul + score_r_dr_dwi + score_r_dr_internship
            
    score_g_dr_suzi = 0
    score_g_dr_nurul = 0
    score_g_dr_dwi = 0
    score_g_dr_internship = 0
    score_g_non_dr = 0
    for i in data_resep:
        if i.kunjungan_pasien.nama_dokter == "suz":
            if i.obat.nama_obat in non_generic:
                pass
            else:
                score_g_dr_suzi += 1
                print("Hitung jumlah R/ non generic total dr Suzi: {}".format(score_g_dr_suzi))
        elif i.kunjungan_pasien.nama_dokter == "nur":
            if i.obat.nama_obat in non_generic:
                pass
            else:
                score_g_dr_nurul += 1
                print("Hitung jumlah R/ non generic dr Nurul: {}".format(score_g_dr_nurul))
        elif i.kunjungan_pasien.nama_dokter == "dwi":
            if i.obat.nama_obat in non_generic:
                pass
            else:
                score_g_dr_dwi += 1
                print("Hitung jumlah R/ non generic dr Dwi: {}".format(score_g_dr_dwi))
        elif i.kunjungan_pasien.nama_dokter == "int":
            if i.obat.nama_obat in non_generic:
                pass
            else:
                score_g_dr_internship += 1
                print("Hitung jumlah R/ non generic dr Internship: {}".format(score_g_dr_internship))
        else:
            if i.obat.nama_obat in non_generic:
                pass
            else:
                score_g_non_dr += 1
                print("Hitung jumlah R/ non generic non dokter: {}".format(score_g_non_dr))
        tot_g = score_g_dr_suzi + score_g_dr_nurul + score_g_dr_dwi + score_g_dr_internship
    
    suz = pd.DataFrame({"Nama Dokter": ["dr. Suzi Leoni A."], "Jumlah Lembar": [score_dr_suzi], "Jumlah R/": [score_r_dr_suzi], "Jumlah R/ Generic": [score_g_dr_suzi], "% Generic": ["{:.2f}".format((score_g_dr_suzi / score_r_dr_suzi) * 100)]})
    nur = pd.DataFrame({"Nama Dokter": ["dr. Nurul Pratiwi"], "Jumlah Lembar": [score_dr_nurul], "Jumlah R/": [score_r_dr_nurul], "Jumlah R/ Generic": [score_g_dr_nurul], "% Generic": ["{:.2f}".format((score_g_dr_nurul / score_r_dr_nurul) * 100)]})
    dwi = pd.DataFrame({"Nama Dokter": ["dr. Dwi Yosta C."], "Jumlah Lembar": [score_dr_dwi], "Jumlah R/": [score_r_dr_dwi], "Jumlah R/ Generic": [score_g_dr_dwi], "% Generic": ["{:.2f}".format((score_g_dr_dwi / score_r_dr_dwi) * 100)]})
    intern = pd.DataFrame({"Nama Dokter": ["dr Internship"], "Jumlah Lembar": [score_dr_internship], "Jumlah R/": [score_r_dr_internship], "Jumlah R/ Generic": [score_g_dr_internship], "% Generic": ["{:.2f}".format((score_g_dr_internship / score_r_dr_internship) * 100)]})
    nondr = pd.DataFrame({"Nama Dokter": ["Non Dokter"], "Jumlah Lembar": [score_non_dr], "Jumlah R/": [score_r_non_dr], "Jumlah R/ Generic": [score_g_non_dr]})
    print("\ndata non resep dokter: tidak dimasukkan ke file excel, adalah sebagai berikut:\n")
    print("{}\n".format(nondr))   
    
    frames = pd.concat([suz, nur, dwi, intern])
    print("Mengexpor ke fail excel...")
    frames.to_excel("LAP-GENERIC__{}_{}.xlsx".format(tglbwh, tglatas))
    
    print("\n LAP-GENERIC__{}-{}.xlsx selesai dicetak..".format(tglbwh, tglatas))
    
generate_pandas()