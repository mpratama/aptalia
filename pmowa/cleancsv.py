# coding: utf-8
import csv

def anuw():
    namafile = input("Nama CSV? ")
    with open(namafile, 'r') as f, open(namafile.replace(".csv", "_cleaned.csv") , 'w') as o:
        rd = csv.reader(f)
        wr = csv.writer(o)
        nama = ""
        no_r = ""
        for i in rd:
            if nama != i[0] and no_r != i[1]:
                nama = i[0]
                no_r = i[1]
                #print(x)
                wr.writerow([nama, no_r, i[2], i[3], i[4], i[5], "", nama[-10:], "isi_no_urut", nama[0], nama[nama.find("(")+1:nama.find(")")], i[0]])
            else:
                #print(" ")
                wr.writerow(["", "", i[2], i[3], i[4], i[5], "", "", "", "", "", i[0]])
                
if __name__ == "__main__":
    anuw()

#utk hitung kolom jumlah obat pake rumus excel ini
# =countif(range, criteria)