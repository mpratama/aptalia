from django.db import models
from math import ceil
from datetime import timedelta, datetime

def valcheck(w):
    x = 0
    if w:
        x += 1
    else:
        pass
    return x

def lama_pengobatan(start, jml_obat, w0, w1, w2, w3, w4, jml_minum):
    x0 = valcheck(w0)
    x1 = valcheck(w1)
    x2 = valcheck(w2)
    x3 = valcheck(w3)
    x4 = valcheck(w4)
    mulai_minum_obat = start
    lama_minum_obat = jml_obat/((x0+x1+x2+x3+x4)*jml_minum)
    return mulai_minum_obat + timedelta(days=ceil(lama_minum_obat)-1)

# Create your models here.
class DataPasien(models.Model):
    no_kartu = models.CharField(max_length=20, help_text="Masukkan no BPJS / KTP", default="000", verbose_name="Nomor Kartu")
    nama_pasien = models.CharField(max_length=30, help_text="Masukkan nama", verbose_name="Nama Pasien")
    alamat = models.CharField(max_length=50, help_text="Masukkan alamat")
    usia = models.DateField(help_text="dd-mm-yy", verbose_name="Tanggal Lahir", blank=True, null=True)
    no_whatsapp = models.CharField(max_length=15, help_text="masukkan dengan format +628XXXXXXXXXX", verbose_name="No Whatsapp")
    def __str__(self):
        u = self.umur()
        return  str(self.nama_pasien) + " (" + u + ") " + ", " + str(self.alamat[:30])
    def umur(self):
        usianya = datetime.now().year - self.usia.year
        rendering = "{} tahun".format(usianya)
        return str(rendering)
    class Meta:
        verbose_name_plural = "Data Pasien"
        
class DataObat(models.Model):
    nama_obat = models.CharField(max_length=50, help_text="Tulis nama obat dan dosisnya")
    SAT = (
        ('TAB', 'Tablet'),
        ('CAP', 'Kapsul'),
        ('BKS', 'Bungkus'),
        )
    satuan = models.CharField(max_length=3, choices=SAT, help_text="Bentuk sediaan", verbose_name="Bentuk sediaan")
    def __str__(self):
        return str(self.nama_obat) + " " + str(self.satuan)
    class Meta:
        verbose_name_plural = "Data Obat"

class Kunjungan(models.Model):
    nama_pasien = models.ForeignKey(DataPasien, on_delete=models.CASCADE)
    tanggal_kunjungan = models.DateField(help_text="Tanggal pasien berobat", verbose_name="Tgl Berobat")
    def __str__(self):
        return str(self.nama_pasien) + " | " + str(self.tanggal_kunjungan)
    class Meta:
        verbose_name_plural = "Data Kunjungan"

class Resep(models.Model):
    kunjungan_pasien = models.ForeignKey(Kunjungan, on_delete=models.CASCADE)
    nama_obat = models.ForeignKey(DataObat, on_delete=models.CASCADE)
    jumlah_obat = models.PositiveSmallIntegerField(blank=False, null=False)
    mulai_minum = models.DateField(blank=False, null=False)
    waktu_minum0 = models.TimeField(blank=False, null=False, verbose_name="Waktu minum 1")
    waktu_minum1 = models.TimeField(blank=True, null=True, verbose_name="Waktu minum 2")
    waktu_minum2 = models.TimeField(blank=True, null=True, verbose_name="Waktu minum 3")
    waktu_minum3 = models.TimeField(blank=True, null=True, verbose_name="Waktu minum 4")
    waktu_minum4 = models.TimeField(blank=True, null=True, verbose_name="Waktu minum 5")
    jumlah_obat_minum = models.PositiveSmallIntegerField(blank=False, null=False)
    selesai_minum_obat = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.nama_obat)
    def save(self, *args, **kwargs):
        self.selesai_minum_obat = lama_pengobatan(self.mulai_minum, self.jumlah_obat, self.waktu_minum0, self.waktu_minum1, self.waktu_minum2, self.waktu_minum3, self.waktu_minum4, self.jumlah_obat_minum)
        super(Resep, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Resep"